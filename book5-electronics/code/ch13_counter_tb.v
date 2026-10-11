`timescale 1ns/1ps
module counter_tb;
  reg clk = 0, en = 0; wire [5:0] leds; wire tc;
  // sim twin: W=4, terminal every 16 clks
  counter_sim u(.clk(clk), .en(en), .leds(leds), .tc(tc));
  always #5 clk = ~clk;
  initial $monitor("t=%3d en=%b div=%0d leds=%b tc=%b",
                   $time, en, u.div, leds, tc);
  initial begin
    #12 en = 1; #200 en = 0; #40 $finish;
  end
endmodule
module counter_sim(clk, en, leds, tc);   // scaled twin for the sim
  input clk, en; output reg [5:0] leds = 0; output reg tc = 0;
  reg [3:0] div = 0;
  always @(posedge clk) begin
    tc <= 0;
    if (en)
      if (div == 4'd15) begin div <= 0; leds <= leds + 1'b1; tc <= 1; end
      else div <= div + 1'b1;
  end
endmodule
