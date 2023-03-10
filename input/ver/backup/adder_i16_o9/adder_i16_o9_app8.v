// Benchmark "circuit" written by ABC on Wed Mar 16 10:20:12 2022

module circuit ( 
    g0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15,
    g123, g122, g121, g120, g119, g118, g117, g116, g115  );
  input  g0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14,
    g15;
  output g123, g122, g121, g120, g119, g118, g117, g116, g115;
  wire g16, g20, g25, g29, g31, g34, g35, g36, g37, g38, g39, g43, g45, g48,
    g49, g50, g51, g55, g57, g60, g61, g62, g63, g67, g69, g72, g73, g74,
    g75, g79, g81, g84, g85, g86, g87, g91, g93, g96, g97, g98, g99, g103,
    g104, g105, g114, \0 ;
  assign g16 = ~g15;
  assign g20 = ~g14;
  assign g25 = ~g7 | ~g15;
  assign g29 = ~g13;
  assign g31 = ~g5;
  assign g34 = ~g6 | ~g7;
  assign g35 = ~g16 & ~g34;
  assign g36 = ~g20 & ~g25;
  assign g37 = ~g35 & ~g36;
  assign g38 = ~g6 | ~g14;
  assign g39 = ~g37 | ~g38;
  assign g43 = ~g12;
  assign g45 = ~g4;
  assign g48 = ~g29 | ~g31;
  assign g49 = ~g39 | ~g48;
  assign g50 = ~g5 | ~g13;
  assign g51 = ~g49 | ~g50;
  assign g55 = ~g11;
  assign g57 = ~g3;
  assign g60 = ~g43 | ~g45;
  assign g61 = ~g51 | ~g60;
  assign g62 = ~g4 | ~g12;
  assign g63 = ~g61 | ~g62;
  assign g67 = ~g10;
  assign g69 = ~g2;
  assign g72 = ~g55 | ~g57;
  assign g73 = ~g63 | ~g72;
  assign g74 = ~g3 | ~g11;
  assign g75 = ~g73 | ~g74;
  assign g79 = ~g9;
  assign g81 = ~g1;
  assign g84 = ~g67 | ~g69;
  assign g85 = ~g75 | ~g84;
  assign g86 = ~g2 | ~g10;
  assign g87 = ~g85 | ~g86;
  assign g91 = ~g8;
  assign g93 = ~g0;
  assign g96 = ~g79 | ~g81;
  assign g97 = ~g87 | ~g96;
  assign g98 = ~g1 | ~g9;
  assign g99 = ~g97 | ~g98;
  assign g103 = ~g91 | ~g93;
  assign g104 = ~g99 | ~g103;
  assign g105 = ~g0 | ~g8;
  assign g114 = ~g104 | ~g105;
  assign g115 = \0 ;
  assign g116 = \0 ;
  assign g117 = \0 ;
  assign g118 = \0 ;
  assign g119 = \0 ;
  assign g120 = \0 ;
  assign g121 = \0 ;
  assign g122 = \0 ;
  assign g123 = g114;
  assign \0  = 1'b0;
endmodule


