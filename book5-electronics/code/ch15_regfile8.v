// 8x8 register file: one synchronous write port, two asynchronous read ports.
// Reads are combinational (address in, data out now); the write lands on the
// clock edge. Both read ports may look at any register, including the one
// being written this cycle.
module regfile8 (
  input  wire        i_clk,
  input  wire        i_we,     // write enable
  input  wire [2:0]  i_waddr,  // which register to write
  input  wire [7:0]  i_wdata,
  input  wire [2:0]  i_raddr_a,
  input  wire [2:0]  i_raddr_b,
  output wire [7:0]  o_ra,
  output wire [7:0]  o_rb
);
  reg [7:0] mem [0:7];
  assign o_ra = mem[i_raddr_a];
  assign o_rb = mem[i_raddr_b];
  always @(posedge i_clk) begin
    if (i_we) mem[i_waddr] <= i_wdata;
  end
endmodule
