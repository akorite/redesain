// ch14_alu8.v -- the 8-bit ALU: compute all answers, then pick one.
// Contract: o_y/o_z/o_n/o_c/o_v combinational; flags defined in ch14 flag
// table. Op encoding is the book's fixed contract (ch15/ch16 keep it):
//   000 ADD   001 SUB   010 AND   011 OR
//   100 XOR   101 SHL   110 SHR   111 CMP
module alu8 (
  input  wire [7:0] i_a,
  input  wire [7:0] i_b,
  input  wire [2:0] i_op,
  output reg  [7:0] o_y,
  output reg        o_z,
  output reg        o_n,
  output reg        o_c,
  output reg        o_v
);
  localparam OP_ADD = 3'b000, OP_SUB = 3'b001, OP_AND = 3'b010,
             OP_OR  = 3'b011, OP_XOR = 3'b100, OP_SHL = 3'b101,
             OP_SHR = 3'b110, OP_CMP = 3'b111;

  // stage 1: every answer computed in parallel, always
  wire [8:0] add = {1'b0, i_a} + {1'b0, i_b};          // carry in bit 8
  wire [8:0] sub = {1'b0, i_a} + {1'b0, ~i_b} + 9'd1;  // a - b = a + ~b + 1
  wire [7:0] y_and = i_a & i_b;
  wire [7:0] y_or  = i_a | i_b;
  wire [7:0] y_xor = i_a ^ i_b;
  wire [7:0] y_shl = {i_a[6:0], 1'b0};
  wire [7:0] y_shr = {1'b0, i_a[7:1]};

  // per-path flag candidates: only the muxed ones reach the outputs
  wire c_add = add[8];
  wire v_add = (i_a[7] == i_b[7]) && (add[7] != i_a[7]);
  wire c_sub = sub[8];
  wire v_sub = (i_a[7] != i_b[7]) && (sub[7] != i_a[7]);

  // stage 2: the op field picks one result and one {C,V} pair
  always @(*) begin
    case (i_op)
      OP_ADD:         begin o_y = add[7:0]; o_c = c_add;  o_v = v_add; end
      OP_SUB, OP_CMP: begin o_y = sub[7:0]; o_c = c_sub;  o_v = v_sub; end
      OP_AND:         begin o_y = y_and;    o_c = 1'b0;   o_v = 1'b0;  end
      OP_OR:          begin o_y = y_or;     o_c = 1'b0;   o_v = 1'b0;  end
      OP_XOR:         begin o_y = y_xor;    o_c = 1'b0;   o_v = 1'b0;  end
      OP_SHL:         begin o_y = y_shl;    o_c = i_a[7]; o_v = 1'b0;  end
      OP_SHR:         begin o_y = y_shr;    o_c = i_a[0]; o_v = 1'b0;  end
      default:        begin o_y = 8'h00;    o_c = 1'b0;   o_v = 1'b0;  end
    endcase
    o_z = (o_y == 8'h00);   // zero flag: result is all zeros
    o_n = o_y[7];           // negative flag: sign bit of result
  end
endmodule
