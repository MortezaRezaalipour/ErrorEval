/* Generated by Yosys 0.9+4052 (git sha1 a5adb007, gcc 9.3.0-17ubuntu1~20.04 -fPIC -Os) */

module circ(x0, x1, x2, x3, x4, r);
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
  wire _101_;
  wire _102_;
  wire _103_;
  wire _104_;
  wire _105_;
  wire _106_;
  wire _107_;
  wire _108_;
  wire _109_;
  wire _110_;
  wire _111_;
  wire _112_;
  wire _113_;
  wire _114_;
  wire _115_;
  wire _116_;
  wire _117_;
  wire _118_;
  wire _119_;
  wire _120_;
  wire _121_;
  wire _122_;
  wire _123_;
  wire _124_;
  wire _125_;
  wire _126_;
  wire _127_;
  wire _128_;
  wire _129_;
  wire _130_;
  wire _131_;
  wire _132_;
  wire _133_;
  wire _134_;
  wire _135_;
  wire _136_;
  wire _137_;
  wire _138_;
  wire _139_;
  wire _140_;
  wire _141_;
  wire _142_;
  wire _143_;
  wire _144_;
  wire _145_;
  wire _146_;
  wire _147_;
  wire _148_;
  wire _149_;
  wire _150_;
  wire _151_;
  wire _152_;
  wire _153_;
  wire _154_;
  wire _155_;
  wire _156_;
  wire _157_;
  wire _158_;
  wire _159_;
  wire _160_;
  wire _161_;
  wire _162_;
  wire _163_;
  wire _164_;
  wire _165_;
  wire _166_;
  wire _167_;
  wire _168_;
  wire _169_;
  wire _170_;
  wire _171_;
  wire _172_;
  wire _173_;
  wire _174_;
  wire _175_;
  wire _176_;
  wire _177_;
  wire _178_;
  wire _179_;
  wire _180_;
  wire _181_;
  wire _182_;
  wire _183_;
  wire _184_;
  wire _185_;
  wire _186_;
  wire _187_;
  wire _188_;
  wire _189_;
  wire _190_;
  wire _191_;
  wire _192_;
  wire _193_;
  wire _194_;
  wire _195_;
  wire _196_;
  wire _197_;
  wire _198_;
  wire _199_;
  wire _200_;
  wire _201_;
  wire _202_;
  wire _203_;
  wire _204_;
  wire _205_;
  wire _206_;
  wire _207_;
  wire _208_;
  wire _209_;
  wire _210_;
  wire _211_;
  wire _212_;
  wire _213_;
  wire \U0.U5.new_n35 ;
  wire \U0.U6.new_n14 ;
  wire \U0.po1 ;
  wire \U0.po3 ;
  wire \U0.po4 ;
  output [4:0] r;
  input [3:0] x0;
  input [3:0] x1;
  input [3:0] x2;
  input [3:0] x3;
  input [3:0] x4;
  assign _140_ = x0[3] | ~(x2[3]);
  assign _141_ = x2[2] & ~(x0[2]);
  assign _142_ = x0[2] & ~(x2[2]);
  assign _143_ = x0[1] | ~(x2[1]);
  assign _144_ = x2[1] | ~(x0[1]);
  assign _145_ = x0[0] & ~(x2[0]);
  assign _146_ = _144_ & ~(_145_);
  assign _147_ = _143_ & ~(_146_);
  assign _148_ = ~(_147_ | _142_);
  assign _149_ = _148_ | _141_;
  assign _150_ = _149_ & ~(_140_);
  assign _151_ = x2[0] & ~(x0[0]);
  assign _152_ = _151_ & _144_;
  assign _153_ = _143_ & ~(_152_);
  assign _154_ = _153_ | _142_;
  assign _155_ = x2[3] | ~(x0[3]);
  assign _156_ = _155_ | _141_;
  assign _157_ = _154_ & ~(_156_);
  assign _158_ = ~(_157_ | _150_);
  assign _159_ = x0[3] | ~(x3[3]);
  assign _160_ = x0[2] | ~(x3[2]);
  assign _161_ = x0[1] & ~(x3[1]);
  assign _162_ = x0[2] & ~(x3[2]);
  assign _163_ = ~(_162_ | _161_);
  assign _164_ = _163_ | ~(_160_);
  assign _165_ = _159_ | ~(_164_);
  assign _166_ = x0[3] & ~(x3[3]);
  assign _167_ = x3[1] & ~(x0[1]);
  assign _168_ = _167_ | ~(_160_);
  assign _169_ = _168_ & ~(_162_);
  assign _170_ = _166_ & ~(_169_);
  assign _171_ = _165_ & ~(_170_);
  assign _172_ = _171_ ^ _158_;
  assign _173_ = x0[3] | ~(x1[3]);
  assign _174_ = x0[2] | ~(x1[2]);
  assign _175_ = x1[2] | ~(x0[2]);
  assign _176_ = x0[1] | ~(x1[1]);
  assign _177_ = x1[0] | ~(x0[0]);
  assign _178_ = x0[1] & ~(x1[1]);
  assign _179_ = _177_ & ~(_178_);
  assign _180_ = _176_ & ~(_179_);
  assign _181_ = _175_ & ~(_180_);
  assign _182_ = _181_ | ~(_174_);
  assign _183_ = _173_ | ~(_182_);
  assign _184_ = x0[3] & ~(x1[3]);
  assign _185_ = x1[0] & ~(x0[0]);
  assign _186_ = _185_ & ~(_178_);
  assign _187_ = _176_ & ~(_186_);
  assign _188_ = _187_ & _174_;
  assign _189_ = _175_ & ~(_188_);
  assign _190_ = _184_ & ~(_189_);
  assign _191_ = _183_ & ~(_190_);
  assign _192_ = ~(_191_ ^ _172_);
  assign _193_ = x0[3] | ~(x4[3]);
  assign _194_ = x0[2] | ~(x4[2]);
  assign _195_ = x4[2] | ~(x0[2]);
  assign _196_ = x4[1] & ~(x0[1]);
  assign _197_ = x4[0] | ~(x0[0]);
  assign _198_ = x0[1] & ~(x4[1]);
  assign _199_ = _197_ & ~(_198_);
  assign _200_ = ~(_199_ | _196_);
  assign _201_ = _195_ & ~(_200_);
  assign _202_ = _201_ | ~(_194_);
  assign _203_ = _202_ & ~(_193_);
  assign _204_ = x0[3] & ~(x4[3]);
  assign _205_ = x4[0] & ~(x0[0]);
  assign _206_ = _205_ & ~(_198_);
  assign _207_ = _206_ | _196_;
  assign _208_ = _194_ & ~(_207_);
  assign _209_ = _195_ & ~(_208_);
  assign _210_ = _204_ & ~(_209_);
  assign _211_ = ~(_210_ | _203_);
  assign _212_ = _142_ | _141_;
  assign _213_ = _155_ & _149_;
  assign _000_ = _140_ & ~(_213_);
  assign _001_ = _000_ | ~(_147_);
  assign _002_ = _140_ & ~(_149_);
  assign _003_ = _155_ & ~(_002_);
  assign _004_ = ~(_003_ | _153_);
  assign _005_ = _001_ & ~(_004_);
  assign _006_ = _000_ | _147_;
  assign _007_ = _153_ & ~(_003_);
  assign _008_ = _006_ & ~(_007_);
  assign _009_ = _212_ ? _005_ : _008_;
  assign _010_ = _160_ & ~(_162_);
  assign _011_ = _164_ & ~(_166_);
  assign _012_ = _159_ & ~(_011_);
  assign _013_ = _012_ | _161_;
  assign _014_ = ~_167_;
  assign _015_ = _164_ | ~(_159_);
  assign _016_ = _015_ & ~(_166_);
  assign _017_ = _014_ & ~(_016_);
  assign _018_ = _013_ & ~(_017_);
  assign _019_ = _016_ | _014_;
  assign _020_ = _161_ & ~(_012_);
  assign _021_ = _019_ & ~(_020_);
  assign _022_ = _010_ ? _021_ : _018_;
  assign _023_ = _009_ & ~(_022_);
  assign _024_ = ~(_175_ & _174_);
  assign _025_ = _173_ & ~(_182_);
  assign _026_ = ~(_025_ | _184_);
  assign _027_ = _026_ | _187_;
  assign _028_ = _182_ & ~(_184_);
  assign _029_ = _173_ & ~(_028_);
  assign _030_ = _180_ & ~(_029_);
  assign _031_ = _027_ & ~(_030_);
  assign _032_ = _029_ | _180_;
  assign _033_ = _187_ & ~(_026_);
  assign _034_ = _032_ & ~(_033_);
  assign _035_ = _024_ ? _034_ : _031_;
  assign _036_ = _195_ & _194_;
  assign _037_ = _193_ & ~(_202_);
  assign _038_ = ~(_037_ | _204_);
  assign _039_ = _038_ | _207_;
  assign _040_ = ~_200_;
  assign _041_ = _202_ & ~(_204_);
  assign _042_ = _193_ & ~(_041_);
  assign _043_ = _040_ & ~(_042_);
  assign _044_ = _039_ & ~(_043_);
  assign _045_ = _042_ | _040_;
  assign _046_ = _207_ & ~(_038_);
  assign _047_ = _045_ & ~(_046_);
  assign _048_ = _036_ ? _047_ : _044_;
  assign _049_ = _048_ | _035_;
  assign _050_ = x2[0] ^ x3[0];
  assign _051_ = ~(x2[0] ^ x3[0]);
  assign _052_ = ~(_051_ ^ _050_);
  assign _053_ = ~(_198_ | _196_);
  assign _054_ = _038_ | _205_;
  assign _055_ = _197_ & ~(_042_);
  assign _056_ = _054_ & ~(_055_);
  assign _057_ = _042_ | _197_;
  assign _058_ = _205_ & ~(_038_);
  assign _059_ = _057_ & ~(_058_);
  assign _060_ = _053_ ? _059_ : _056_;
  assign _061_ = _060_ | ~(_052_);
  assign _062_ = _053_ ? _056_ : _059_;
  assign _063_ = _052_ & ~(_062_);
  assign _064_ = _176_ & ~(_178_);
  assign _065_ = _026_ | _185_;
  assign _066_ = _177_ & ~(_029_);
  assign _067_ = _065_ & ~(_066_);
  assign _068_ = _029_ | _177_;
  assign _069_ = _185_ & ~(_026_);
  assign _070_ = _068_ & ~(_069_);
  assign _071_ = _064_ ? _070_ : _067_;
  assign _072_ = ~(_071_ | _063_);
  assign _073_ = _072_ | ~(_061_);
  assign _074_ = _024_ ? _031_ : _034_;
  assign _075_ = _036_ ? _044_ : _047_;
  assign _076_ = ~(_075_ | _074_);
  assign _077_ = _073_ & ~(_076_);
  assign _078_ = _049_ & ~(_077_);
  assign _079_ = _049_ & ~(_073_);
  assign _080_ = ~(_079_ | _076_);
  assign _081_ = _023_ ? _078_ : _080_;
  assign _082_ = ~(_081_ ^ _211_);
  assign _083_ = _082_ | _192_;
  assign _084_ = _010_ ? _018_ : _021_;
  assign _085_ = _009_ ? _022_ : _084_;
  assign _086_ = _049_ & ~(_076_);
  assign _087_ = ~(_086_ ^ _073_);
  assign _088_ = _087_ | ~(_085_);
  assign _089_ = _086_ ^ _073_;
  assign _090_ = _085_ ? _087_ : _089_;
  assign _091_ = ~(_144_ & _143_);
  assign _092_ = _145_ & ~(_000_);
  assign _093_ = _151_ & ~(_003_);
  assign _094_ = _093_ | _092_;
  assign _095_ = ~(_003_ | _151_);
  assign _096_ = ~(_000_ | _145_);
  assign _097_ = _096_ | _095_;
  assign _098_ = _091_ ? _094_ : _097_;
  assign _099_ = _064_ ? _067_ : _070_;
  assign _100_ = _061_ & ~(_063_);
  assign _101_ = _100_ | _099_;
  assign _102_ = _072_ & _061_;
  assign _103_ = _101_ & ~(_102_);
  assign _104_ = _098_ | ~(_103_);
  assign _105_ = ~(x4[0] ^ x1[0]);
  assign _106_ = _050_ & ~(_105_);
  assign _107_ = ~_197_;
  assign _108_ = x1[0] ? _205_ : _107_;
  assign _109_ = _108_ | _106_;
  assign _110_ = _098_ & ~(_103_);
  assign _111_ = _109_ & ~(_110_);
  assign _112_ = _104_ & ~(_111_);
  assign _113_ = _090_ & ~(_112_);
  assign _114_ = _088_ & ~(_113_);
  assign _115_ = _081_ ^ _211_;
  assign _116_ = _192_ & ~(_115_);
  assign _117_ = _116_ | ~(_114_);
  assign _118_ = ~(_117_ & _083_);
  assign _119_ = ~(_171_ | _158_);
  assign _120_ = _172_ & ~(_191_);
  assign _121_ = ~(_120_ | _119_);
  assign _122_ = _023_ & ~(_078_);
  assign _123_ = _080_ | _023_;
  assign _124_ = _123_ & ~(_211_);
  assign _125_ = ~(_124_ | _122_);
  assign _126_ = _211_ & ~(_122_);
  assign _127_ = _123_ & ~(_126_);
  assign _128_ = _121_ ? _125_ : _127_;
  assign _129_ = _118_ & ~(_128_);
  assign _130_ = _083_ & ~(_114_);
  assign _131_ = _130_ | _116_;
  assign _132_ = _121_ ? _127_ : _125_;
  assign _133_ = _131_ & ~(_132_);
  assign \U0.po4  = _133_ | _129_;
  assign _134_ = _192_ ? _115_ : _082_;
  assign \U0.po3  = ~(_134_ ^ _114_);
  assign _135_ = _104_ & ~(_110_);
  assign \U0.po1  = _135_ ^ _109_;
  assign _136_ = x4[0] ^ x1[0];
  assign _137_ = _136_ | ~(_051_);
  assign \U0.U6.new_n14  = _137_ & ~(_106_);
  assign _138_ = _109_ | ~(_104_);
  assign _139_ = _138_ & ~(_110_);
  assign \U0.U5.new_n35  = _090_ ? _112_ : _139_;
  assign r = { \U0.po4 , \U0.po3 , \U0.U5.new_n35 , \U0.po1 , \U0.U6.new_n14  };
endmodule