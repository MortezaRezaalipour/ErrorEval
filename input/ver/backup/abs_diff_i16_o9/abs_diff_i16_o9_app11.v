/* Generated by Yosys 0.9+4052 (git sha1 a5adb007, gcc 9.3.0-17ubuntu1~20.04 -fPIC -Os) */

module circ(a, b, r);
  wire \U0.U1.DUT1.k0 ;
  wire \U0.po0 ;
  input [8:0] a;
  input [8:0] b;
  output [8:0] r;
  assign \U0.po0  = a[0] ^ b[0];
  assign \U0.U1.DUT1.k0  = a[3] & ~(b[3]);
  assign r = { 5'h05, \U0.U1.DUT1.k0 , 2'h2, \U0.po0  };
endmodule
