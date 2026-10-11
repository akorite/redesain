// ch11_counter2.v -- 4-bit counter, book style: params + named signals.
module counter2 #(parameter W = 4) (clk, rst, en, q, tc);
  input clk, rst, en;
  output reg [W-1:0] q;
  output wire tc;
  assign tc = en & (q == {W{1'b1}});      // terminal count
  always @(posedge clk) begin
    if (rst) q <= {W{1'b0}};
    else if (en) q <= q + 1'b1;
  end
endmodule
