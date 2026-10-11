`timescale 1ns/1ps
// BAD: stimulus changes in the same instant the clock edges.
module race_bad_tb;
  reg clk=0, d=0; wire q;
  dff2 u(.clk(clk), .d(d), .q(q));
  always #5 clk=~clk;
  always @(posedge clk) d = ~d;          // races the DFF's sample!
  initial $monitor("t=%2d clk=%b d=%b q=%b", $time, clk, d, q);
  initial #40 $finish;
endmodule
// GOOD: drive on the opposite edge (or #1 after) - no ambiguity.
module race_good_tb;
  reg clk=0, d=0; wire q;
  dff2 u(.clk(clk), .d(d), .q(q));
  always #5 clk=~clk;
  always @(negedge clk) d = ~d;          // settled half a cycle early
  initial $monitor("t=%2d clk=%b d=%b q=%b", $time, clk, d, q);
  initial #40 $finish;
endmodule
