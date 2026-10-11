// ch11_tb_template.v -- the testbench recipe, every line on purpose.
`timescale 1ns/1ps                    // sim units
module mymod_tb;                      // tb is a module too, no ports
  reg clk = 0, rst = 1;               // reg: we drive them procedurally
  wire [3:0] q;                       // wire: the DUT drives it
  mymod u(.clk(clk), .rst(rst), .q(q));  // instantiate (unit under test)
  always #5 clk = ~clk;               // free-running clock, 10 ns period
  initial begin
    $dumpfile("mymod.vcd");           // record every signal...
    $dumpvars(0, mymod_tb);           // ...into a waveform file
    $monitor("t=%0d q=%0d", $time, q);// text trace for the page
    #15 rst = 0;                      // stimulus, in time order
    #100 $finish;                     // always end the sim yourself
  end
endmodule
