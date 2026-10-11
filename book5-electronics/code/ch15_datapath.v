// Partial datapath for the C1 machine: PC + program ROM + regfile +
// the ch14 ALU + flags and OUT registers. There is no control unit in
// here on purpose -- the i_* lines ARE the control word, driven by the
// testbench in this chapter and by the fetch-decode-execute FSM in ch16.
//
// Conventions (the contract ch16 encodes):
//   instruction byte = {op[7:4], operand[3:0]}; rom[pc+1] is the
//   immediate byte for two-byte ops.
//   r0 is the accumulator A: ALU's left operand is always regfile[0].
//   WB mux: 00=alu result, 01=immediate byte, 10=port-A value, 11=port-B value.
//   DST: 0 = write r0 (A), 1 = write r[operand[2:0]].
//   PC: 00 = +1, 01 = +2 (two-byte op), 10 = operand[3:0], 11 = hold (HALT).
module datapath (
  input  wire        i_clk, i_rst,
  input  wire [2:0]  i_alu_op,
  input  wire [1:0]  i_wb_sel,
  input  wire        i_dst_sel,
  input  wire        i_we,
  input  wire        i_flags_we,
  input  wire        i_out_we,
  input  wire [1:0]  i_pc_mode,
  output wire [3:0]  o_pc,
  output wire [7:0]  o_instr,
  output wire [7:0]  o_imm,
  output wire [7:0]  o_a,
  output wire [7:0]  o_rb,
  output wire [7:0]  o_out,
  output wire        o_z, o_n, o_c, o_v
);
  localparam PC_NEXT = 2'b00, PC_SKIP = 2'b01, PC_JUMP = 2'b10, PC_HOLD = 2'b11;

  // program counter: the bus tap the control unit steers
  reg  [3:0] pc;
  wire [3:0] pc_next =
      i_pc_mode == PC_NEXT ? pc + 4'd1 :
      i_pc_mode == PC_SKIP ? pc + 4'd2 :
      i_pc_mode == PC_JUMP ? o_instr[3:0] : pc;
  always @(posedge i_clk) begin
    if (i_rst) pc <= 4'd0;
    else       pc <= pc_next;
  end
  assign o_pc = pc;

  // program memory: fetch this byte and the following (immediate) one
  rom16 urom(.i_addr(pc),       .o_data(o_instr));
  rom16 uimm(.i_addr(pc + 4'd1), .o_data(o_imm));

  // the ALU from ch14, unchanged -- now a processing element
  wire [7:0] port_a, port_b;
  wire [7:0] alu_y;
  wire alu_z, alu_n, alu_c, alu_v;
  alu8 alu(.i_a(port_a), .i_b(port_b), .i_op(i_alu_op),
           .o_y(alu_y), .o_z(alu_z), .o_n(alu_n), .o_c(alu_c), .o_v(alu_v));

  // register file: port A is wired to r0 (the accumulator convention);
  // port B follows the instruction's operand nibble.
  wire [7:0] wb_data =
      i_wb_sel == 2'b00 ? alu_y    :
      i_wb_sel == 2'b01 ? o_imm    :
      i_wb_sel == 2'b10 ? port_a   : port_b;
  wire [2:0] waddr = i_dst_sel ? o_instr[2:0] : 3'd0;
  regfile8 regs(
    .i_clk(i_clk), .i_we(i_we), .i_waddr(waddr), .i_wdata(wb_data),
    .i_raddr_a(3'd0), .i_raddr_b(o_instr[2:0]), .o_ra(port_a), .o_rb(port_b)
  );
  assign o_a  = port_a;
  assign o_rb = port_b;

  // flags register: latched only when the control word says the
  // operation is a real arithmetic step
  reg [3:0] flags;
  always @(posedge i_clk) begin
    if (i_rst)           flags <= 4'd0;
    else if (i_flags_we) flags <= {alu_z, alu_n, alu_c, alu_v};
  end
  assign {o_z, o_n, o_c, o_v} = flags;

  // OUT: the machine's window on the accumulator
  reg [7:0] out_reg;
  always @(posedge i_clk) begin
    if (i_rst)        out_reg <= 8'd0;
    else if (i_out_we) out_reg <= port_a;
  end
  assign o_out = out_reg;
endmodule
