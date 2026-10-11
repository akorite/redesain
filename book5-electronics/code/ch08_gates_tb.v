// ch08_gates_tb.v -- behavioral gate truth printer
// First Verilog in the book: READ it, don't sweat the syntax yet.
// Run: iverilog -o gates_tb ch08_gates_tb.v && vvp gates_tb
`timescale 1ns/1ps

module gates_tb;
  reg  a, b;            // two inputs we will sweep
  wire y_and, y_or, y_xor, y_nand, y_nor, y_xnor;

  // The gates themselves, in "assign" form: each output follows its inputs.
  assign y_and  = a & b;
  assign y_or   = a | b;
  assign y_xor  = a ^ b;
  assign y_nand = ~(a & b);
  assign y_nor  = ~(a | b);
  assign y_xnor = ~(a ^ b);

  integer i;
  initial begin
    $display("a b | AND OR XOR NAND NOR XNOR");
    $display("----+---------------------------------");
    for (i = 0; i < 4; i = i + 1) begin
      {a, b} = i[1:0];            // 00, 01, 10, 11 in binary
      #1;                         // let signals settle one tick
      $display("%b %b |  %b   %b   %b    %b    %b     %b",
               a, b, y_and, y_or, y_xor, y_nand, y_nor, y_xnor);
    end
    $finish;
  end
endmodule
