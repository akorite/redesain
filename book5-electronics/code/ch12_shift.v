// ch12_shift.v -- 8-bit shift register with a "clever" wrap-around bug.
module shift8(clk, en, sin, q);
  input clk, en, sin; output reg [7:0] q;
  always @(posedge clk)
    if (en) q <= {q[6:0], sin} ^ 8'b1;   // subtle bug: extra XOR bit0
endmodule
