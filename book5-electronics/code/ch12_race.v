// ch12_race.v -- one DFF, used by both the good and bad testbenches.
module dff2(clk, d, q);
  input clk, d; output reg q;
  always @(posedge clk) q <= d;
endmodule
