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
  wire \U0.U1.new_n26 ;
  wire \U0.U1.new_n45 ;
  wire \U0.U1.new_n51 ;
  wire \U0.po00 ;
  wire \U0.po07 ;
  input [9:0] a;
  input [9:0] b;
  output [9:0] r;
  assign _00_ = a[6] | ~(b[6]);
  assign _01_ = ~_00_;
  assign _02_ = b[6] | ~(a[6]);
  assign _03_ = ~_02_;
  assign _04_ = a[9] | ~(b[9]);
  assign _05_ = a[7] & ~(b[7]);
  assign _06_ = _02_ & ~(_05_);
  assign _07_ = b[8] & ~(a[8]);
  assign _08_ = b[7] & ~(a[7]);
  assign _09_ = _08_ | _07_;
  assign _10_ = _09_ | _06_;
  assign _11_ = a[9] & ~(b[9]);
  assign _12_ = a[8] & ~(b[8]);
  assign _13_ = _12_ | _11_;
  assign _14_ = _10_ & ~(_13_);
  assign _15_ = _14_ | ~(_04_);
  assign _16_ = _15_ ? _01_ : _03_;
  assign _17_ = _08_ | _05_;
  assign \U0.po07  = ~(_17_ ^ _16_);
  assign \U0.po00  = a[0] ^ b[0];
  assign \U0.U1.new_n26  = _02_ & _00_;
  assign _18_ = ~(_12_ | _07_);
  assign _19_ = _17_ | _16_;
  assign _20_ = _15_ ? _05_ : _08_;
  assign _21_ = _19_ & ~(_20_);
  assign \U0.U1.new_n45  = _21_ ^ _18_;
  assign _22_ = _11_ | ~(_04_);
  assign _23_ = ~(_21_ & _18_);
  assign _24_ = _15_ & _07_;
  assign _25_ = _12_ & _04_;
  assign _26_ = _25_ | _24_;
  assign _27_ = _23_ & ~(_26_);
  assign \U0.U1.new_n51  = _22_ & ~(_27_);
  assign r = { \U0.U1.new_n51 , \U0.U1.new_n45 , \U0.po07 , \U0.U1.new_n26 , 5'h15, \U0.po00  };
endmodule