`timescale 1ns/1ps
module golden_tb;
  reg clk=0, en=0, sin=0;
  wire [7:0] q;
  shift8 u(.clk(clk), .en(en), .sin(sin), .q(q));
  reg [7:0] model = 0;                    // the golden copy
  integer errors = 0;
  always #5 clk=~clk;
  always @(posedge clk) #1 begin         // run the model alongside
    if (en) model = {model[6:0], sin};   // what shift SHOULD do
    if (q !== model) begin
      errors = errors + 1;
      $display("MISMATCH t=%0d q=%b model=%b", $time, q, model);
    end
  end
  initial begin
    en=1; sin=1; #10 sin=0; #30 en=0; #10;
    if (errors == 0) $display("PASS: %0d edges clean", 5);
    else $display("FAIL: %0d mismatches", errors);
    $finish;
  end
endmodule
