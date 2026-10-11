`timescale 1ns/1ps
module mm_tb;
  reg clk=0, x=0;
  wire ymo, yme;
  det_moore dm(.clk(clk), .x(x), .y(ymo));
  det_mealy de(.clk(clk), .x(x), .y(yme));
  always #5 clk=~clk;
  always @(posedge clk) $display("t=%3d x=%b | mealy=%b moore=%b",
                                 $time, x, yme, ymo);
  initial begin
    #12 x=1; #20 x=0; #15 $finish;
  end
endmodule
