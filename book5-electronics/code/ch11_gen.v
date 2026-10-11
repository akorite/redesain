// ch11_gen.v -- parameters and a generate peek: N DFFs from one name.
module regN #(parameter N = 4) (clk, d, q);
  input clk; input [N-1:0] d; output reg [N-1:0] q;
  genvar i;
  generate
    for (i = 0; i < N; i = i + 1) begin : ff
      always @(posedge clk) q[i] <= d[i];
    end
  endgenerate
endmodule
