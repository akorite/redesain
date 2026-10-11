`timescale 1ns/1ps
module traffic_tb;
  reg clk=0, rst=1;
  wire [1:0] ns, ew;
  traffic_fsm u(.clk(clk), .rst(rst), .ns(ns), .ew(ew));
  always #5 clk=~clk;
  always @(posedge clk)
    $display("t=%3d rst=%b state=%d | NS=%b EW=%b",
             $time, rst, u.state, ns, ew);
  initial begin
    #12 rst=0;  #50 $finish;
  end
endmodule
