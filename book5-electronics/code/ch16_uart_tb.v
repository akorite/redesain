// ch16_uart_tb.v -- decode the serial line like a real receiver and
// check the byte that crosses the wire. Real UART, simulated speed.
`timescale 1ns/1ps
module uart_tb;
  parameter CPB = 8;              // fast sim baud
  reg clk = 0, start = 0;
  reg [7:0] din = 0;
  wire tx, busy;
  always #5 clk = ~clk;
  uart_tx8 #(.CLKS_PER_BIT(CPB)) u
    (.i_clk(clk), .i_start(start), .i_data(din), .o_tx(tx), .o_busy(busy));

  integer i;
  reg [7:0] got;
  initial begin
    $dumpfile("ch16_uart.vcd"); $dumpvars(0, uart_tb);
    din = 8'h39;                   // '9' -- 0b00111001
    @(negedge clk); start = 1;
    @(negedge clk); start = 0;
    // decode: wait for start bit, sample mid-bit like a UART RX
    @(negedge tx);                 // start edge
    #(CPB*10/2);                   // mid-start
    for (i = 0; i < 8; i = i + 1) begin
      #(CPB*10);                   // one bit period later
      got[i] = tx;
    end
    if (got === 8'h39)
      $display("PASS: UART RX decoded 0x%02x on the wire", got);
    else
      $display("FAIL: decoded 0x%02x", got);
    #(CPB*10*2);
    if (!busy) $display("busy released after stop bit");
    $finish;
  end
endmodule
