`timescale 1ns/1ps
// ch14_alu8_exh_tb.v -- exhaustive proof for the two arithmetic paths.
// Directed vectors cover the cases we *thought* of; this bench sweeps all
// 65536 (a,b) pairs for ADD and SUB against an independent golden model
// written from the flag table, not from the DUT.
module alu8_exh_tb;
  reg  [7:0] a, b;
  reg  [2:0] op;
  wire [7:0] y;
  wire       z, n, c, v;

  alu8 u(.i_a(a), .i_b(b), .i_op(op), .o_y(y),
         .o_z(z), .o_n(n), .o_c(c), .o_v(v));

  integer errors = 0, checks = 0;
  reg [8:0] full;
  reg gv;

  task sweep(input [2:0] the_op);
    integer ia, ib;
    begin
      for (ia = 0; ia < 256; ia = ia + 1)
        for (ib = 0; ib < 256; ib = ib + 1) begin
          a = ia[7:0]; b = ib[7:0]; op = the_op; #1;
          // golden model: flag-table semantics, not the DUT's structure
          if (the_op == 3'b000) begin
            full = a + b;
            gv = (a[7] == b[7]) && (full[7] != a[7]);
          end else begin
            // NOT a + ~b + 9'd1: ~b is complemented at the 9-bit
            // context width (~8'h01 -> 9'h1FE, not 9'h0FE) -- the
            // explicit concat keeps the complement at 8 bits.
            full = a + {1'b0, ~b} + 9'd1;
            gv = (a[7] != b[7]) && (full[7] != a[7]);
          end
          checks = checks + 1;
          if ({y, z, n, c, v} !== {full[7:0], (full[7:0] == 8'h00),
                                   full[7], full[8], gv}) begin
            errors = errors + 1;
            if (errors < 6)
              $display("MISMATCH op=%b a=%h b=%h got y=%h z=%b n=%b c=%b v=%b want y=%h z=%b n=%b c=%b v=%b",
                       the_op, a, b, y, z, n, c, v,
                       full[7:0], (full[7:0] == 8'h00), full[7], full[8], gv);
          end
        end
    end
  endtask

  initial begin
    sweep(3'b000);   // ADD: all 65536 operand pairs
    $display("ADD done: %0d checks, %0d errors", checks, errors);
    sweep(3'b001);   // SUB: all 65536 operand pairs
    if (errors == 0)
      $display("PASS: %0d exhaustive vectors clean", checks);
    else
      $display("FAIL: %0d mismatches in %0d vectors", errors, checks);
    $finish;
  end
endmodule
