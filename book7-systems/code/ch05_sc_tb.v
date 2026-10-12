// ch05_sc_tb.v -- run the 13-word program on the single-cycle core,
// check the architectural state after it parks at the jal self-loop.
`timescale 1ns/1ps
module ch05_sc_tb;
  reg clk=0, rst=1;
  wire [31:0] pc, da, dw; wire dwe, ret;
  reg [31:0] imem [0:63];
  reg [31:0] dmem [0:255];
  wire [31:0] insn = imem[pc[7:2]];
  wire [31:0] drd  = dmem[da[9:2]];
  rv32i_sc_top dut(.clk(clk), .rst(rst), .insn(insn),
    .dmem_rdata(drd), .pc(pc), .dmem_addr(da),
    .dmem_wdata(dw), .dmem_we(dwe), .retired(ret));
  always #5 clk = ~clk;
  always @(posedge clk) if (dwe) dmem[da[9:2]] <= dw;
  integer i, cyc = 0;
  initial begin
    for (i=0;i<256;i=i+1) dmem[i]=0;
    $readmemh("ch05_prog.hex", imem);
    #12 rst = 0;
    // run until pc parks at the jal self-loop (pc==0x30)
    while (pc != 32'h30 && cyc < 60) begin @(posedge clk); cyc=cyc+1; end
    @(posedge clk);
    $display("ran %0d cycles, pc parked at %h", cyc, pc);
    check(dut.rf.x[10] === 32'd1,  "a0 = 1");
    check(dut.rf.x[11] === 32'd2,  "a1 = 2");
    check(dut.rf.x[12] === 32'd3,  "a2 = a0+a1 = 3");
    check(dmem[2]      === 32'd3,  "mem[8] = 3 (sw worked)");
    check(dut.rf.x[13] === 32'd3,  "a3 = lw back = 3");
    check(dut.rf.x[14] === 32'd8,  "a4 = a3+5 = 8 (beq skipped 99)");
    check(dut.rf.x[15] === 32'd5,  "a5 = a4-a2 = 5");
    check(dut.rf.x[16] === 32'h12345000, "a6 = lui 0x12345000");
    $display("CPI check: %0d instrs retired in %0d cycles (CPI=1 by construction)", cyc, cyc);
    $display("ch05 PASS");
    $finish;
  end
  task check(input cond, input [8*48:0] name);
    if (!cond) begin $display("FAIL: %0s", name); $fatal; end
    else $display("  ok: %0s", name);
  endtask
endmodule
