// ch10_mm.v -- Moore vs Mealy on the SAME "saw a 1" task.
module det_moore(clk, x, y);
  input clk, x; output reg y;
  localparam WAIT=0, GOT=1;
  reg st = WAIT;
  always @(posedge clk) st <= x ? GOT : WAIT;
  always @(*) y = (st == GOT);      // out asserts the cycle AFTER the sample
endmodule
module det_mealy(clk, x, y);
  input clk, x; output reg y;
  reg prev = 0;
  always @(posedge clk) prev <= x;
  always @(*) y = x & ~prev;        // same-cycle on the rise
endmodule
