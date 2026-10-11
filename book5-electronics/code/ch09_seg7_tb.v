// ch09_seg7_tb.v -- dump the decoder truth table.
`timescale 1ns/1ps
module seg7_tb;
  reg  [3:0] d;
  wire [6:0] seg;
  seg7 dut(.d(d), .seg(seg));
  integer i;
  initial begin
    $display(" d | abcdefg");
    $display("---+--------");
    for (i = 0; i < 16; i = i + 1) begin
      d = i[3:0]; #1;
      $display("%2d | %b", d, seg);
    end
    $finish;
  end
endmodule
