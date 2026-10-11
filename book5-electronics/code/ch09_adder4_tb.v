// ch09_adder4_tb.v -- sweep a few sums, print as decimal.
`timescale 1ns/1ps
module adder4_tb;
  reg  [3:0] a, b;
  wire [3:0] sum;
  wire       cout;
  adder4 dut(.a(a), .b(b), .sum(sum), .cout(cout));
  integer i, j;
  initial begin
    $display(" a +  b = (cout,sum)");
    for (i = 0; i < 16; i = i + 1)
      for (j = 0; j < 16; j = j + 5) begin
        a = i; b = j; #1;
        $display("%2d + %2d = (%d,%2d)", a, b, cout, sum);
      end
    $finish;
  end
endmodule
