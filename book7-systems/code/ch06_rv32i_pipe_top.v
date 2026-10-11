// ch06_rv32i_pipe_top.v -- 5-stage pipeline, NAIVE on purpose:
// no forwarding, no stalls, no flush -- ch06's honest broken machine.
`timescale 1ns/1ps
module rv32i_pipe_top(
    input  wire        clk,
    input  wire        rst,
    input  wire [31:0] insn_f,        // from imem at pc_f
    input  wire [31:0] dmem_rdata,
    output wire [31:0] pc_f,
    output wire [31:0] dmem_addr,
    output wire [31:0] dmem_wdata,
    output wire        dmem_we,
    output wire        retired);      // WB-stage write pulse
  // ---- IF ----
  reg [31:0] pc;
  assign pc_f = pc;
  wire [31:0] pc4 = pc + 32'd4;
  // ---- IF/ID pipeline register ----
  reg [31:0] ifid_insn, ifid_pc4;
  always @(posedge clk) begin
    ifid_insn <= insn_f;
    ifid_pc4  <= pc4;
  end
  // ---- ID ----
  wire [3:0] aluop; wire alusrc, regwrite, memread, memwrite,
       branch, jump, lui_imm; wire [1:0] wbsel;
  rv32i_decode dec(.insn(ifid_insn), .aluop(aluop), .alusrc(alusrc),
    .regwrite(regwrite), .memread(memread), .memwrite(memwrite),
    .wbsel(wbsel), .branch(branch), .jump(jump), .lui_imm(lui_imm));
  wire [31:0] immI = {{20{ifid_insn[31]}}, ifid_insn[31:20]};
  wire [31:0] immS = {{20{ifid_insn[31]}}, ifid_insn[31:25],
                      ifid_insn[11:7]};
  wire [31:0] immB = {{19{ifid_insn[31]}}, ifid_insn[31], ifid_insn[7],
                      ifid_insn[30:25], ifid_insn[11:8], 1'b0};
  wire [31:0] immU = {ifid_insn[31:12], 12'b0};
  wire [31:0] immJ = {{11{ifid_insn[31]}}, ifid_insn[31],
                      ifid_insn[19:12], ifid_insn[20],
                      ifid_insn[30:21], 1'b0};
  wire [31:0] imm = lui_imm ? immU :
                    (ifid_insn[6:0]==7'b0100011) ? immS :
                    (ifid_insn[6:0]==7'b1100011) ? immB :
                    (ifid_insn[6:0]==7'b1101111) ? immJ : immI;
  wire [31:0] rd1, rd2, wbdata;
  wire [4:0]  wbwa;  wire wbwe;
  rv32i_regfile rf(.clk(clk), .we(wbwe),
    .ra1(ifid_insn[19:15]), .ra2(ifid_insn[24:20]), .wa(wbwa),
    .wd(wbdata), .rd1(rd1), .rd2(rd2));
  // ---- ID/EX pipeline register ----
  reg [31:0] idex_rd1, idex_rd2, idex_imm, idex_pc4;
  reg [4:0]  idex_rd;
  reg [3:0]  idex_aluop;
  reg        idex_alusrc, idex_regwrite, idex_memread, idex_memwrite,
             idex_branch, idex_jump, idex_lui;
  reg [1:0]  idex_wbsel;
  always @(posedge clk) begin
    idex_rd1<=rd1; idex_rd2<=rd2; idex_imm<=imm; idex_pc4<=ifid_pc4;
    idex_rd<=ifid_insn[11:7]; idex_aluop<=aluop; idex_alusrc<=alusrc;
    idex_regwrite<=regwrite; idex_memread<=memread;
    idex_memwrite<=memwrite; idex_branch<=branch; idex_jump<=jump;
    idex_lui<=lui_imm; idex_wbsel<=wbsel;
  end
  // ---- EX ----
  wire [31:0] alu_b = idex_alusrc ? idex_imm : idex_rd2;
  wire [31:0] alu_y; wire alu_zero;
  rv32i_alu alu(.a(idex_rd1), .b(alu_b), .op(idex_aluop),
                .y(alu_y), .zero(alu_zero));
  // naive: branch resolved in EX, no flush -- wrong-path insns run
  // ---- EX/MEM pipeline register ----
  reg [31:0] exmem_y, exmem_rd2, exmem_pc4;
  reg [4:0]  exmem_rd;
  reg        exmem_regwrite, exmem_memread, exmem_memwrite;
  reg [1:0]  exmem_wbsel;
  always @(posedge clk) begin
    exmem_y<=alu_y; exmem_rd2<=idex_rd2; exmem_pc4<=idex_pc4;
    exmem_rd<=idex_rd; exmem_regwrite<=idex_regwrite;
    exmem_memread<=idex_memread; exmem_memwrite<=idex_memwrite;
    exmem_wbsel<=idex_wbsel;
  end
  // ---- MEM ----
  assign dmem_addr  = exmem_y;
  assign dmem_wdata = exmem_rd2;
  assign dmem_we    = exmem_memwrite;
  // ---- MEM/WB pipeline register ----
  reg [31:0] memwb_y, memwb_mem, memwb_pc4;
  reg [4:0]  memwb_rd;
  reg        memwb_regwrite;
  reg [1:0]  memwb_wbsel;
  always @(posedge clk) begin
    memwb_y<=exmem_y; memwb_mem<=dmem_rdata; memwb_pc4<=exmem_pc4;
    memwb_rd<=exmem_rd; memwb_regwrite<=exmem_regwrite;
    memwb_wbsel<=exmem_wbsel;
  end
  // ---- WB ----
  assign wbdata = memwb_wbsel==2'd1 ? memwb_mem :
                  memwb_wbsel==2'd2 ? memwb_pc4 : memwb_y;
  assign wbwa   = memwb_rd;
  assign wbwe   = memwb_regwrite;
  assign retired = wbwe;
  // ---- next pc: sequential only for the naive core ----
  always @(posedge clk)
    if (rst) pc <= 32'd0; else pc <= pc4;
endmodule
