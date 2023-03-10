// Benchmark "circuit" written by ABC on Sun Jul  8 15:05:00 2018

module circuit ( 
    g0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15,
    g16, g17, g18, g19, g20, g21, g22, g23, g24, g25, g26, g27, g28, g29,
    g30, g31,
    g251, g250, g249, g248, g247, g246, g245, g244, g243, g242, g241, g240,
    g239, g238, g237, g236, g235  );
  input  g0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14,
    g15, g16, g17, g18, g19, g20, g21, g22, g23, g24, g25, g26, g27, g28,
    g29, g30, g31;
  output g251, g250, g249, g248, g247, g246, g245, g244, g243, g242, g241,
    g240, g239, g238, g237, g236, g235;
  wire g32, g36, g38, g41, g42, g43, g44, g45, g46, g47, g48, g49, g50, g51,
    g52, g53, g54, g55, g56, g57, g58, g59, g60, g61, g62, g63, g64, g65,
    g66, g67, g68, g69, g70, g71, g72, g73, g74, g75, g76, g77, g78, g79,
    g80, g81, g82, g83, g84, g85, g86, g87, g88, g89, g90, g91, g92, g93,
    g94, g95, g96, g100, g102, g105, g106, g107, g108, g112, g114, g117,
    g118, g119, g120, g124, g126, g129, g130, g131, g132, g136, g137, g138,
    g139, g140, g141, g142, g143, g144, g145, g146, g147, g148, g149, g150,
    g151, g152, g153, g154, g155, g156, g157, g158, g159, g160, g161, g162,
    g232, g233, g234, \0 ;
  assign g32 = ~g31;
  assign g36 = ~g21;
  assign g38 = ~g5;
  assign g41 = ~g6;
  assign g42 = ~g22;
  assign g43 = ~g41 | ~g42;
  assign g44 = ~g7;
  assign g45 = ~g23;
  assign g46 = ~g44 | ~g45;
  assign g47 = ~g8;
  assign g48 = ~g24;
  assign g49 = ~g47 | ~g48;
  assign g50 = ~g9;
  assign g51 = ~g25;
  assign g52 = ~g50 | ~g51;
  assign g53 = ~g10;
  assign g54 = ~g26;
  assign g55 = ~g53 | ~g54;
  assign g56 = ~g11;
  assign g57 = ~g27;
  assign g58 = ~g56 | ~g57;
  assign g59 = ~g12;
  assign g60 = ~g28;
  assign g61 = ~g59 | ~g60;
  assign g62 = ~g13;
  assign g63 = ~g29;
  assign g64 = ~g62 | ~g63;
  assign g65 = ~g14 | ~g15;
  assign g66 = ~g32 & ~g65;
  assign g67 = ~g30;
  assign g68 = ~g15 | ~g31;
  assign g69 = ~g67 & ~g68;
  assign g70 = ~g66 & ~g69;
  assign g71 = ~g14 | ~g30;
  assign g72 = ~g70 | ~g71;
  assign g73 = ~g64 | ~g72;
  assign g74 = ~g13 | ~g29;
  assign g75 = ~g73 | ~g74;
  assign g76 = ~g61 | ~g75;
  assign g77 = ~g12 | ~g28;
  assign g78 = ~g76 | ~g77;
  assign g79 = ~g58 | ~g78;
  assign g80 = ~g11 | ~g27;
  assign g81 = ~g79 | ~g80;
  assign g82 = ~g55 | ~g81;
  assign g83 = ~g10 | ~g26;
  assign g84 = ~g82 | ~g83;
  assign g85 = ~g52 | ~g84;
  assign g86 = ~g9 | ~g25;
  assign g87 = ~g85 | ~g86;
  assign g88 = ~g49 | ~g87;
  assign g89 = ~g8 | ~g24;
  assign g90 = ~g88 | ~g89;
  assign g91 = ~g46 | ~g90;
  assign g92 = ~g7 | ~g23;
  assign g93 = ~g91 | ~g92;
  assign g94 = ~g43 | ~g93;
  assign g95 = ~g6 | ~g22;
  assign g96 = ~g94 | ~g95;
  assign g100 = ~g20;
  assign g102 = ~g4;
  assign g105 = ~g36 | ~g38;
  assign g106 = ~g96 | ~g105;
  assign g107 = ~g5 | ~g21;
  assign g108 = ~g106 | ~g107;
  assign g112 = ~g19;
  assign g114 = ~g3;
  assign g117 = ~g100 | ~g102;
  assign g118 = ~g108 | ~g117;
  assign g119 = ~g4 | ~g20;
  assign g120 = ~g118 | ~g119;
  assign g124 = ~g18;
  assign g126 = ~g2;
  assign g129 = ~g112 | ~g114;
  assign g130 = ~g120 | ~g129;
  assign g131 = ~g3 | ~g19;
  assign g132 = ~g130 | ~g131;
  assign g136 = ~g17;
  assign g137 = ~g1 | ~g136;
  assign g138 = ~g1;
  assign g139 = ~g17 | ~g138;
  assign g140 = ~g137 | ~g139;
  assign g141 = ~g124 | ~g126;
  assign g142 = ~g132 | ~g141;
  assign g143 = ~g2 | ~g18;
  assign g144 = ~g142 | ~g143;
  assign g145 = ~g140 | ~g144;
  assign g146 = ~g145;
  assign g147 = ~g140 & ~g144;
  assign g148 = ~g16;
  assign g149 = ~g0 | ~g148;
  assign g150 = ~g0;
  assign g151 = ~g16 | ~g150;
  assign g152 = ~g149 | ~g151;
  assign g153 = ~g136 | ~g138;
  assign g154 = ~g144 | ~g153;
  assign g155 = ~g1 | ~g17;
  assign g156 = ~g154 | ~g155;
  assign g157 = ~g152 | ~g156;
  assign g158 = ~g157;
  assign g159 = ~g152 & ~g156;
  assign g160 = ~g148 | ~g150;
  assign g161 = ~g156 | ~g160;
  assign g162 = ~g0 | ~g16;
  assign g232 = ~g146 & ~g147;
  assign g233 = ~g158 & ~g159;
  assign g234 = ~g161 | ~g162;
  assign g235 = \0 ;
  assign g236 = \0 ;
  assign g237 = \0 ;
  assign g238 = \0 ;
  assign g239 = \0 ;
  assign g240 = \0 ;
  assign g241 = \0 ;
  assign g242 = \0 ;
  assign g243 = \0 ;
  assign g244 = \0 ;
  assign g245 = \0 ;
  assign g246 = \0 ;
  assign g247 = \0 ;
  assign g248 = \0 ;
  assign g249 = g232;
  assign g250 = g233;
  assign g251 = g234;
  assign \0  = 1'b0;
endmodule


