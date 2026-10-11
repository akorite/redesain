`timescale 1ns/1ps
module counter_tb;
  reg clk = 0, en = 0;
  wire [3:0] q; wire tc;
  counter u(.clk(clk), .en(en), .q(q), .tc(tc));
  always #5 clk = ~clk;
  initial begin
    $monitor("t=%3d en=%b | q=%2d tc=%b", $time, en, q, tc);
    #12 en=1;
    #170 en=0;
    #20 $finish;
  end
endmodule
