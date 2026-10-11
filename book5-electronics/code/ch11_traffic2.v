// ch11_traffic2.v -- ch10's traffic FSM recoded book-style:
// parameters for encodings, named wires, one-line next-state table.
module traffic2(clk, rst, ns, ew);
  input clk, rst;
  output reg [1:0] ns, ew;              // 00=red 01=yellow 10=green
  parameter RED=2'b00, YEL=2'b01, GRN=2'b10;
  parameter NSG=0, NSY=1, EWG=2, EWY=3; // state encodings
  reg [1:0] st, nx;
  always @(*) case (st)                 // next-state logic
    NSG: nx = NSY;  NSY: nx = EWG;
    EWG: nx = EWY;  default: nx = NSG;
  endcase
  always @(posedge clk)                 // state register
    if (rst) st <= NSG; else st <= nx;
  always @(*) case (st)                 // output logic (Moore)
    NSG: begin ns=GRN; ew=RED; end
    NSY: begin ns=YEL; ew=RED; end
    EWG: begin ns=RED; ew=GRN; end
    default: begin ns=RED; ew=YEL; end
  endcase
endmodule
