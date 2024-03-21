/* Generated by Yosys 0.9+4052 (git sha1 a5adb007, gcc 9.3.0-17ubuntu1~20.04 -fPIC -Os) */

module circuit(g0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g253, g252, g251, g250, g249, g248, g247, g246, g245);
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
  input g0;
  input g1;
  input g10;
  input g11;
  input g12;
  input g13;
  input g14;
  input g15;
  input g2;
  output g245;
  output g246;
  output g247;
  output g248;
  output g249;
  output g250;
  output g251;
  output g252;
  output g253;
  input g3;
  input g4;
  input g5;
  input g6;
  input g7;
  input g8;
  input g9;
  assign g245 = g7 ^ g15;
  assign _00_ = g7 | ~(g15);
  assign _01_ = _00_ & ~(g14);
  assign _02_ = _01_ | g6;
  assign _03_ = g7 | ~(g14);
  assign _04_ = g15 & ~(_03_);
  assign _05_ = _04_ | ~(_02_);
  assign _06_ = g5 & ~(g13);
  assign _07_ = _06_ | ~(_05_);
  assign _08_ = g13 & ~(g5);
  assign g246 = _08_ | ~(_07_);
  assign _09_ = ~(g246 & g12);
  assign _10_ = ~(_09_ & g4);
  assign _11_ = ~(g246 | g12);
  assign _12_ = _10_ & ~(_11_);
  assign _13_ = g11 & ~(g3);
  assign _14_ = _13_ | _12_;
  assign _15_ = g3 & ~(g11);
  assign g249 = _14_ & ~(_15_);
  assign _16_ = ~g10;
  assign _17_ = ~(_11_ | g4);
  assign _18_ = _17_ | ~(_09_);
  assign _19_ = _18_ & ~(_15_);
  assign _20_ = _19_ | _13_;
  assign _21_ = _20_ & ~(_16_);
  assign _22_ = _21_ | ~(g2);
  assign _23_ = _16_ & ~(_20_);
  assign _24_ = _22_ & ~(_23_);
  assign _25_ = g9 & ~(g1);
  assign _26_ = _25_ | _24_;
  assign _27_ = g0 & ~(g8);
  assign _28_ = _27_ | _26_;
  assign _29_ = g1 & ~(g9);
  assign _30_ = _29_ | g8;
  assign _31_ = _30_ & ~(g0);
  assign _32_ = _28_ & ~(_31_);
  assign _33_ = _29_ & g8;
  assign g250 = _32_ & ~(_33_);
  assign g247 = g246;
  assign g248 = 1'h1;
  assign g251 = g250;
  assign g252 = g250;
  assign g253 = 1'h0;
endmodule