// ch16_uart_tx8.v -- 8N1 UART transmitter, parameterised baud.
// i_start pulses one cycle with i_data valid; o_busy stays high for
// the whole frame. The board top wires cpu8.o_out_we to i_start.
module uart_tx8 #(parameter CLKS_PER_BIT = 234) (  // 27MHz/115200
  input  wire       i_clk,
  input  wire       i_start,
  input  wire [7:0] i_data,
  output reg        o_tx,
  output reg        o_busy
);
  localparam IDLE=0, START=1, DATA=2, STOP=3;
  reg [1:0]  state = IDLE;
  reg [15:0] cnt = 0;
  reg [2:0]  bitn = 0;
  reg [7:0]  sh = 0;
  always @(posedge i_clk) begin
    case (state)
      IDLE: begin
        o_tx <= 1'b1; o_busy <= 0;
        if (i_start) begin
          state <= START; sh <= i_data; o_busy <= 1; cnt <= 0;
        end
      end
      START: begin
        o_tx <= 1'b0;
        if (cnt == CLKS_PER_BIT-1) begin
          cnt <= 0; state <= DATA; bitn <= 0;
        end else cnt <= cnt + 1;
      end
      DATA: begin
        o_tx <= sh[0];
        if (cnt == CLKS_PER_BIT-1) begin
          cnt <= 0; sh <= sh >> 1;
          if (bitn == 7) state <= STOP; else bitn <= bitn + 1;
        end else cnt <= cnt + 1;
      end
      STOP: begin
        o_tx <= 1'b1;
        if (cnt == CLKS_PER_BIT-1) begin
          cnt <= 0; state <= IDLE;
        end else cnt <= cnt + 1;
      end
    endcase
  end
endmodule
