`timescale 1ns/1ps
// Decode the frame back: sample tx at mid-bit, reconstruct the byte.
module uart_tb;
  reg clk = 0, start = 0; reg [7:0] data = 8'h41;   // 'A'
  wire tx, busy;
  uart_tx #(.TICKS(8)) u(.clk(clk), .start(start), .data(data),
                         .tx(tx), .busy(busy));
  always #1 clk = ~clk;                 // fast sim clock
  integer i; reg [7:0] got = 0;
  initial $monitor("t=%3d busy=%b bit=%0d tx=%b", $time, busy, u.bitn, tx);
  initial #2 begin start = 1; #2 start = 0; end   // stimulus
  initial begin                          // decoder: arm BEFORE the edge
    @(negedge tx); #8;                   // mid start bit
    for (i = 0; i < 8; i = i + 1) begin
      #16 got[i] = tx;                   // mid-bit sample each period
    end
    #16 $display("decoded byte = %h (want 41), busy=%b", got, busy);
    if (got === 8'h41) $display("PASS: UART frame decoded");
    else $display("FAIL: got %h", got);
    $finish;
  end
endmodule
