// ch08_rv32i_soc_top.v -- forwarded core + minimal trap CSRs +
// MMIO UART. ecall -> mtvec (fixed 0x40); mret -> mepc.
`timescale 1ns/1ps
module rv32i_soc_top(
    input  wire        clk, rst,
    input  wire [31:0] insn_f,
    input  wire [31:0] dmem_rdata,
    output wire [31:0] pc_f,
    output wire [31:0] dmem_addr,
    output wire [31:0] dmem_wdata,
    output wire        dmem_we,
    output wire        uart_req,       // MMIO store to UART base
    output wire        retired);
  reg [31:0] pc;
  assign pc_f = pc;
  wire [31:0] pc4 = pc + 32'd4;
  reg [31:0] mepc; reg [4:0] mcause;
  localparam MTVEC = 32'h80;
  reg [31:0] ifid_insn, ifid_pc4;
  wire stall, flush;
  always @(posedge clk) begin
    if (rst) begin ifid_insn <= 32'h00000013; ifid_pc4 <= 0; end
    else if (!stall) begin
      ifid_insn <= flush ? 32'h13 : insn_f;
      ifid_pc4  <= pc4;
    end
  end
  wire [3:0] aluop; wire alusrc, regwrite, memread, memwrite,
       branch, jump, lui_imm; wire [1:0] wbsel;
  rv32i_decode dec(.insn(ifid_insn), .aluop(aluop), .alusrc(alusrc),
    .regwrite(regwrite), .memread(memread), .memwrite(memwrite),
    .wbsel(wbsel), .branch(branch), .jump(jump), .lui_imm(lui_imm));
  wire is_ecall = (ifid_insn == 32'h00000073);
  wire is_mret  = (ifid_insn == 32'h30200073);
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
  wire [4:0]  wbwa; wire wbwe;
  rv32i_regfile rf(.clk(clk), .we(wbwe),
    .ra1(ifid_insn[19:15]), .ra2(ifid_insn[24:20]), .wa(wbwa),
    .wd(wbdata), .rd1(rd1), .rd2(rd2));
  reg [31:0] idex_rd1, idex_rd2, idex_imm, idex_pc4, idex_pc;
  reg [4:0]  idex_rd, idex_rs1, idex_rs2;
  reg [3:0]  idex_aluop;
  reg        idex_alusrc, idex_regwrite, idex_memread, idex_memwrite,
             idex_branch, idex_jump, idex_lui, idex_f30,
             idex_ecall, idex_mret;
  reg [1:0]  idex_wbsel;
  assign stall = idex_memread &&
                 ((idex_rd == ifid_insn[19:15] && ifid_insn[19:15]!=0) ||
                  (idex_rd == ifid_insn[24:20] && ifid_insn[24:20]!=0));
  always @(posedge clk) begin
    if (rst || stall || flush) begin
      idex_regwrite<=0; idex_memread<=0; idex_memwrite<=0;
      idex_branch<=0; idex_jump<=0; idex_f30<=0; idex_memread<=0;
      idex_rd<=0; idex_rs1<=0; idex_rs2<=0; idex_ecall<=0; idex_mret<=0;
    end else begin
      idex_rd1<=rd1; idex_rd2<=rd2; idex_imm<=imm; idex_pc4<=ifid_pc4;
      idex_pc<=ifid_pc4-4;
      idex_rd<=ifid_insn[11:7]; idex_rs1<=ifid_insn[19:15];
      idex_rs2<=ifid_insn[24:20];
      idex_aluop<=aluop; idex_alusrc<=alusrc;
      idex_regwrite<=regwrite; idex_memread<=memread;
      idex_memwrite<=memwrite; idex_branch<=branch; idex_jump<=jump;
      idex_lui<=lui_imm; idex_wbsel<=wbsel; idex_f30<=ifid_insn[12];
      idex_ecall<=is_ecall; idex_mret<=is_mret;
    end
  end
  reg [31:0] exmem_y, exmem_rd2, exmem_pc4;
  reg [4:0]  exmem_rd;
  reg        exmem_regwrite, exmem_memread, exmem_memwrite;
  reg [1:0]  exmem_wbsel;
  reg [31:0] memwb_y, memwb_mem, memwb_pc4;
  reg [4:0]  memwb_rd;
  reg        memwb_regwrite;
  reg [1:0]  memwb_wbsel;
  wire [31:0] exmem_wb = (exmem_wbsel==2'd2) ? exmem_pc4 :
                         (exmem_wbsel==2'd1) ? dmem_rdata : exmem_y;
  wire [31:0] fwdA = (exmem_regwrite && exmem_rd!=0 && exmem_rd==idex_rs1)
                     ? exmem_wb :
                     (memwb_regwrite && memwb_rd!=0 && memwb_rd==idex_rs1)
                     ? wbdata : idex_rd1;
  wire [31:0] fwdB = (exmem_regwrite && exmem_rd!=0 && exmem_rd==idex_rs2)
                     ? exmem_wb :
                     (memwb_regwrite && memwb_rd!=0 && memwb_rd==idex_rs2)
                     ? wbdata : idex_rd2;
  wire [31:0] alu_b = idex_alusrc ? idex_imm : fwdB;
  wire [31:0] alu_y; wire alu_zero;
  rv32i_alu alu(.a(fwdA), .b(alu_b), .op(idex_aluop),
                .y(alu_y), .zero(alu_zero));
  wire brtake = idex_branch & (idex_f30 ? ~alu_zero : alu_zero);
  assign flush = brtake | idex_jump | idex_ecall | idex_mret;
  wire [31:0] pc_tgt = idex_pc4 - 32'd4 + idex_imm;
  always @(posedge clk) begin
    if (rst) begin exmem_regwrite<=0; exmem_memread<=0;
                  exmem_memwrite<=0; exmem_rd<=0; end
    exmem_y<=alu_y; exmem_rd2<=fwdB; exmem_pc4<=idex_pc4;
    exmem_rd<=idex_rd; exmem_regwrite<=idex_regwrite;
    exmem_memread<=idex_memread; exmem_memwrite<=idex_memwrite;
    exmem_wbsel<=idex_wbsel;
  end
  assign dmem_addr  = exmem_y;
  assign dmem_wdata = exmem_rd2;
  assign dmem_we    = exmem_memwrite;
  assign uart_req   = exmem_memwrite & (exmem_y == 32'h10000000);
  always @(posedge clk) begin
    if (rst) begin memwb_regwrite<=0; memwb_rd<=0; end
    memwb_y<=exmem_y; memwb_mem<=dmem_rdata; memwb_pc4<=exmem_pc4;
    memwb_rd<=exmem_rd; memwb_regwrite<=exmem_regwrite;
    memwb_wbsel<=exmem_wbsel;
  end
  assign wbdata = memwb_wbsel==2'd1 ? memwb_mem :
                  memwb_wbsel==2'd2 ? memwb_pc4 : memwb_y;
  assign wbwa   = memwb_rd;
  assign wbwe   = memwb_regwrite;
  assign retired = wbwe;
  // trap machinery: ecall in EX -> mepc=insn pc, pc=MTVEC
  // mret in EX -> pc=mepc
  always @(posedge clk) begin
    if (rst) begin pc <= 0; mepc <= 0; mcause <= 0; end
    else begin
      if (idex_ecall) mepc <= idex_pc;
      if (stall) pc <= pc;
      else if (idex_ecall) pc <= MTVEC;
      else if (idex_mret) pc <= mepc + 4;
      else if (brtake | idex_jump) pc <= pc_tgt;
      else pc <= pc4;
    end
  end
endmodule
