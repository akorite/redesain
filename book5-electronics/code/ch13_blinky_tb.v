`timescale 1ns/1ps
// Shrink the counter for simulation: same structure, 4-bit top.
module blinky_tb;
  reg clk = 0; wire led;
  blinky_sim u(.clk(clk), .led(led));
  always #5 clk = ~clk;
  initial $monitor("t=%3d cnt=%b led=%b", $time, u.cnt[3:0], led);
  initial #170 $finish;
endmodule
// test-only twin: led on bit 3, toggles every 8 clks (80 ns)
module blinky_sim(clk, led);
  input clk; output led;
  reg [23:0] cnt = 0;
  always @(posedge clk) cnt <= cnt + 1'b1;
  assign led = cnt[3];
endmodule
