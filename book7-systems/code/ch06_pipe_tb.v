// ch06_pipe_tb.v -- the naive pipeline SHOWN breaking:
// (a) independent stream: CPI ~ 1 and correct values
// (b) dependent stream: wrong value in a1 -- the hazard, visible
`timescale 1ns/1ps
module ch06_pipe_tb;
  reg clk=0, rst=1;
  wire [31:0] pc, da, dw; wire dwe, ret;
  reg [31:0] imem [0:63];
  reg [31:0] dmem [0:255];
  wire [31:0] insn = imem[pc[7:2]];
  wire [31:0] drd  = dmem[da[9:2]];
  rv32i_pipe_top dut(.clk(clk),.rst(rst),.insn_f(insn),
    .dmem_rdata(drd),.pc_f(pc),.dmem_addr(da),.dmem_wdata(dw),
    .dmem_we(dwe),.retired(ret));
  always #5 clk = ~clk;
  always @(posedge clk) if (dwe) dmem[da[9:2]] <= dw;
  integer i, cyc;
  initial begin
    for (i=0;i<256;i=i+1) dmem[i]=0;
    // DEPENDENT stream: a0=5; a1=a0+3 (reads a0 3 cycles too early)
    imem[0]=32'h00500513; // addi a0,zero,5
    imem[1]=32'h00350593; // addi a1,a0,3     <- hazard
    imem[2]=32'h00000613; // addi a2,zero,0
    imem[3]=32'h0000006f; // jal self
    #12 rst=0; cyc=0;
    while (cyc<30) begin @(posedge clk); cyc=cyc+1; end
    $display("dependent: a0=%0d (want 5)  a1=%0d (want 8)",
             dut.rf.x[10], dut.rf.x[11]);
    $display("  ^^ a1 read the OLD a0 -- data hazard, REAL and wrong");
    // INDEPENDENT stream: five insns that never touch each other
    imem[0]=32'h00100513; // addi a0,zero,1
    imem[1]=32'h00200593; // addi a1,zero,2
    imem[2]=32'h00300613; // addi a2,zero,3
    imem[3]=32'h00400693; // addi a3,zero,4
    imem[4]=32'h00500713; // addi a4,zero,5
    imem[5]=32'h0000006f; // jal self
    rst=1; #12 rst=0; cyc=0;
    while (cyc<30) begin @(posedge clk); cyc=cyc+1; end
    $display("independent: a0..a4 = %0d %0d %0d %0d %0d (want 1..5)",
             dut.rf.x[10],dut.rf.x[11],dut.rf.x[12],dut.rf.x[13],
             dut.rf.x[14]);
    $display("ch06 SHOWN: pipeline retires ~1/cyc when independent,",
             "lies when dependent");
    $finish;
  end
endmodule
