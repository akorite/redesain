// ch12_caselatch.v -- case without default -> latch again (the polite way)
module alu4(op, a, b, y);
  input [1:0] op; input [3:0] a, b; output reg [3:0] y;
  always @(*) case (op)
    2'b00: y = a + b;
    2'b01: y = a - b;
    2'b10: y = a & b;
    // 2'b11 silently missing -> y holds old value
  endcase
endmodule
module alu4safe(op, a, b, y);
  input [1:0] op; input [3:0] a, b; output reg [3:0] y;
  always @(*) case (op)
    2'b00: y = a + b;
    2'b01: y = a - b;
    2'b10: y = a & b;
    default: y = 4'b0000;    // explicit, no latch
  endcase
endmodule
