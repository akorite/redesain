// ch10_dff.v -- a transparent latch and a real D flip-flop, side by side.
module d_latch(en, d, q);
  input en, d;
  output reg q;
  always @(*) if (en) q = d;      // level-sensitive: follows d while en=1
endmodule

module d_ff(clk, d, q);
  input clk, d;
  output reg q;
  always @(posedge clk) q <= d;   // edge-sensitive: samples d only at clk rise
endmodule
