// ch10_counter.v -- 4-bit counter with enable + terminal-count flag.
module counter(clk, en, q, tc);
  input clk, en;
  output reg [3:0] q = 0;
  output tc;
  assign tc = (q == 4'd15) & en;
  always @(posedge clk)
    if (en) q <= q + 1;
endmodule
