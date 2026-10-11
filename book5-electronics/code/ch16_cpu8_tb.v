// ch16_cpu8_tb.v -- run fib.hex: check every OUT byte is the next
// Fibonacci number mod 256, then confirm the machine halts.
`timescale 1ns/1ps
module cpu8_tb;
  reg clk = 0, rst = 1;
  always #10 clk = ~clk;

  wire [7:0] a, pc, instr, out_r;
  wire out_we, halted;
  cpu8 #() u (.i_clk(clk), .i_rst(rst), .o_a(a), .o_pc(pc),
              .o_instr(instr), .o_out(out_r), .o_out_we(out_we),
              .o_halted(halted));

  integer errs = 0, outs = 0;
  reg pending = 0;
  reg [7:0] exp [0:12];
  integer i;
  initial begin
    exp[0]=1; exp[1]=1; exp[2]=2; exp[3]=3; exp[4]=5; exp[5]=8;
    exp[6]=13; exp[7]=21; exp[8]=34; exp[9]=55; exp[10]=89;
    exp[11]=144; exp[12]=0;
    $dumpfile("ch16_cpu8.vcd");
    $dumpvars(0, cpu8_tb);
    repeat (4) @(negedge clk);
    rst = 0;
    repeat (800) begin
      @(negedge clk);
      if (pending && !out_we) begin   // out_reg latched: NOW read it
        pending = 0;
        if (out_r !== exp[outs])
          begin errs=errs+1;
            $display("FAIL out[%0d]=%0d expected %0d",outs,out_r,exp[outs]); end
        else
          $display("OUT %3d ok (pc=%0d)", out_r, pc);
        outs = outs + 1;
      end
      if (out_we) pending = 1;        // byte lands at the next edge
      if (halted) begin
        if (outs !== 12) begin errs=errs+1;
          $display("FAIL: halted after %0d OUTs", outs); end
        else $display("PASS: cpu8 printed Fibonacci 1..144 then halted (%0d OUT bytes)", outs);
        if (errs) $display("FAILURES: %0d", errs); else $display("ALL CHECKS PASS");
        $finish;
      end
    end
    $display("FAIL: never halted");
    $finish;
  end
endmodule
