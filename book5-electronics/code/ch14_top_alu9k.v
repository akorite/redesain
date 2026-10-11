// ch14_top_alu9k.v -- board wrapper: DIP switches drive the operands,
// the six onboard LEDs show result and flags. Fully combinational:
// this demo has no clock domain at all.
//
// Display (6 LEDs, active-low on this board):
//   S1 released : led[5:0] = y[5:0]          (low 6 bits of result)
//   S1 pressed  : led[5:0] = {Z,N,C,V,y[7:6]} (all flags + top 2 bits)
// Read both ways and you have the whole answer.
module top_alu9k (
  input  wire [7:0] i_a,      // DIP bank on J6 header (pins 79-86)
  input  wire [7:0] i_b,      // DIP bank on J5 header (pins 25-30,33,34)
  input  wire [2:0] i_op,     // DIP-3 on J6 header (pins 76,77,48)
  input  wire       i_mode_n, // onboard button S1 (pin 3, active-low)
  output wire [5:0] o_led     // onboard LEDs (pins 10,11,13,14,15,16)
);
  wire [7:0] y;
  wire       z, n, c, v;

  alu8 u(.i_a(i_a), .i_b(i_b), .i_op(i_op),
         .o_y(y), .o_z(z), .o_n(n), .o_c(c), .o_v(v));

  wire [5:0] disp = i_mode_n ? y[5:0] : {z, n, c, v, y[7:6]};
  assign o_led = ~disp;        // LEDs are wired active-low on this board
endmodule
