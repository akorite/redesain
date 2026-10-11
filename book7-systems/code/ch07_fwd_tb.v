// ch07_fwd_tb.v -- the same dependent pair ch06 broke, now forwarded.
`timescale 1ns/1ps
module ch07_fwd_tb;
  reg clk=0, rst=1;
  wire [31:0] pc, da, dw; wire dwe, ret, st;
  reg [31:0] imem [0:63];
  reg [31:0] dmem [0:255];
  wire [31:0] insn = imem[pc[7:2]];
  wire [31:0] drd  = dmem[da[9:2]];
  rv32i_fwd_top dut(.clk(clk),.rst(rst),.insn_f(insn),
    .dmem_rdata(drd),.pc_f(pc),.dmem_addr(da),.dmem_wdata(dw),
    .dmem_we(dwe),.retired(ret),.stalled(st));
  always #5 clk = ~clk;
  always @(posedge clk) if (dwe) dmem[da[9:2]] <= dw;
  integer i, cyc, stalls=0, retires=0;
  initial begin
    for (i=0;i<256;i=i+1) dmem[i]=0;
    // (1) ALU dependent pair: forwarding, no stall
    imem[0]=32'h00500513; // addi a0,zero,5
    imem[1]=32'h00350593; // addi a1,a0,3
    // (2) load-use: lw a2,0(zero); addi a3,a2,1  -> 1 bubble
    imem[2]=32'h00002603; // lw a2,0(zero)
    imem[3]=32'h00160693; // addi a3,a2,1
    // (3) dependent store: sw a3,4(zero)
    imem[4]=32'h00d02223; // sw a3,4(zero)
    imem[5]=32'h00000013; // nop
    dmem[0]=32'd41;
    #12 rst=0; cyc=0;
    while (cyc<40) begin
      @(posedge clk); cyc=cyc+1;
      if (st) stalls=stalls+1;
      if (ret) retires=retires+1;
    end
    $display("fwd results:");
    $display("  a0=%0d (5) a1=%0d (8) -- forwarding fixed ch06's 3",
             dut.rf.x[10], dut.rf.x[11]);
    $display("  a2=%0d (41) a3=%0d (42) -- load-use stalled once",
             dut.rf.x[12], dut.rf.x[13]);
    $display("  dmem[1]=%0d (42) -- dependent store forwarded",
             dmem[1]);
    $display("measured: %0d stalls, %0d WB-writes in %0d cycles",
             stalls, retires, cyc);
    check(dut.rf.x[10]==5 && dut.rf.x[11]==8, "ALU forward");
    check(dut.rf.x[12]==41 && dut.rf.x[13]==42, "load-use stall");
    check(dmem[1]==42, "store forward");
    check(stalls==1, "exactly 1 bubble");
    $display("ch07 PASS");
    $finish;
  end
  task check(input cond, input [8*24:0] name);
    if (!cond) begin $display("FAIL: %0s", name); $fatal; end
    else $display("  ok: %0s", name);
  endtask
endmodule
