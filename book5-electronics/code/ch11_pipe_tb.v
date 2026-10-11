`timescale 1ns/1ps
module pipe_tb;
  reg clk=0, d=0; wire qnb, qb;
  pipe_nb un(.clk(clk), .d(d), .q(qnb));
  pipe_b  ub(.clk(clk), .d(d), .q(qb));
  always #5 clk = ~clk;
  initial $monitor("t=%2d clk=%b d=%b | q_nb=%b q_block=%b",
                   $time, clk, d, qnb, qb);
  initial begin
    #7 d=1; #35 d=0; #10 $finish;
  end
endmodule
