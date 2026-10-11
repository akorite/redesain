`timescale 1ns/1ps
module gen_tb;
  reg clk=0; reg [7:0] d; wire [3:0] q4; wire [7:0] q8;
  regN #(4) r4(.clk(clk), .d(d[3:0]), .q(q4));
  regN #(8) r8(.clk(clk), .d(d),       .q(q8));
  always #5 clk=~clk;
  initial begin
    d=8'b10110100; #12;
    $display("t=%0d d=%b | q4=%b q8=%b", $time, d, q4, q8);
    d=8'b01101001; #12;
    $display("t=%0d d=%b | q4=%b q8=%b", $time, d, q4, q8);
    $finish;
  end
endmodule
