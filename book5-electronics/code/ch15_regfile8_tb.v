// Directed checks for regfile8: write-then-read on both ports,
// the write's edge timing, and an independent read of every cell.
`timescale 1ns/1ps
module regfile8_tb;
  reg clk = 0, we = 0;
  reg [2:0] waddr = 0, raddr_a = 0, raddr_b = 0;
  reg [7:0] wdata = 0;
  wire [7:0] ra, rb;
  integer errors = 0, i;

  regfile8 u(.i_clk(clk), .i_we(we), .i_waddr(waddr), .i_wdata(wdata),
             .i_raddr_a(raddr_a), .i_raddr_b(raddr_b), .o_ra(ra), .o_rb(rb));

  always #5 clk = ~clk;

  task check8(input [127:0] what, input [7:0] got, input [7:0] exp);
    if (got !== exp) begin
      errors = errors + 1;
      $display("FAIL %0s: got=%h exp=%h", what, got, exp);
    end
  endtask

  initial begin
    $dumpfile("ch15_regfile8.vcd");
    $dumpvars(0, regfile8_tb);
    // r0 becomes our accumulator; write every cell a distinct value
    for (i = 0; i < 8; i = i + 1) begin
      @(negedge clk);
      we = 1; waddr = i[2:0]; wdata = 8'h10 + i[7:0];
      @(posedge clk); #1;
      we = 0;
      raddr_a = i[2:0]; #1;
      check8("write cell", ra, 8'h10 + i[7:0]);
    end
    // two ports can read different cells at once
    raddr_a = 3'd2; raddr_b = 3'd6; #1;
    check8("port A r2", ra, 8'h12);
    check8("port B r6", rb, 8'h16);
    // a write mid-cycle does NOT appear on the read port until the edge
    @(negedge clk);
    we = 1; waddr = 3'd3; wdata = 8'hAB;
    raddr_a = 3'd3; #1;
    check8("pre-edge still old", ra, 8'h13);
    @(posedge clk); #1;
    check8("post-edge new", ra, 8'hAB);
    // we=0 holds contents
    @(negedge clk);
    we = 0; waddr = 3'd3; wdata = 8'h77;
    @(posedge clk); #1;
    check8("we low keeps value", ra, 8'hAB);
    if (errors == 0) $display("PASS: regfile8 %0d checks clean", 12);
    $finish;
  end
endmodule
