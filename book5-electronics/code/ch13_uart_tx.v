// ch13_uart_tx.v -- minimal UART transmitter, 27 MHz clk, 115200 baud.
// Frame: 1 start bit (0), 8 data bits LSB-first, 1 stop bit (1).
// TICKS = 27e6 / 115200 ~ 234 clocks per bit.
module uart_tx #(parameter TICKS = 234) (clk, start, data, tx, busy);
  input clk, start; input [7:0] data;
  output reg tx; output reg busy;
  reg [8:0] cnt;
  reg [3:0] bitn;
  reg [7:0] shreg;
  initial begin tx = 1; busy = 0; cnt = 0; bitn = 0; shreg = 0; end
  always @(posedge clk)
    if (!busy) begin
      tx <= 1;                          // idle line is HIGH
      if (start) begin busy <= 1; shreg <= data; cnt <= 0; bitn <= 0; tx <= 0; end
    end else begin
      if (cnt == TICKS - 1) begin
        cnt <= 0;
        if (bitn == 8) begin busy <= 0; tx <= 1; end   // stop bit
        else begin tx <= shreg[0]; shreg <= {1'b0, shreg[7:1]}; bitn <= bitn + 1; end
      end else cnt <= cnt + 1;
    end
endmodule
