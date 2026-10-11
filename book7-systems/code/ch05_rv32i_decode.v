// ch05_rv32i_decode.v -- control decoder: instruction bits -> control word.
// The truth table the chapter's figure draws row by row.
`timescale 1ns/1ps
module rv32i_decode(
    input  wire [31:0] insn,
    output reg  [3:0]  aluop,
    output reg         alusrc,   // 0=rs2, 1=imm
    output reg         regwrite,
    output reg         memread,
    output reg         memwrite,
    output reg  [1:0]  wbsel,    // 0=alu 1=mem 2=pc+4
    output reg         branch,
    output reg         jump,
    output reg         lui_imm); // imm is U-type
  wire [6:0] op  = insn[6:0];
  wire [2:0] f3  = insn[14:12];
  wire [6:0] f7  = insn[31:25];
  always @(*) begin
    // safe defaults: a NOP writes nothing, touches nothing
    aluop=4'd0; alusrc=0; regwrite=0; memread=0; memwrite=0;
    wbsel=2'd0; branch=0; jump=0; lui_imm=0;
    case (op)
      7'b0110011: begin                       // R-type
        regwrite=1;
        case ({f7[5],f3})
          4'b0_000: aluop=4'd0;               // add
          4'b1_000: aluop=4'd1;               // sub
          4'b0_111: aluop=4'd2;               // and
          4'b0_110: aluop=4'd3;               // or
          4'b0_100: aluop=4'd4;               // xor
          4'b0_001: aluop=4'd5;               // sll
          4'b0_101: aluop=4'd6;               // srl
          4'b0_010: aluop=4'd7;               // slt
          default:  aluop=4'd0;
        endcase
      end
      7'b0010011: begin                       // I-type ALU
        regwrite=1; alusrc=1;
        case (f3)
          3'b000: aluop=4'd0;                 // addi
          3'b111: aluop=4'd2;                 // andi
          3'b110: aluop=4'd3;                 // ori
          3'b100: aluop=4'd4;                 // xori
          3'b001: aluop=4'd5;                 // slli
          3'b101: aluop=4'd6;                 // srli
          3'b010: aluop=4'd7;                 // slti
          default: aluop=4'd0;
        endcase
      end
      7'b0000011: begin                       // lw
        regwrite=1; alusrc=1; memread=1; wbsel=2'd1; aluop=4'd0;
      end
      7'b0100011: begin                       // sw
        alusrc=1; memwrite=1; aluop=4'd0;
      end
      7'b1100011: begin                       // beq (bne uses f3 too)
        branch=1; aluop=4'd1;                 // sub for compare
      end
      7'b0110111: begin                       // lui
        regwrite=1; alusrc=1; lui_imm=1;
      end
      7'b1101111: begin                       // jal
        regwrite=1; jump=1; wbsel=2'd2;
      end
      default: ;
    endcase
  end
endmodule
