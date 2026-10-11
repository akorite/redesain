// ch13_counter.v -- up-counter to a bus of LEDs, with enable + terminal count.
module counter6 #(parameter W = 27, parameter TOP = 13500000) (
  input clk, input en,
  output reg [5:0] leds = 0, output reg tc = 0);
  reg [W-1:0] div = 0;
  always @(posedge clk) begin
    tc <= 0;
    if (en) begin
      if (div == TOP) begin              // 27 MHz / (TOP+1) ticks per step
        div <= 0; leds <= leds + 1'b1; tc <= 1;
      end else div <= div + 1'b1;
    end
  end
endmodule
