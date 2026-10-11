// ch16_cpu8_mult_tb.v -- run mult.hex: 7x6 by repeated addition -> 42.
`timescale 1ns/1ps
module cpu8_mult_tb;
  reg clk = 0, rst = 1;
  always #10 clk = ~clk;
  wire [7:0] a, pc, instr, out_r;
  wire out_we, halted;
  reg pending = 0;
  cpu8 u (.i_clk(clk), .i_rst(rst), .o_a(a), .o_pc(pc),
          .o_instr(instr), .o_out(out_r), .o_out_we(out_we),
          .o_halted(halted));
  initial begin
    $dumpfile("ch16_mult.vcd"); $dumpvars(0, cpu8_mult_tb);
    u.rom[0]=8'h10; u.rom[1]=8'h07; u.rom[2]=8'h21; u.rom[3]=8'h10;
    u.rom[4]=8'h06; u.rom[5]=8'h22; u.rom[6]=8'h10; u.rom[7]=8'h01;
    u.rom[8]=8'h23; u.rom[9]=8'h10; u.rom[10]=8'h00; u.rom[11]=8'h24;
    u.rom[12]=8'ha4; u.rom[13]=8'h31; u.rom[14]=8'h24; u.rom[15]=8'ha2;
    u.rom[16]=8'h43; u.rom[17]=8'h22; u.rom[18]=8'h70; u.rom[19]=8'h16;
    u.rom[20]=8'h60; u.rom[21]=8'h0c; u.rom[22]=8'ha4; u.rom[23]=8'h80;
    u.rom[24]=8'h90;
    repeat (4) @(negedge clk); rst = 0;
    repeat (400) begin
      @(negedge clk);
      if (pending && !out_we) begin   // out_reg latched: read it
        pending = 0;
        if (out_r === 8'd42) $display("PASS: 7*6 printed %0d", out_r);
        else $display("FAIL: OUT=%0d expected 42", out_r);
      end
      if (out_we) pending = 1;
      if (halted) begin
        $display("mult run halted at pc=%0d", pc); $finish;
      end
    end
    $display("FAIL: never halted"); $finish;
  end
endmodule
