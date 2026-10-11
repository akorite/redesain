// ch05_rv32i_alu.v -- 32-bit ALU for the RV32I core.
// Adapted from Book 5 ch14's 8-bit ALU: same compute-all-then-mux shape,
// widened to 32 bits with the RV32I op set (Book 7 ISA mapping table).
`timescale 1ns/1ps
module rv32i_alu(
    input  wire [31:0] a,
    input  wire [31:0] b,
    input  wire [3:0]  op,
    output reg  [31:0] y,
    output wire        zero);
  // op: 0 add 1 sub 2 and 3 or 4 xor 5 sll 6 srl 7 slt 8 sltu
  always @(*) begin
    case (op)
      4'd0: y = a + b;
      4'd1: y = a - b;
      4'd2: y = a & b;
      4'd3: y = a | b;
      4'd4: y = a ^ b;
      4'd5: y = a << b[4:0];
      4'd6: y = a >> b[4:0];
      4'd7: y = ($signed(a) < $signed(b)) ? 32'd1 : 32'd0;
      4'd8: y = (a < b) ? 32'd1 : 32'd0;
      default: y = 32'hdeaddead;
    endcase
  end
  assign zero = (y == 32'd0);
endmodule
