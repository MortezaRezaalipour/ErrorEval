/* Generated by Yosys 0.9+4052 (git sha1 a5adb007, gcc 9.3.0-17ubuntu1~20.04 -fPIC -Os) */

module circ(a, b, r);
  wire _00_;
  wire _01_;
  wire _02_;
  wire _03_;
  wire _04_;
  wire _05_;
  wire _06_;
  wire _07_;
  wire _08_;
  wire _09_;
  wire _10_;
  wire _11_;
  wire _12_;
  wire _13_;
  wire _14_;
  wire _15_;
  wire _16_;
  wire _17_;
  wire _18_;
  wire _19_;
  wire _20_;
  wire _21_;
  wire _22_;
  wire _23_;
  wire _24_;
  wire _25_;
  wire _26_;
  wire _27_;
  wire _28_;
  wire _29_;
  wire _30_;
  wire _31_;
  wire _32_;
  wire _33_;
  wire _34_;
  wire _35_;
  wire _36_;
  wire _37_;
  wire _38_;
  wire _39_;
  wire \U0.U0.new_n18 ;
  wire \U0.U0.new_n24 ;
  wire \U0.U1.DUT1.k0 ;
  wire \U0.po0 ;
  wire \U0.po4 ;
  wire \U0.po6 ;
  input [8:0] a;
  input [8:0] b;
  output [8:0] r;
  assign \U0.U1.DUT1.k0  = a[3] & ~(b[3]);
  assign _00_ = a[1] & ~(b[1]);
  assign _01_ = _00_ | a[0];
  assign _02_ = b[1] & ~(a[1]);
  assign _03_ = _01_ & ~(_02_);
  assign _04_ = a[2] & ~(b[2]);
  assign _05_ = _04_ | _03_;
  assign _06_ = b[2] & ~(a[2]);
  assign _07_ = _05_ & ~(_06_);
  assign _08_ = b[3] & ~(a[3]);
  assign _09_ = _07_ & ~(_08_);
  assign _10_ = _09_ | \U0.U1.DUT1.k0 ;
  assign _11_ = _10_ & ~(b[4]);
  assign _12_ = ~(_11_ | a[4]);
  assign _13_ = b[4] & ~(_10_);
  assign _14_ = _13_ | _12_;
  assign _15_ = a[6] & ~(b[6]);
  assign _16_ = _14_ & ~(_15_);
  assign _17_ = a[5] & ~(b[5]);
  assign _18_ = _16_ & ~(_17_);
  assign _19_ = b[5] & ~(a[5]);
  assign _20_ = _19_ & ~(_15_);
  assign _21_ = _20_ | _18_;
  assign _22_ = b[6] & ~(a[6]);
  assign _23_ = _22_ | _21_;
  assign \U0.po4  = a[4] ^ b[4];
  assign \U0.po6  = \U0.po4  ^ _23_;
  assign \U0.po0  = a[0] ^ b[0];
  assign _24_ = ~\U0.po4 ;
  assign _25_ = b[7] & ~(a[7]);
  assign _26_ = a[7] & ~(b[7]);
  assign _27_ = ~(_26_ | _25_);
  assign \U0.U0.new_n18  = _27_ ^ _24_;
  assign _28_ = b[8] & ~(a[8]);
  assign _29_ = a[8] & ~(b[8]);
  assign _30_ = _29_ | _28_;
  assign _31_ = ~(_27_ & _24_);
  assign _32_ = _26_ & ~(_28_);
  assign _33_ = _25_ | _23_;
  assign _34_ = _29_ | _26_;
  assign _35_ = _34_ | ~(_33_);
  assign _36_ = _35_ & ~(_28_);
  assign _37_ = _25_ & ~(_36_);
  assign _38_ = _37_ | _32_;
  assign _39_ = _31_ & ~(_38_);
  assign \U0.U0.new_n24  = _30_ & ~(_39_);
  assign r = { \U0.U0.new_n24 , \U0.U0.new_n18 , \U0.po6 , 1'h0, \U0.po4 , \U0.U1.DUT1.k0 , 2'h2, \U0.po0  };
endmodule
