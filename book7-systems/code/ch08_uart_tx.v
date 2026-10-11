// ch08_uart_tx.v -- UART transmitter: load byte -> serialise 8N1.
`timescale 1ns/1ps
module uart_tx(
    input  wire       clk, rst,
    input  wire       valid,      // pulse: send data
    input  wire [7:0] data,
    input  wire [15:0] div,       // clocks per bit
    output wire       tx,
    output reg        busy);
  reg [9:0]  sh;      // start + 8 data + stop
  reg [15:0] cnt;
  reg [3:0]  idx;
  assign tx = busy ? sh[0] : 1'b1;
  always @(posedge clk) begin
    if (rst) begin busy<=0; sh<=10'h3FF; cnt<=0; idx<=0; end
    else if (valid && !busy) begin
      sh <= {1'b1, data, 1'b0};   // stop, data, start
      busy <= 1; cnt <= 0; idx <= 0;
    end else if (busy) begin
      if (cnt == div-1) begin
        cnt <= 0; sh <= {1'b1, sh[9:1]};
        if (idx == 4'd9) busy <= 0; else idx <= idx + 1;
      end else cnt <= cnt + 1;
    end
  end
endmodule
