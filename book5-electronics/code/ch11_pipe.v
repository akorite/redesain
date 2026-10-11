// ch11_pipe.v -- a 2-flop pipeline, done right and done wrong.
module pipe_nb(clk, d, q);              // correct: nonblocking
  input clk, d; output reg q; reg q1;
  always @(posedge clk) begin
    q1 <= d;  q <= q1;
  end
endmodule
module pipe_b(clk, d, q);               // wrong: blocking
  input clk, d; output reg q; reg q1;
  always @(posedge clk) begin
    q1 = d;   q = q1;
  end
endmodule
