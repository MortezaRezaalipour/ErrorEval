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
  wire _214_;
  wire _215_;
  wire _216_;
  wire _217_;
  wire _218_;
  wire _219_;
  wire _220_;
  wire _221_;
  wire _222_;
  wire \U0.U5.new_n35 ;
  wire \U0.U6.DUT1.k3 ;
  wire \U0.po1 ;
  wire \U0.po3 ;
  wire \U0.po4 ;
  output [4:0] r;
  input [3:0] x0;
  input [3:0] x1;
  input [3:0] x2;
  input [3:0] x3;
  input [3:0] x4;
  assign _149_ = x0[3] | ~(x2[3]);
  assign _150_ = x2[2] & ~(x0[2]);
  assign _151_ = x2[2] | ~(x0[2]);
  assign _152_ = x0[1] | ~(x2[1]);
  assign _153_ = x2[1] | ~(x0[1]);
  assign _154_ = x0[0] & ~(x2[0]);
  assign _155_ = _153_ & ~(_154_);
  assign _156_ = _152_ & ~(_155_);
  assign _157_ = _151_ & ~(_156_);
  assign _158_ = _157_ | _150_;
  assign _159_ = _158_ & ~(_149_);
  assign _160_ = x2[0] & ~(x0[0]);
  assign _161_ = _160_ & _153_;
  assign _162_ = _152_ & ~(_161_);
  assign _163_ = _162_ | ~(_151_);
  assign _164_ = x2[3] | ~(x0[3]);
  assign _165_ = _164_ | _150_;
  assign _166_ = _163_ & ~(_165_);
  assign _167_ = ~(_166_ | _159_);
  assign _168_ = x0[3] | ~(x3[3]);
  assign _169_ = x0[2] | ~(x3[2]);
  assign _170_ = x3[1] & ~(x0[1]);
  assign _171_ = x3[0] | ~(x0[0]);
  assign _172_ = x0[1] & ~(x3[1]);
  assign _173_ = _171_ & ~(_172_);
  assign _174_ = _173_ | _170_;
  assign _175_ = x0[2] & ~(x3[2]);
  assign _176_ = _174_ & ~(_175_);
  assign _177_ = _176_ | ~(_169_);
  assign _178_ = _168_ | ~(_177_);
  assign _179_ = x0[3] & ~(x3[3]);
  assign _180_ = _160_ | _154_;
  assign _181_ = ~(x3[0] ^ x2[0]);
  assign _182_ = ~(_181_ ^ _180_);
  assign _183_ = _182_ ^ _171_;
  assign _184_ = ~(_183_ | _172_);
  assign _185_ = ~(_184_ | _170_);
  assign _186_ = ~(_185_ & _169_);
  assign _187_ = _186_ & ~(_175_);
  assign _188_ = _179_ & ~(_187_);
  assign _189_ = _178_ & ~(_188_);
  assign _190_ = _189_ ^ _167_;
  assign _191_ = x1[3] & ~(x0[3]);
  assign _192_ = ~_191_;
  assign _193_ = x0[2] | ~(x1[2]);
  assign _194_ = x1[2] | ~(x0[2]);
  assign _195_ = x0[1] & ~(x1[1]);
  assign _196_ = _194_ & ~(_195_);
  assign _197_ = _193_ & ~(_196_);
  assign _198_ = _197_ | _192_;
  assign _199_ = x0[3] & ~(x1[3]);
  assign _200_ = x1[1] & ~(x0[1]);
  assign _201_ = _193_ & ~(_200_);
  assign _202_ = _194_ & ~(_201_);
  assign _203_ = _199_ & ~(_202_);
  assign _204_ = _198_ & ~(_203_);
  assign _205_ = ~(_204_ ^ _190_);
  assign _206_ = x0[3] | ~(x4[3]);
  assign _207_ = x0[2] | ~(x4[2]);
  assign _208_ = x4[2] | ~(x0[2]);
  assign _209_ = x4[1] & ~(x0[1]);
  assign _210_ = x4[0] | ~(x0[0]);
  assign _211_ = x0[1] & ~(x4[1]);
  assign _212_ = _210_ & ~(_211_);
  assign _213_ = ~(_212_ | _209_);
  assign _214_ = _208_ & ~(_213_);
  assign _215_ = _214_ | ~(_207_);
  assign _216_ = _215_ & ~(_206_);
  assign _217_ = x0[3] & ~(x4[3]);
  assign _218_ = x4[0] & ~(x0[0]);
  assign _219_ = _218_ & ~(_211_);
  assign _220_ = _219_ | _209_;
  assign _221_ = _207_ & ~(_220_);
  assign _222_ = _208_ & ~(_221_);
  assign _000_ = _217_ & ~(_222_);
  assign _001_ = ~(_000_ | _216_);
  assign _002_ = _153_ & _152_;
  assign _003_ = _149_ & ~(_158_);
  assign _004_ = _164_ & ~(_003_);
  assign _005_ = _004_ | _160_;
  assign _006_ = ~_154_;
  assign _007_ = _164_ & _158_;
  assign _008_ = _149_ & ~(_007_);
  assign _009_ = _006_ & ~(_008_);
  assign _010_ = _005_ & ~(_009_);
  assign _011_ = _008_ | _006_;
  assign _012_ = _160_ & ~(_004_);
  assign _013_ = _011_ & ~(_012_);
  assign _014_ = _002_ ? _013_ : _010_;
  assign _015_ = x2[0] ? _183_ : _171_;
  assign _016_ = ~_015_;
  assign _017_ = _016_ & ~(_014_);
  assign _018_ = _151_ & ~(_150_);
  assign _019_ = _008_ | _156_;
  assign _020_ = _162_ & ~(_004_);
  assign _021_ = _019_ & ~(_020_);
  assign _022_ = _008_ | ~(_156_);
  assign _023_ = ~(_004_ | _162_);
  assign _024_ = _022_ & ~(_023_);
  assign _025_ = _018_ ? _024_ : _021_;
  assign _026_ = _017_ & ~(_025_);
  assign _027_ = _018_ ? _021_ : _024_;
  assign _028_ = _017_ ? _025_ : _027_;
  assign _029_ = _169_ & ~(_175_);
  assign _030_ = ~_174_;
  assign _031_ = _177_ & ~(_179_);
  assign _032_ = _168_ & ~(_031_);
  assign _033_ = _032_ | _030_;
  assign _034_ = _168_ & ~(_177_);
  assign _035_ = ~(_034_ | _179_);
  assign _036_ = _185_ & ~(_035_);
  assign _037_ = _033_ & ~(_036_);
  assign _038_ = _035_ | _185_;
  assign _039_ = _030_ & ~(_032_);
  assign _040_ = _038_ & ~(_039_);
  assign _041_ = _029_ ? _040_ : _037_;
  assign _042_ = _028_ & ~(_041_);
  assign _043_ = _042_ | _026_;
  assign _044_ = ~(_194_ & _193_);
  assign _045_ = ~_200_;
  assign _046_ = _197_ & ~(_191_);
  assign _047_ = ~(_046_ | _199_);
  assign _048_ = _047_ | _045_;
  assign _049_ = ~(_199_ | _197_);
  assign _050_ = _192_ & ~(_049_);
  assign _051_ = _195_ & ~(_050_);
  assign _052_ = _048_ & ~(_051_);
  assign _053_ = _050_ | _195_;
  assign _054_ = _045_ & ~(_047_);
  assign _055_ = _053_ & ~(_054_);
  assign _056_ = _044_ ? _055_ : _052_;
  assign _057_ = _208_ & _207_;
  assign _058_ = _206_ & ~(_215_);
  assign _059_ = ~(_058_ | _217_);
  assign _060_ = _059_ | _220_;
  assign _061_ = ~_213_;
  assign _062_ = _215_ & ~(_217_);
  assign _063_ = _206_ & ~(_062_);
  assign _064_ = _061_ & ~(_063_);
  assign _065_ = _060_ & ~(_064_);
  assign _066_ = _063_ | _061_;
  assign _067_ = _220_ & ~(_059_);
  assign _068_ = _066_ & ~(_067_);
  assign _069_ = _057_ ? _068_ : _065_;
  assign _070_ = _069_ | _056_;
  assign _071_ = x3[0] ^ x2[0];
  assign _072_ = ~(_071_ ^ _181_);
  assign _073_ = ~(_211_ | _209_);
  assign _074_ = _059_ | _218_;
  assign _075_ = _210_ & ~(_063_);
  assign _076_ = _074_ & ~(_075_);
  assign _077_ = _063_ | _210_;
  assign _078_ = _218_ & ~(_059_);
  assign _079_ = _077_ & ~(_078_);
  assign _080_ = _073_ ? _079_ : _076_;
  assign _081_ = _080_ | ~(_072_);
  assign _082_ = _073_ ? _076_ : _079_;
  assign _083_ = _072_ & ~(_082_);
  assign _084_ = ~(x1[1] ^ x0[1]);
  assign _085_ = ~(_084_ | _083_);
  assign _086_ = _085_ | ~(_081_);
  assign _087_ = _044_ ? _052_ : _055_;
  assign _088_ = _057_ ? _065_ : _068_;
  assign _089_ = ~(_088_ | _087_);
  assign _090_ = _086_ & ~(_089_);
  assign _091_ = _070_ & ~(_090_);
  assign _092_ = _070_ & ~(_086_);
  assign _093_ = ~(_092_ | _089_);
  assign _094_ = _043_ ? _091_ : _093_;
  assign _095_ = ~(_094_ ^ _001_);
  assign _096_ = _095_ | _205_;
  assign _097_ = _029_ ? _037_ : _040_;
  assign _098_ = _028_ ? _041_ : _097_;
  assign _099_ = _070_ & ~(_089_);
  assign _100_ = ~(_099_ ^ _086_);
  assign _101_ = _100_ | ~(_098_);
  assign _102_ = _099_ ^ _086_;
  assign _103_ = _098_ ? _100_ : _102_;
  assign _104_ = _002_ ? _010_ : _013_;
  assign _105_ = _015_ ? _104_ : _014_;
  assign _106_ = x1[1] ^ x0[1];
  assign _107_ = _081_ & ~(_083_);
  assign _108_ = _107_ | _106_;
  assign _109_ = _085_ & _081_;
  assign _110_ = _108_ & ~(_109_);
  assign _111_ = ~(_110_ & _105_);
  assign _112_ = ~(x1[0] ^ x4[0]);
  assign _113_ = ~(_112_ | _071_);
  assign _114_ = ~(x1[0] & x0[0]);
  assign _115_ = x4[0] & ~(_114_);
  assign _116_ = _115_ | _113_;
  assign _117_ = x1[0] | x0[0];
  assign _118_ = _117_ | x4[0];
  assign _119_ = _118_ & ~(_116_);
  assign _120_ = ~(_110_ | _105_);
  assign _121_ = _119_ & ~(_120_);
  assign _122_ = _111_ & ~(_121_);
  assign _123_ = _103_ & ~(_122_);
  assign _124_ = _101_ & ~(_123_);
  assign _125_ = _094_ ^ _001_;
  assign _126_ = _205_ & ~(_125_);
  assign _127_ = _126_ | ~(_124_);
  assign _128_ = ~(_127_ & _096_);
  assign _129_ = ~(_189_ | _167_);
  assign _130_ = _190_ & ~(_204_);
  assign _131_ = ~(_130_ | _129_);
  assign _132_ = _043_ & ~(_091_);
  assign _133_ = _093_ | _043_;
  assign _134_ = _133_ & ~(_001_);
  assign _135_ = ~(_134_ | _132_);
  assign _136_ = _001_ & ~(_132_);
  assign _137_ = _133_ & ~(_136_);
  assign _138_ = _131_ ? _135_ : _137_;
  assign _139_ = _128_ & ~(_138_);
  assign _140_ = _096_ & ~(_124_);
  assign _141_ = _140_ | _126_;
  assign _142_ = _131_ ? _137_ : _135_;
  assign _143_ = _141_ & ~(_142_);
  assign \U0.po4  = _143_ | _139_;
  assign _144_ = _205_ ? _125_ : _095_;
  assign \U0.po3  = ~(_144_ ^ _124_);
  assign _145_ = _111_ & ~(_120_);
  assign \U0.po1  = _145_ ^ _119_;
  assign _146_ = _112_ & ~(_181_);
  assign \U0.U6.DUT1.k3  = _146_ | _113_;
  assign _147_ = _119_ | ~(_111_);
  assign _148_ = _147_ & ~(_120_);
  assign \U0.U5.new_n35  = _103_ ? _122_ : _148_;
  assign r = { \U0.po4 , \U0.po3 , \U0.U5.new_n35 , \U0.po1 , \U0.U6.DUT1.k3  };
endmodule
