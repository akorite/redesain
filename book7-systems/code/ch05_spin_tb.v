`timescale 1ns/1ps
module ch05_spin_tb;
  reg clk=0, rst=1;
  wire [31:0] pc, da, dw; wire dwe, ret;
  reg [31:0] imem [0:63];
  reg [31:0] dmem [0:255];
  wire [31:0] insn = imem[pc[7:2]];
  wire [31:0] drd  = dmem[da[9:2]];
  rv32i_sc_top dut(.clk(clk),.rst(rst),.insn(insn),.dmem_rdata(drd),
    .pc(pc),.dmem_addr(da),.dmem_wdata(dw),.dmem_we(dwe),.retired(ret));
  always #5 clk = ~clk;
  always @(posedge clk) if (dwe) dmem[da[9:2]] <= dw;
  integer cyc = 0;
  initial begin
    $readmemh("ch05_spin.hex", imem);
    #12 rst = 0;
    while (cyc < 2000) begin @(posedge clk); cyc=cyc+1; end
    $display("sim ran %0d cycles", cyc);
    $finish;
  end
endmodule
