// Data RAM: 16 x 8, synchronous write, synchronous read.
// The registered read output is the shape that maps onto BRAM:
// a latch-free write path plus one output register. Read o_rdata
// one clock AFTER presenting i_raddr.
module ram16 (
  input  wire        i_clk,
  input  wire        i_we,
  input  wire [3:0]  i_addr,
  input  wire [7:0]  i_wdata,
  output reg  [7:0]  o_rdata
);
  reg [7:0] mem [0:15];
  always @(posedge i_clk) begin
    if (i_we) mem[i_addr] <= i_wdata;
    o_rdata <= mem[i_addr];
  end
endmodule
