`timescale 1ns/1ps
module report_tb;
  integer n = 0, errors = 0, warns = 0;
  task check(input cond, input [8*24-1:0] what);
    if (cond) n = n + 1;
    else begin
      errors = errors + 1;
      $display("%0t ERROR %0s failed", $time, what);
    end
  endtask
  initial begin
    $display("--- tb start ---");
    check(4 == 4,   "add table row");
    check(15 == 15, "terminal count");
    check(0 === 1'bx, "planted x compare");
    if (errors > 4) $fatal(1, "too many errors, aborting");
    $display("--- tb done: %0d checks, %0d errors ---", n, errors);
    $finish;
  end
endmodule
