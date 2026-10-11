// Program ROM: 16 x 8, combinational read. Contents load from
// ch15_program.hex -- the program is data sitting in memory, exactly
// like the machine will execute it in ch16.
module rom16 (
  input  wire [3:0] i_addr,
  output wire [7:0] o_data
);
  reg [7:0] mem [0:15];
  initial $readmemh("ch15_program.hex", mem);
  assign o_data = mem[i_addr];
endmodule
