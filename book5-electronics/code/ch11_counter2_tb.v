`timescale 1ns/1ps
module counter2_tb;
  reg clk=0, rst=1, en=0;
  wire [3:0] q; wire tc;
  integer errors = 0;
  counter2 u(.clk(clk), .rst(rst), .en(en), .q(q), .tc(tc));
  always #5 clk = ~clk;
  // the self-check: one task, compares reality to expectation
  task check(input [3:0] want, input [8*24-1:0] what);
    if (q !== want) begin
      errors = errors + 1;
      $display("FAIL t=%0d %0s: q=%0d expected %0d", $time, what, q, want);
    end
  endtask
  initial begin
    #12 rst=0; en=1;
    repeat (4) @(posedge clk); #1 check(4, "counted to 4");
    en=0; @(posedge clk); #1 check(4, "hold when en=0");
`ifdef SABOTAGE
    check(9, "planted bad check");
`endif
    rst=1; @(posedge clk); #1 check(0, "rst clears");
    if (errors == 0) $display("PASS: all %0d checks", 3);
    else $display("FAIL: %0d errors", errors);
    $finish;
  end
endmodule
