`timescale 1ns/1ps
module xcounter_tb;
  reg clk=0, rst=1;
  wire [3:0] qx, qr;
  cnt_norst u1(.clk(clk), .q(qx));
  cnt_rst   u2(.clk(clk), .rst(rst), .q(qr));
  always #5 clk=~clk;
  initial $monitor("t=%2d | no-rst q=%b | with-rst q=%b", $time, qx, qr);
  initial begin
    #25 rst=0;        // release after 2.5 edges
    #35 $finish;
  end
endmodule
