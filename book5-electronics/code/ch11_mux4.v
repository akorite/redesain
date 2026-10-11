// ch11_mux4.v -- one 2:1 mux, four legal ways.
module mux_assign(sel, a, b, y);
  input sel, a, b; output y;
  assign y = sel ? b : a;                    // way 1: ternary
endmodule
module mux_bool(sel, a, b, y);
  input sel, a, b; output y;
  assign y = (~sel & a) | (sel & b);         // way 2: gates
endmodule
module mux_if(sel, a, b, y);
  input sel, a, b; output reg y;
  always @(*)                                // way 3: procedural if
    if (sel) y = b; else y = a;
endmodule
module mux_case(sel, a, b, y);
  input sel, a, b; output reg y;
  always @(*)                                // way 4: case
    case (sel)
      1'b0: y = a;
      default: y = b;
    endcase
endmodule
// wrong way 1: the missing else -> an inferred latch
module mux_latch(sel, a, b, y);
  input sel, a, b; output reg y;
  always @(*)
    if (sel == 1'b0) y = a;                  // sel=1: y keeps old value
endmodule
// wrong way 2: half sensitivity list -> stale output
module mux_stale(sel, a, b, y);
  input sel, a, b; output reg y;
  always @(a or b)                           // sel changes don't retrigger
    y = sel ? b : a;
endmodule
