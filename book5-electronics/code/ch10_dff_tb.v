// ch10_dff_tb.v -- the classic bug: latch follows glitches, FF doesn't.
`timescale 1ns/1ps
module dff_tb;
  reg en = 0, clk = 0, d = 0;
  wire q_latch, q_ff;
  d_latch u1(.en(en), .d(d), .q(q_latch));
  d_ff    u2(.clk(clk), .d(d), .q(q_ff));
  always #5 clk = ~clk;
  initial begin
    $dumpfile("ch10_dff.vcd");
    $dumpvars(0, dff_tb);
    $monitor("t=%3d en=%b clk=%b d=%b | latch=%b ff=%b",
             $time, en, clk, d, q_latch, q_ff);
    // data toggles mid-cycle; en is high for one long window
    #3  d=1;
    #5  en=1;        // latch opens at t=8
    #4  d=0;         // glitch low while en high
    #4  d=1;         // back high, still open
    #5  en=0;        // latch closes at t=21
    #20 $finish;
  end
endmodule
