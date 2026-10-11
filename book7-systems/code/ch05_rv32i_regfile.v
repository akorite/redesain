// ch05_rv32i_regfile.v -- 32x32 register file, x0 hardwired.
// Write-bypass: a WB write in the same cycle is visible to an ID
// read (the textbook "write first" ordering that removes the
// WB->ID boundary hazard -- found the hard way on this core).
`timescale 1ns/1ps
module rv32i_regfile(
    input  wire        clk,
    input  wire        we,
    input  wire [4:0]  ra1, ra2, wa,
    input  wire [31:0] wd,
    output wire [31:0] rd1, rd2);
  reg [31:0] x [0:31];
  assign rd1 = (ra1 == 5'd0) ? 32'd0 :
               (we && wa == ra1) ? wd : x[ra1];
  assign rd2 = (ra2 == 5'd0) ? 32'd0 :
               (we && wa == ra2) ? wd : x[ra2];
  always @(posedge clk)
    if (we && wa != 5'd0) x[wa] <= wd;
  initial begin : INIT
    integer i;
    for (i = 0; i < 32; i = i + 1) x[i] = 32'd0;
  end
endmodule
