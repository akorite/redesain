`timescale 1ns/1ps
module traffic2_tb;
  reg clk=0, rst=1; wire [1:0] ns, ew;
  traffic2 u(.clk(clk), .rst(rst), .ns(ns), .ew(ew));
  always #5 clk=~clk;
  initial begin
    $dumpfile("ch11_traffic2.vcd"); $dumpvars(0, traffic2_tb);
    $monitor("t=%2d rst=%b | st=%0d nx=%0d | ns=%b ew=%b",
             $time, rst, u.st, u.nx, ns, ew);
    #15 rst=0; #50 $finish;
  end
endmodule
