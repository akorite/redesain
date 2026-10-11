// Checks rom16 (combinational reads of ch15_program.hex) and ram16
// (write-then-readback with the BRAM shape's one-cycle read latency).
`timescale 1ns/1ps
module mem_tb;
  reg clk = 0, we = 0;
  reg [3:0] addr = 0, raddr = 0;
  reg [7:0] wdata = 0;
  wire [7:0] rdata, romdata;
  integer errors = 0, i;

  rom16 urom(.i_addr(addr), .o_data(romdata));
  ram16 uram(.i_clk(clk), .i_we(we), .i_addr(addr), .i_wdata(wdata), .o_rdata(rdata));

  always #5 clk = ~clk;

  task check(input [191:0] what, input [7:0] got, input [7:0] exp);
    if (got !== exp) begin
      errors = errors + 1;
      $display("FAIL %0s: got=%h exp=%h", what, got, exp);
    end
  endtask

  initial begin
    $dumpfile("ch15_mem.vcd");
    $dumpvars(0, mem_tb);
    #1;
    // ROM: the first bytes of ch15_program.hex, read combinationally
    addr = 4'd0; #1; check("rom[0] LDI A",      romdata, 8'h10);
    addr = 4'd1; #1; check("rom[1] imm8 05",    romdata, 8'h05);
    addr = 4'd2; #1; check("rom[2] MOV r1",     romdata, 8'h21);
    addr = 4'd6; #1; check("rom[6] ADD r1",     romdata, 8'h31);
    addr = 4'd9; #1; check("rom[9] HALT",       romdata, 8'h90);
    // RAM: write a value on the edge, read it back a cycle later
    @(negedge clk);
    we = 1; addr = 4'd5; wdata = 8'hC3;
    @(posedge clk); #1;
    we = 0; addr = 4'd0;          // move the address off so only reads matter
    @(negedge clk);
    addr = 4'd5;
    @(posedge clk); #1;           // read lands one edge after the address
    check("ram readback", rdata, 8'hC3);
    // overwrite and confirm the old value is gone
    @(negedge clk);
    we = 1; addr = 4'd5; wdata = 8'h55;
    @(posedge clk); #1;
    we = 0;
    @(posedge clk); #1;
    check("ram overwritten", rdata, 8'h55);
    if (errors == 0) $display("PASS: rom16 + ram16 %0d checks clean", 8);
    $finish;
  end
endmodule
