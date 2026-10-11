`timescale 1ns/1ps
module caselatch_tb;
  reg [1:0] op=0; reg [3:0] a=0,b=0;
  wire [3:0] yl, ys;
  alu4     ul(.op(op), .a(a), .b(b), .y(yl));
  alu4safe us(.op(op), .a(a), .b(b), .y(ys));
  initial $monitor("t=%2d op=%b a=%d b=%d | latched=%d safe=%d",
                   $time, op, a, b, yl, ys);
  initial begin
    a=7;b=2; op=0; #10;   // y = 9
    op=1;          #10;   // y = 5
    op=3;          #10;   // BUG: latched keeps 5; safe -> 0
    op=0;          #10;
    $finish;
  end
endmodule
