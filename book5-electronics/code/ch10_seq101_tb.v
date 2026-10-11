`timescale 1ns/1ps
module seq101_tb;
  reg clk=0, x=0; wire hit;
  seq101 u(.clk(clk), .x(x), .hit(hit));
  always #5 clk=~clk;
  always @(posedge clk)
    $display("t=%3d x=%b state=%d hit=%b", $time, x, u.st, hit);
  reg [7:0] stream; integer i;
  initial begin
    stream = 8'b11010110;           // 101 occurs twice w/ overlap
    for (i=7; i>=0; i=i-1) begin x = stream[i]; #10; end
    $finish;
  end
endmodule
