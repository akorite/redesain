// ch09_full_adder.v -- one full adder cell, the ripple's brick.
module full_adder(a, b, cin, sum, cout);
  input  a, b, cin;
  output sum, cout;
  assign sum  = a ^ b ^ cin;
  assign cout = (a & b) | (cin & (a ^ b));
endmodule
