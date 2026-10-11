// ch12_xcounter.v -- the "x forever" counter: no reset means x + 1 = x.
module cnt_norst(clk, q);
  input clk; output reg [3:0] q;
  always @(posedge clk) q <= q + 1'b1;   // q starts x -> stays x
endmodule
module cnt_rst(clk, rst, q);
  input clk, rst; output reg [3:0] q;
  always @(posedge clk)
    if (rst) q <= 4'd0; else q <= q + 1'b1;
endmodule
