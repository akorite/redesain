// ch16_cpu8.v -- the C1 machine, complete.
//
// Architecture: pc(8) + rom256 + regfile8 + alu8 (ch14/15 modules
// unchanged, instantiated as a library) + flags + OUT register +
// combinational decoder + the smallest FSM that exists: RUN/HALT.
//
// ISA (ch16 freezes it; ch15 seeded the fields):
//   byte 0: { op[7:4], operand[3:0] }
//   byte 1 (2-byte ops only): immediate byte
//   0x0 NOP         pc+1
//   0x1 LDI A,imm   r0 <- imm,            pc+2
//   0x2 MOV rd      r[operand[2:0]] <- A, pc+1
//   0x3 ADD rs      A <- A + rs,          pc+1  (flags)
//   0x4 SUB rs      A <- A - rs,          pc+1  (flags)
//   0x5 AND rs      A <- A & rs,          pc+1  (flags)
//   0x6 JMP tgt     pc <- imm8,           2-byte
//   0x7 JZ  tgt     pc <- imm8 if Z,      2-byte
//   0x8 OUT         out <- A,             pc+1
//   0x9 HALT        pc holds forever
//   0xA MOVA rs     A <- rs,              pc+1
//
// Jump targets are a FULL BYTE (imm at pc+1), not the operand
// nibble: nibble jumps cannot reach past address 0x0F and real
// programs exceed 16 bytes. That is the one refinement ch15's
// seeded conventions needed.
module cpu8 (
  input  wire       i_clk,
  input  wire       i_rst,
  output wire [7:0] o_a,      // debug taps (top module keeps these)
  output wire [7:0] o_pc,
  output wire [7:0] o_instr,
  output wire [7:0] o_out,
  output wire       o_out_we, // pulses one cycle per OUT
  output wire       o_halted
);
  // ---------- sequencer state ----------
  reg [7:0] pc;
  reg       halted;

  // ---------- program ROM ----------
  reg [7:0] rom [0:255];
`ifdef ROMFILE
  initial $readmemh(`ROMFILE, rom);
`else
  initial $readmemh("ch16_fib.hex", rom);
`endif
  wire [7:0] instr = rom[pc];
  wire [7:0] imm8  = rom[pc + 8'd1];
  wire [3:0] op      = instr[7:4];
  wire [3:0] operand = instr[3:0];

  // ---------- datapath ----------
  reg        alu_we, flags_we, out_we, rf_we;
  reg  [1:0] wb_sel;         // 00=ALU 01=imm 10=portA 11=portB
  reg        dst_sel;        // 0=A(r0) 1=r[operand[2:0]]
  reg  [1:0] pc_mode;        // 00=+1 01=+2 10=jump(imm8) 11=hold
  reg  [2:0] alu_op;
  wire [7:0] rf_ra, rf_rb;
  wire [7:0] alu_y;
  wire       alu_z, alu_n, alu_c, alu_v;
  wire [7:0] wb_data = (wb_sel == 2'b00) ? alu_y :
                       (wb_sel == 2'b01) ? imm8  :
                       (wb_sel == 2'b10) ? rf_ra : rf_rb;
  wire [7:0] rf_waddr_ext = dst_sel ? {5'b0, operand[2:0]} : 8'd0;

  regfile8 rf (
    .i_clk(i_clk), .i_we(rf_we),
    .i_waddr(rf_waddr_ext[2:0]), .i_wdata(wb_data),
    .i_raddr_a(3'd0),                      // port A is always A
    .i_raddr_b(operand[2:0]),              // port B is the operand reg
    .o_ra(rf_ra), .o_rb(rf_rb)
  );

  alu8 alu (
    .i_a(rf_ra), .i_b(rf_rb), .i_op(alu_op),
    .o_y(alu_y), .o_z(alu_z), .o_n(alu_n),
    .o_c(alu_c), .o_v(alu_v)
  );

  reg [3:0] flags;   // {z,n,c,v}
  reg [7:0] out_reg;

  // ---------- the decoder: instr byte -> control word ----------
  // Combinational: this is the "fetch-decode-execute collapsed into
  // one cycle" the chapter explains.
  always @(*) begin
    rf_we = 0; flags_we = 0; out_we = 0;
    wb_sel = 2'b00; dst_sel = 1'b0; pc_mode = 2'b00; alu_op = 3'b000;
    case (op)
      4'h1: begin wb_sel=2'b01; dst_sel=0; rf_we=1; pc_mode=2'b01; end // LDI
      4'h2: begin wb_sel=2'b10; dst_sel=1; rf_we=1; end                // MOV rd
      4'h3: begin alu_op=3'b000; rf_we=1; flags_we=1; end              // ADD
      4'h4: begin alu_op=3'b001; rf_we=1; flags_we=1; end              // SUB
      4'h5: begin alu_op=3'b010; rf_we=1; flags_we=1; end              // AND
      4'h6: pc_mode = 2'b10;                                          // JMP
      4'h7: pc_mode = flags[3] ? 2'b10 : 2'b01;                       // JZ
      4'h8: out_we = 1;                                               // OUT
      4'h9: pc_mode = 2'b11;                                          // HALT
      4'hA: begin wb_sel=2'b11; dst_sel=0; rf_we=1; end                // MOVA
      default: ;                                                      // NOP etc.
    endcase
    if (halted) begin
      rf_we = 0; flags_we = 0; out_we = 0; pc_mode = 2'b11;
    end
  end

  // ---------- sequential side ----------
  always @(posedge i_clk) begin
    if (i_rst) begin
      pc <= 0; halted <= 0; flags <= 0; out_reg <= 0;
    end else if (!halted) begin
      case (pc_mode)
        2'b00:   pc <= pc + 8'd1;
        2'b01:   pc <= pc + 8'd2;
        2'b10:   pc <= imm8;
        default: pc <= pc;
      endcase
      if (op == 4'h9) halted <= 1;
      if (rf_we)    ; // regfile has its own enable inside
      if (flags_we) flags <= {alu_z, alu_n, alu_c, alu_v};
      if (out_we)   out_reg <= rf_ra;
    end
  end

  assign o_a = rf_ra;
  assign o_pc = pc;
  assign o_instr = instr;
  assign o_out = out_reg;
  assign o_out_we = out_we & ~halted;
  assign o_halted = halted;
endmodule
