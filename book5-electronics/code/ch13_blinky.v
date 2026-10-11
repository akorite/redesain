// ch13_blinky.v -- the FPGA hello-world: one LED, one counter, one bit.
// 27 MHz clock -> 24-bit counter -> led = bit 23 -> ~3.2 s half-period.
module blinky(clk, led);
  input clk; output led;
  reg [23:0] cnt = 0;
  always @(posedge clk) cnt <= cnt + 1'b1;
  assign led = cnt[23];        // the slowest counter bit IS the blink
endmodule
