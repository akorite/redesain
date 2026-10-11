// ch10_traffic_fsm.v -- 4-state traffic light, Moore style.
module traffic_fsm(clk, rst, ns, ew);
  input clk, rst;
  output reg [1:0] ns, ew;  // 2'b10 red, 2'b01 yellow, 2'b00 green
  localparam NS_G=2'd0, NS_Y=2'd1, EW_G=2'd2, EW_Y=2'd3;
  reg [1:0] state = NS_G, nxt;
  always @(*) begin
    case (state)
      NS_G: nxt = NS_Y;  NS_Y: nxt = EW_G;
      EW_G: nxt = EW_Y;  EW_Y: nxt = NS_G;
      default: nxt = NS_G;
    endcase
  end
  always @(posedge clk) state <= rst ? NS_G : nxt;
  always @(*) begin
    ns = (state==NS_G) ? 2'b00 : (state==NS_Y) ? 2'b01 : 2'b10;
    ew = (state==EW_G) ? 2'b00 : (state==EW_Y) ? 2'b01 : 2'b10;
  end
endmodule
