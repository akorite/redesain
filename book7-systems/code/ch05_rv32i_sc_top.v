// ch05_rv32i_sc_top.v -- single-cycle RV32I core, the honest version:
// fetch, decode, execute, memory, writeback all in ONE clock edge.
`timescale 1ns/1ps
module rv32i_sc_top(
    input  wire        clk,
    input  wire        rst,
    input  wire [31:0] insn,       // from imem
    input  wire [31:0] dmem_rdata, // from dmem
    output wire [31:0] pc,
    output wire [31:0] dmem_addr,
    output wire [31:0] dmem_wdata,
    output wire        dmem_we,
    output wire        retired);   // pulses once per instruction
  reg [31:0] pc_r;
  assign pc = pc_r;
  assign retired = 1'b1;           // single cycle: every tick retires one

  // --- decode ---
  wire [3:0] aluop; wire alusrc, regwrite, memread, memwrite,
       branch, jump, lui_imm; wire [1:0] wbsel;
  rv32i_decode dec(.insn(insn), .aluop(aluop), .alusrc(alusrc),
    .regwrite(regwrite), .memread(memread), .memwrite(memwrite),
    .wbsel(wbsel), .branch(branch), .jump(jump), .lui_imm(lui_imm));

  // --- immediate generator ---
  wire [31:0] immI = {{20{insn[31]}}, insn[31:20]};
  wire [31:0] immS = {{20{insn[31]}}, insn[31:25], insn[11:7]};
  wire [31:0] immB = {{19{insn[31]}}, insn[31], insn[7],
                      insn[30:25], insn[11:8], 1'b0};
  wire [31:0] immU = {insn[31:12], 12'b0};
  wire [31:0] immJ = {{11{insn[31]}}, insn[31], insn[19:12],
                      insn[20], insn[30:21], 1'b0};
  wire [31:0] imm = lui_imm ? immU :
                    (insn[6:0]==7'b0100011) ? immS :
                    (insn[6:0]==7'b1100011) ? immB :
                    (insn[6:0]==7'b1101111) ? immJ : immI;

  // --- register file ---
  wire [31:0] rd1, rd2;
  reg  [31:0] wb;
  rv32i_regfile #(.BYPASS(0)) rf(.clk(clk), .we(regwrite),
    .ra1(insn[19:15]), .ra2(insn[24:20]), .wa(insn[11:7]),
    .wd(wb), .rd1(rd1), .rd2(rd2));

  // --- ALU ---
  wire [31:0] alu_b = alusrc ? imm : rd2;
  wire [31:0] alu_y; wire alu_zero;
  rv32i_alu alu(.a(rd1), .b(alu_b), .op(aluop), .y(alu_y), .zero(alu_zero));

  // --- memory ---
  assign dmem_addr  = alu_y;
  assign dmem_wdata = rd2;
  assign dmem_we    = memwrite;

  // --- writeback mux ---
  always @(*) begin
    case (wbsel)
      2'd1: wb = dmem_rdata;
      2'd2: wb = pc_r + 32'd4;
      default: wb = lui_imm ? immU : alu_y;
    endcase
  end

  // --- next pc ---
  wire brtake = branch & (insn[12] ? ~alu_zero : alu_zero); // bne=f3 001, beq=f3 000
  wire [31:0] pc_next = jump ? pc_r + imm :
                        brtake ? pc_r + immB : pc_r + 32'd4;
  always @(posedge clk)
    if (rst) pc_r <= 32'd0; else pc_r <= pc_next;
endmodule
