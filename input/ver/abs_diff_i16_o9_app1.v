/* Generated by Yosys 0.9+4052 (git sha1 a5adb007, gcc 9.3.0-17ubuntu1~20.04 -fPIC -Os) */

module circuit(g0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g253, g252, g251, g250, g249, g248, g247, g246, g245);
  wire _000_;
  wire _001_;
  wire _002_;
  wire _003_;
  wire _004_;
  wire _005_;
  wire _006_;
  wire _007_;
  wire _008_;
  wire _009_;
  wire _010_;
  wire _011_;
  wire _012_;
  wire _013_;
  wire _014_;
  wire _015_;
  wire _016_;
  wire _017_;
  wire _018_;
  wire _019_;
  wire _020_;
  wire _021_;
  wire _022_;
  wire _023_;
  wire _024_;
  wire _025_;
  wire _026_;
  wire _027_;
  wire _028_;
  wire _029_;
  wire _030_;
  wire _031_;
  wire _032_;
  wire _033_;
  wire _034_;
  wire _035_;
  wire _036_;
  wire _037_;
  wire _038_;
  wire _039_;
  wire _040_;
  wire _041_;
  wire _042_;
  wire _043_;
  wire _044_;
  wire _045_;
  wire _046_;
  wire _047_;
  wire _048_;
  wire _049_;
  wire _050_;
  wire _051_;
  wire _052_;
  wire _053_;
  wire _054_;
  wire _055_;
  wire _056_;
  wire _057_;
  wire _058_;
  wire _059_;
  wire _060_;
  wire _061_;
  wire _062_;
  wire _063_;
  wire _064_;
  wire _065_;
  wire _066_;
  wire _067_;
  wire _068_;
  wire _069_;
  wire _070_;
  wire _071_;
  wire _072_;
  wire _073_;
  wire _074_;
  wire _075_;
  wire _076_;
  wire _077_;
  wire _078_;
  wire _079_;
  wire _080_;
  wire _081_;
  wire _082_;
  wire _083_;
  wire _084_;
  wire _085_;
  wire _086_;
  wire _087_;
  wire _088_;
  wire _089_;
  wire _090_;
  wire _091_;
  wire _092_;
  wire _093_;
  wire _094_;
  wire _095_;
  wire _096_;
  wire _097_;
  wire _098_;
  wire _099_;
  wire _100_;
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
  assign g245 = g15 ^ g7;
  assign _030_ = g0 & ~(g8);
  assign _031_ = g1 & ~(g9);
  assign _032_ = g10 | ~(g2);
  assign _033_ = g13 | ~(g5);
  assign _034_ = g5 | ~(g13);
  assign _035_ = g6 & ~(g14);
  assign _036_ = g7 | ~(g15);
  assign _037_ = g14 & ~(g6);
  assign _038_ = _036_ & ~(_037_);
  assign _039_ = ~(_038_ | _035_);
  assign _040_ = _034_ & ~(_039_);
  assign _041_ = _040_ | ~(_033_);
  assign _042_ = _041_ & ~(g12);
  assign _043_ = _042_ | g4;
  assign _044_ = g12 & ~(_041_);
  assign _045_ = _043_ & ~(_044_);
  assign _046_ = g3 & ~(g11);
  assign _047_ = _046_ | _045_;
  assign _048_ = g11 & ~(g3);
  assign _049_ = _047_ & ~(_048_);
  assign _050_ = g10 & ~(g2);
  assign _051_ = _049_ & ~(_050_);
  assign _052_ = _051_ | ~(_032_);
  assign _053_ = g9 & ~(g1);
  assign _054_ = _052_ & ~(_053_);
  assign _055_ = _054_ | _031_;
  assign _056_ = g8 & ~(g0);
  assign _057_ = ~(_056_ | _055_);
  assign _058_ = _057_ | _030_;
  assign _059_ = _058_ & g245;
  assign _060_ = ~(_037_ | _035_);
  assign _061_ = _060_ ^ _036_;
  assign g246 = _061_ ^ _059_;
  assign _062_ = ~(_035_ | _036_);
  assign _063_ = ~(_062_ | _037_);
  assign _064_ = _034_ & _033_;
  assign _065_ = _064_ ? _039_ : _063_;
  assign _066_ = g245 | ~(_060_);
  assign _067_ = _066_ & _058_;
  assign g247 = _067_ ^ _065_;
  assign _068_ = _066_ | _065_;
  assign _069_ = _033_ & ~(_063_);
  assign _070_ = _034_ & ~(_069_);
  assign _071_ = g4 ^ g12;
  assign _072_ = _041_ & ~(_071_);
  assign _073_ = g4 | ~(g12);
  assign _074_ = g12 | ~(g4);
  assign _075_ = g11 ? _074_ : _073_;
  assign _076_ = g3 & ~(_075_);
  assign _077_ = _076_ | _072_;
  assign _078_ = g11 ? _073_ : _074_;
  assign _079_ = _078_ | g3;
  assign _080_ = _079_ & ~(_077_);
  assign _081_ = _080_ | _070_;
  assign _082_ = g3 ^ g11;
  assign _083_ = _072_ & ~(_082_);
  assign _084_ = _081_ & ~(_083_);
  assign g248 = _084_ | _068_;
  assign _085_ = _068_ | ~(_071_);
  assign _086_ = ~(_074_ & _058_);
  assign _087_ = _082_ & ~(_086_);
  assign _088_ = _085_ & ~(_087_);
  assign _089_ = _088_ | _070_;
  assign _090_ = ~(_074_ & _073_);
  assign _091_ = _090_ | _068_;
  assign _092_ = ~(_073_ & _058_);
  assign _093_ = ~(_048_ | _046_);
  assign _094_ = _093_ & ~(_092_);
  assign _095_ = _091_ & ~(_094_);
  assign _096_ = _041_ & ~(_095_);
  assign _097_ = _089_ & ~(_096_);
  assign _098_ = _073_ & _070_;
  assign _099_ = _074_ & ~(_098_);
  assign _100_ = _058_ ? _073_ : _099_;
  assign _000_ = _082_ & ~(_100_);
  assign _001_ = _097_ & ~(_000_);
  assign _002_ = _074_ & ~(_041_);
  assign _003_ = _073_ & ~(_002_);
  assign _004_ = _058_ ? _074_ : _003_;
  assign _005_ = _093_ & ~(_004_);
  assign _006_ = _001_ & ~(_005_);
  assign g249 = _006_ ^ g248;
  assign _007_ = ~_049_;
  assign _008_ = _070_ | ~(g12);
  assign _009_ = ~(_008_ & g4);
  assign _010_ = _070_ & ~(g12);
  assign _011_ = _009_ & ~(_010_);
  assign _012_ = ~(_011_ | _048_);
  assign _013_ = _012_ | _046_;
  assign _014_ = _032_ & ~(_050_);
  assign _015_ = _014_ ? _007_ : _013_;
  assign _016_ = g248 & _058_;
  assign g250 = _016_ ^ _015_;
  assign _017_ = ~_052_;
  assign _018_ = _032_ & ~(_013_);
  assign _019_ = ~(_018_ | _050_);
  assign _020_ = ~(_053_ | _031_);
  assign _021_ = _020_ ? _017_ : _019_;
  assign _022_ = ~(_015_ | g248);
  assign _023_ = _058_ & ~(_022_);
  assign g251 = _023_ ^ _021_;
  assign _024_ = _030_ & ~(_055_);
  assign _025_ = ~(_056_ | _030_);
  assign _026_ = _025_ ^ _055_;
  assign _027_ = _022_ & ~(_021_);
  assign _028_ = _058_ & ~(_027_);
  assign _029_ = _026_ & ~(_028_);
  assign g252 = _029_ | _024_;
  assign g253 = 1'h0;
endmodule
