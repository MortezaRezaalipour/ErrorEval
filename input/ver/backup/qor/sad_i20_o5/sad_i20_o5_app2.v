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
  wire _223_;
  wire _224_;
  wire _225_;
  wire _226_;
  wire _227_;
  wire _228_;
  wire _229_;
  wire _230_;
  wire _231_;
  wire _232_;
  wire _233_;
  wire _234_;
  wire _235_;
  wire _236_;
  wire _237_;
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
  assign _163_ = x0[3] | ~(x2[3]);
  assign _165_ = x2[2] & ~(x0[2]);
  assign _166_ = x0[2] & ~(x2[2]);
  assign _167_ = x0[1] | ~(x2[1]);
  assign _168_ = x2[1] | ~(x0[1]);
  assign _169_ = x0[0] & ~(x2[0]);
  assign _170_ = _168_ & ~(_169_);
  assign _171_ = _167_ & ~(_170_);
  assign _172_ = ~(_171_ | _166_);
  assign _173_ = _172_ | _165_;
  assign _174_ = _173_ & ~(_163_);
  assign _175_ = x2[0] & ~(x0[0]);
  assign _176_ = _175_ & _168_;
  assign _177_ = _167_ & ~(_176_);
  assign _178_ = _177_ | _166_;
  assign _179_ = x2[3] | ~(x0[3]);
  assign _180_ = _179_ | _165_;
  assign _181_ = _178_ & ~(_180_);
  assign _182_ = ~(_181_ | _174_);
  assign _183_ = x0[3] | ~(x3[3]);
  assign _184_ = x0[2] | ~(x3[2]);
  assign _185_ = x3[1] & ~(x0[1]);
  assign _186_ = x3[0] | ~(x0[0]);
  assign _187_ = x0[1] & ~(x3[1]);
  assign _188_ = _186_ & ~(_187_);
  assign _189_ = _188_ | _185_;
  assign _190_ = x0[2] & ~(x3[2]);
  assign _191_ = _189_ & ~(_190_);
  assign _192_ = _191_ | ~(_184_);
  assign _193_ = _183_ | ~(_192_);
  assign _194_ = x0[3] & ~(x3[3]);
  assign _195_ = ~_186_;
  assign _196_ = _175_ | _169_;
  assign _197_ = ~(x3[0] ^ x2[0]);
  assign _198_ = _197_ ^ _196_;
  assign _199_ = _198_ ^ _195_;
  assign _200_ = ~(_199_ | _187_);
  assign _201_ = ~(_200_ | _185_);
  assign _202_ = ~(_201_ & _184_);
  assign _203_ = _202_ & ~(_190_);
  assign _204_ = _194_ & ~(_203_);
  assign _205_ = _193_ & ~(_204_);
  assign _206_ = _205_ ^ _182_;
  assign _207_ = x1[3] & ~(x0[3]);
  assign _208_ = ~_207_;
  assign _209_ = x0[2] | ~(x1[2]);
  assign _210_ = x1[2] | ~(x0[2]);
  assign _211_ = x0[1] & ~(x1[1]);
  assign _212_ = _210_ & ~(_211_);
  assign _213_ = _209_ & ~(_212_);
  assign _214_ = _213_ | _208_;
  assign _215_ = x0[3] & ~(x1[3]);
  assign _216_ = x1[1] & ~(x0[1]);
  assign _217_ = _209_ & ~(_216_);
  assign _218_ = _210_ & ~(_217_);
  assign _219_ = _215_ & ~(_218_);
  assign _220_ = _214_ & ~(_219_);
  assign _221_ = ~(_220_ ^ _206_);
  assign _222_ = x0[3] | ~(x4[3]);
  assign _223_ = x0[2] | ~(x4[2]);
  assign _224_ = x4[2] | ~(x0[2]);
  assign _225_ = x4[1] & ~(x0[1]);
  assign _226_ = x4[0] | ~(x0[0]);
  assign _227_ = x0[1] & ~(x4[1]);
  assign _228_ = _226_ & ~(_227_);
  assign _229_ = ~(_228_ | _225_);
  assign _230_ = _224_ & ~(_229_);
  assign _231_ = _230_ | ~(_223_);
  assign _232_ = _231_ & ~(_222_);
  assign _233_ = x0[3] & ~(x4[3]);
  assign _234_ = x4[0] & ~(x0[0]);
  assign _235_ = _234_ & ~(_227_);
  assign _236_ = _235_ | _225_;
  assign _237_ = _223_ & ~(_236_);
  assign _000_ = _224_ & ~(_237_);
  assign _001_ = _233_ & ~(_000_);
  assign _002_ = ~(_001_ | _232_);
  assign _003_ = _168_ & _167_;
  assign _004_ = _163_ & ~(_173_);
  assign _005_ = _179_ & ~(_004_);
  assign _006_ = ~(_005_ | _175_);
  assign _007_ = _179_ & _173_;
  assign _008_ = _163_ & ~(_007_);
  assign _009_ = ~(_008_ | _169_);
  assign _010_ = _009_ | _006_;
  assign _011_ = _169_ & ~(_008_);
  assign _012_ = _175_ & ~(_005_);
  assign _013_ = _012_ | _011_;
  assign _014_ = _003_ ? _013_ : _010_;
  assign _015_ = x2[0] ? _199_ : _186_;
  assign _016_ = _014_ & ~(_015_);
  assign _017_ = ~(_166_ | _165_);
  assign _018_ = _008_ | _171_;
  assign _019_ = _177_ & ~(_005_);
  assign _020_ = _018_ & ~(_019_);
  assign _021_ = _008_ | ~(_171_);
  assign _022_ = ~(_005_ | _177_);
  assign _023_ = _021_ & ~(_022_);
  assign _024_ = _017_ ? _023_ : _020_;
  assign _025_ = _016_ & ~(_024_);
  assign _026_ = _017_ ? _020_ : _023_;
  assign _027_ = _016_ ? _024_ : _026_;
  assign _028_ = _184_ & ~(_190_);
  assign _029_ = ~_189_;
  assign _030_ = _192_ & ~(_194_);
  assign _031_ = _183_ & ~(_030_);
  assign _032_ = _031_ | _029_;
  assign _033_ = _183_ & ~(_192_);
  assign _034_ = ~(_033_ | _194_);
  assign _035_ = _201_ & ~(_034_);
  assign _036_ = _032_ & ~(_035_);
  assign _037_ = _034_ | _201_;
  assign _038_ = _029_ & ~(_031_);
  assign _039_ = _037_ & ~(_038_);
  assign _040_ = _028_ ? _039_ : _036_;
  assign _041_ = _027_ & ~(_040_);
  assign _042_ = _041_ | _025_;
  assign _043_ = ~(_210_ & _209_);
  assign _044_ = ~_216_;
  assign _045_ = _213_ & ~(_207_);
  assign _046_ = ~(_045_ | _215_);
  assign _047_ = _046_ | _044_;
  assign _048_ = ~(_215_ | _213_);
  assign _049_ = _208_ & ~(_048_);
  assign _050_ = _211_ & ~(_049_);
  assign _051_ = _047_ & ~(_050_);
  assign _052_ = _049_ | _211_;
  assign _053_ = _044_ & ~(_046_);
  assign _054_ = _052_ & ~(_053_);
  assign _055_ = _043_ ? _054_ : _051_;
  assign _056_ = _224_ & _223_;
  assign _057_ = _222_ & ~(_231_);
  assign _058_ = ~(_057_ | _233_);
  assign _059_ = _058_ | _236_;
  assign _060_ = ~_229_;
  assign _061_ = _231_ & ~(_233_);
  assign _062_ = _222_ & ~(_061_);
  assign _063_ = _060_ & ~(_062_);
  assign _064_ = _059_ & ~(_063_);
  assign _065_ = _062_ | _060_;
  assign _066_ = _236_ & ~(_058_);
  assign _067_ = _065_ & ~(_066_);
  assign _068_ = _056_ ? _067_ : _064_;
  assign _069_ = _068_ | _055_;
  assign _070_ = _031_ | x3[0];
  assign _071_ = ~(_187_ | _185_);
  assign _072_ = ~_071_;
  assign _073_ = _071_ ? _070_ : _034_;
  assign _074_ = _073_ | ~(x0[0]);
  assign _075_ = _031_ | _195_;
  assign _076_ = ~x3[0];
  assign _077_ = _076_ & ~(_034_);
  assign _078_ = _075_ & ~(_077_);
  assign _079_ = _072_ & ~(_078_);
  assign _080_ = _074_ & ~(_079_);
  assign _081_ = _034_ | x0[0];
  assign _082_ = _081_ | _076_;
  assign _083_ = _071_ & ~(_082_);
  assign _084_ = _080_ & ~(_083_);
  assign _085_ = ~(_227_ | _225_);
  assign _086_ = _058_ | _234_;
  assign _087_ = _226_ & ~(_062_);
  assign _088_ = _086_ & ~(_087_);
  assign _089_ = _062_ | _226_;
  assign _090_ = _234_ & ~(_058_);
  assign _091_ = _089_ & ~(_090_);
  assign _092_ = _085_ ? _091_ : _088_;
  assign _093_ = _092_ | _084_;
  assign _094_ = x3[0] ^ x2[0];
  assign _095_ = ~(_094_ ^ _197_);
  assign _096_ = _095_ ^ _084_;
  assign _097_ = _085_ ? _088_ : _091_;
  assign _098_ = _096_ & ~(_097_);
  assign _099_ = ~(x1[1] ^ x0[1]);
  assign _100_ = ~(_099_ | _098_);
  assign _101_ = _100_ | ~(_093_);
  assign _102_ = _043_ ? _051_ : _054_;
  assign _103_ = _056_ ? _064_ : _067_;
  assign _104_ = ~(_103_ | _102_);
  assign _105_ = _101_ & ~(_104_);
  assign _106_ = _069_ & ~(_105_);
  assign _107_ = _069_ & ~(_101_);
  assign _108_ = ~(_107_ | _104_);
  assign _109_ = _042_ ? _106_ : _108_;
  assign _110_ = ~(_109_ ^ _002_);
  assign _111_ = _110_ | _221_;
  assign _112_ = _028_ ? _036_ : _039_;
  assign _113_ = _027_ ? _040_ : _112_;
  assign _114_ = _069_ & ~(_104_);
  assign _115_ = ~(_114_ ^ _101_);
  assign _116_ = _115_ | ~(_113_);
  assign _117_ = _114_ ^ _101_;
  assign _118_ = _113_ ? _115_ : _117_;
  assign _119_ = _003_ ? _010_ : _013_;
  assign _120_ = _015_ ? _119_ : _014_;
  assign _121_ = x1[1] ^ x0[1];
  assign _122_ = _093_ & ~(_098_);
  assign _123_ = _122_ | _121_;
  assign _124_ = _100_ & _093_;
  assign _125_ = _123_ & ~(_124_);
  assign _126_ = _120_ | ~(_125_);
  assign _127_ = ~(x1[0] ^ x4[0]);
  assign _128_ = ~(_127_ | _094_);
  assign _129_ = ~(x1[0] & x0[0]);
  assign _130_ = x4[0] & ~(_129_);
  assign _131_ = _130_ | _128_;
  assign _132_ = x1[0] | x0[0];
  assign _133_ = _132_ | x4[0];
  assign _134_ = _133_ & ~(_131_);
  assign _135_ = _120_ & ~(_125_);
  assign _136_ = _134_ & ~(_135_);
  assign _137_ = _126_ & ~(_136_);
  assign _138_ = _118_ & ~(_137_);
  assign _139_ = _116_ & ~(_138_);
  assign _140_ = _109_ ^ _002_;
  assign _141_ = _221_ & ~(_140_);
  assign _142_ = _141_ | ~(_139_);
  assign _143_ = ~(_142_ & _111_);
  assign _144_ = ~(_205_ | _182_);
  assign _145_ = _206_ & ~(_220_);
  assign _146_ = ~(_145_ | _144_);
  assign _147_ = _042_ & ~(_106_);
  assign _148_ = _108_ | _042_;
  assign _149_ = _148_ & ~(_002_);
  assign _150_ = ~(_149_ | _147_);
  assign _151_ = _002_ & ~(_147_);
  assign _152_ = _148_ & ~(_151_);
  assign _153_ = _146_ ? _150_ : _152_;
  assign _154_ = _143_ & ~(_153_);
  assign _155_ = _111_ & ~(_139_);
  assign _156_ = _155_ | _141_;
  assign _157_ = _146_ ? _152_ : _150_;
  assign _158_ = _156_ & ~(_157_);
  assign \U0.po4  = _158_ | _154_;
  assign _159_ = _221_ ? _140_ : _110_;
  assign \U0.po3  = ~(_159_ ^ _139_);
  assign _160_ = _126_ & ~(_135_);
  assign \U0.po1  = _160_ ^ _134_;
  assign _161_ = _127_ & ~(_197_);
  assign \U0.U6.DUT1.k3  = _161_ | _128_;
  assign _162_ = _134_ | ~(_126_);
  assign _164_ = _162_ & ~(_135_);
  assign \U0.U5.new_n35  = _118_ ? _137_ : _164_;
  assign r = { \U0.po4 , \U0.po3 , \U0.U5.new_n35 , \U0.po1 , \U0.U6.DUT1.k3  };
endmodule