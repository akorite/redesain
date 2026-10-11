`timescale 1ns/1ps
module mux4_tb;
  reg sel=0, a=0, b=0;
  wire y1,y2,y3,y4,yl,ys;
  mux_assign u1(.sel(sel),.a(a),.b(b),.y(y1));
  mux_bool   u2(.sel(sel),.a(a),.b(b),.y(y2));
  mux_if     u3(.sel(sel),.a(a),.b(b),.y(y3));
  mux_case   u4(.sel(sel),.a(a),.b(b),.y(y4));
  mux_latch  u5(.sel(sel),.a(a),.b(b),.y(yl));
  mux_stale  u6(.sel(sel),.a(a),.b(b),.y(ys));
  initial $monitor("t=%2d sel=%b a=%b b=%b | y1..4=%b%b%b%b latch=%b stale=%b",
                   $time, sel, a, b, y1, y2, y3, y4, yl, ys);
  initial begin
    a=0;b=1;sel=0; #10;
    sel=1;         #10;   // legal muxes -> b=1; latch/stale vary
    a=1;b=0;       #10;   // inputs change, sel stays 1
    sel=0;         #10;
    $finish;
  end
endmodule
