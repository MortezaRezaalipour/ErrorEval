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
  wire \U0.U0.new_n18 ;
  wire \U0.U0.new_n24 ;
  wire \U0.U2.DUT1.k0 ;
  wire \U0.po0 ;
  wire \U0.po4 ;
  wire \U0.po6 ;
  input [8:0] a;
  input [8:0] b;
  output [8:0] r;
  assign _00_ = b[4] | ~(a[4]);
  assign _01_ = b[6] | ~(a[6]);
  assign _02_ = _01_ & _00_;
  assign _03_ = a[5] & ~(b[5]);
  assign _04_ = _02_ & ~(_03_);
  assign _05_ = a[5] | ~(b[5]);
  assign _06_ = _01_ & ~(_05_);
  assign _07_ = _06_ | _04_;
  assign _08_ = b[6] & ~(a[6]);
  assign _09_ = _08_ | _07_;
  assign \U0.po4  = a[4] ^ b[4];
  assign \U0.po6  = \U0.po4  ^ _09_;
  assign \U0.po0  = a[0] ^ b[0];
  assign _10_ = b[5] ^ a[5];
  assign _11_ = ~_00_;
  assign _12_ = a[8] | ~(b[8]);
  assign _13_ = b[7] & ~(a[7]);
  assign _14_ = _13_ | _09_;
  assign _15_ = a[8] & ~(b[8]);
  assign _16_ = a[7] & ~(b[7]);
  assign _17_ = _16_ | _15_;
  assign _18_ = _14_ & ~(_17_);
  assign _19_ = _18_ | ~(_12_);
  assign _20_ = b[4] & ~(a[4]);
  assign _21_ = _19_ ? _11_ : _20_;
  assign _22_ = _21_ & ~(_10_);
  assign _23_ = _03_ | ~(_05_);
  assign _24_ = _23_ & ~(_21_);
  assign \U0.U2.DUT1.k0  = _24_ | _22_;
  assign _25_ = ~\U0.po4 ;
  assign _26_ = ~(_16_ | _13_);
  assign \U0.U0.new_n18  = _26_ ^ _25_;
  assign _27_ = _15_ | ~(_12_);
  assign _28_ = ~(_26_ & _25_);
  assign _29_ = _16_ & _12_;
  assign _30_ = _19_ & _13_;
  assign _31_ = _30_ | _29_;
  assign _32_ = _28_ & ~(_31_);
  assign \U0.U0.new_n24  = _27_ & ~(_32_);
  assign r = { \U0.U0.new_n24 , \U0.U0.new_n18 , \U0.po6 , \U0.U2.DUT1.k0 , \U0.po4 , 3'h2, \U0.po0  };
endmodule
