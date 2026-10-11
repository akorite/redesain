// ch10_seq101.v -- "101" detector with overlap, Moore out.
module seq101(clk, x, hit);
  input clk, x; output reg hit;
  localparam IDLE=0, GOT1=1, GOT10=2, FOUND=3;
  reg [1:0] st = IDLE, nx;
  always @(*) case (st)
    IDLE:  nx = x ? GOT1 : IDLE;
    GOT1:  nx = x ? GOT1 : GOT10;
    GOT10: nx = x ? FOUND : IDLE;
    FOUND: nx = x ? GOT1 : GOT10;   // overlap: last 1 restarts
    default: nx = IDLE;
  endcase
  always @(posedge clk) st <= nx;
  always @(*) hit = (st == FOUND);
endmodule
