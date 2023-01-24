from z3 import *
import sys
import time
import csv

def abs(x):
	return If(x >= 0, x, -x)

in8 = Bool('in8')
in7 = Bool('in7')
in6 = Bool('in6')
in5 = Bool('in5')
in4 = Bool('in4')
in3 = Bool('in3')
in2 = Bool('in2')
in1 = Bool('in1')
in0 = Bool('in0')

g0 = Bool('g0')
g1 = Bool('g1')
g2 = Bool('g2')
g3 = Bool('g3')
g4 = Bool('g4')
g5 = Bool('g5')
g6 = Bool('g6')
g7 = Bool('g7')
g8 = Bool('g8')
g9 = Bool('g9')
g10 = Bool('g10')
g11 = Bool('g11')
g12 = Bool('g12')
g14 = Bool('g14')
g13 = Bool('g13')
g15 = Bool('g15')
g17 = Bool('g17')
g18 = Bool('g18')
g16 = Bool('g16')
g20 = Bool('g20')
g19 = Bool('g19')
g21 = Bool('g21')
g22 = Bool('g22')
g24 = Bool('g24')
g23 = Bool('g23')
g27 = Bool('g27')
g26 = Bool('g26')
g25 = Bool('g25')
g28 = Bool('g28')
g31 = Bool('g31')
g29 = Bool('g29')
g30 = Bool('g30')
g33 = Bool('g33')
g34 = Bool('g34')
g32 = Bool('g32')
g37 = Bool('g37')
g36 = Bool('g36')
g35 = Bool('g35')
g38 = Bool('g38')
g39 = Bool('g39')
g40 = Bool('g40')
g41 = Bool('g41')
g42 = Bool('g42')
g43 = Bool('g43')
g44 = Bool('g44')
g45 = Bool('g45')
g46 = Bool('g46')
g48 = Bool('g48')
g47 = Bool('g47')
g49 = Bool('g49')
g51 = Bool('g51')
g50 = Bool('g50')
g53 = Bool('g53')
g54 = Bool('g54')
g52 = Bool('g52')
g56 = Bool('g56')
g57 = Bool('g57')
g55 = Bool('g55')
g59 = Bool('g59')
g58 = Bool('g58')
g61 = Bool('g61')
g60 = Bool('g60')
g63 = Bool('g63')
g64 = Bool('g64')
g62 = Bool('g62')
g66 = Bool('g66')
g65 = Bool('g65')
g68 = Bool('g68')
g69 = Bool('g69')
g67 = Bool('g67')
g72 = Bool('g72')
g71 = Bool('g71')
g70 = Bool('g70')
g76 = Bool('g76')
g75 = Bool('g75')
g74 = Bool('g74')
g73 = Bool('g73')
g81 = Bool('g81')
g80 = Bool('g80')
g78 = Bool('g78')
g79 = Bool('g79')
g77 = Bool('g77')
g86 = Bool('g86')
g85 = Bool('g85')
g83 = Bool('g83')
g84 = Bool('g84')
g82 = Bool('g82')
g87 = Bool('g87')
g91 = Bool('g91')
g90 = Bool('g90')
g89 = Bool('g89')
g88 = Bool('g88')
g92 = Bool('g92')
g95 = Bool('g95')
g93 = Bool('g93')
g94 = Bool('g94')
g99 = Bool('g99')
g96 = Bool('g96')
g97 = Bool('g97')
g98 = Bool('g98')
g100 = Bool('g100')
g101 = Bool('g101')
g102 = Bool('g102')
g103 = Bool('g103')
g104 = Bool('g104')
g106 = Bool('g106')
g105 = Bool('g105')
g107 = Bool('g107')
g108 = Bool('g108')
g111 = Bool('g111')
g110 = Bool('g110')
g109 = Bool('g109')
g113 = Bool('g113')
g112 = Bool('g112')
g114 = Bool('g114')
g115 = Bool('g115')
g116 = Bool('g116')
g118 = Bool('g118')
g117 = Bool('g117')
g121 = Bool('g121')
g120 = Bool('g120')
g119 = Bool('g119')
g123 = Bool('g123')
g122 = Bool('g122')
g125 = Bool('g125')
g126 = Bool('g126')
g124 = Bool('g124')
g127 = Bool('g127')
g128 = Bool('g128')
g130 = Bool('g130')
g129 = Bool('g129')
g132 = Bool('g132')
g131 = Bool('g131')
g133 = Bool('g133')
out0 = Bool('out0')
out1 = Bool('out1')
out2 = Bool('out2')
out3 = Bool('out3')
out4 = Bool('out4')
out5 = Bool('out5')









g0=Not(in8)
g1=Not(in7)
g2=Not(in6)
g3=And(in5,in2)
g4=And(in4,in2)
g5=And(in3,in2)
g6=And(in5,in1)
g7=And(in4,in1)
g8=And(in3,in1)
g9=And(in5,in0)
g10=And(in4,in0)
g11=And(in3,in0)
g12=Not(g4)
g14=Not(g5)
g13=And(in8,g5)
g15=Not(g6)
g17=Not(g7)
g18=And(g3,g7)
g16=Not(g7)
g20=Not(g8)
g19=And(in7,g8)
g21=Not(g9)
g22=Not(g10)
g24=Not(g11)
g23=And(in6,g11)
g27=And(g0,g14)
g26=Not(g13)
g25=Not(g13)
g28=And(g15,g12)
g31=Not(g18)
g29=And(g3,g16)
g30=Not(g18)
g33=Not(g19)
g34=And(g1,g20)
g32=Not(g19)
g37=And(g2,g24)
g36=Not(g23)
g35=Not(g23)
g38=Not(g27)
g39=Not(g28)
g40=Not(g29)
g41=Not(g34)
g42=Not(g37)
g43=And(g25,g38)
g44=And(g39,g31)
g45=And(g41,g33)
g46=And(g35,g42)
g48=Not(g43)
g47=And(g7,g43)
g49=Not(g44)
g51=Not(g45)
g50=And(g10,g45)
out0=g46
g53=Not(g47)
g54=And(g17,g48)
g52=Not(g47)
g56=Not(g50)
g57=And(g22,g51)
g55=Not(g50)
g59=Not(g54)
g58=And(g52,g26)
g61=Not(g57)
g60=And(g32,g55)
g63=Not(g58)
g64=And(g59,g53)
g62=And(g58,g49)
g66=And(g61,g56)
g65=Not(g60)
g68=And(g63,g44)
g69=Not(g64)
g67=Not(g62)
g72=Not(g66)
g71=And(g23,g66)
g70=And(g65,g64)
g76=And(g60,g69)
g75=And(g68,g29)
g74=Not(g68)
g73=Not(g68)
g81=And(g72,g36)
g80=Not(g71)
g78=Not(g70)
g79=Not(g71)
g77=Not(g70)
g86=Not(g76)
g85=Not(g75)
g83=And(g74,g40)
g84=Not(g75)
g82=And(g67,g73)
g87=Not(g81)
g91=And(g77,g86)
g90=And(g84,g30)
g89=Not(g83)
g88=Not(g82)
g92=And(g87,g80)
g95=And(g9,g91)
g93=And(g85,g89)
g94=Not(g91)
out1=g92
g99=Not(g95)
g96=Not(g93)
g97=And(g94,g21)
g98=Not(g95)
g100=Not(g97)
g101=And(g98,g78)
g102=And(g100,g99)
g103=And(g88,g101)
g104=Not(g101)
g106=Not(g102)
g105=And(g102,g71)
g107=Not(g103)
g108=And(g104,g82)
g111=And(g106,g79)
g110=Not(g105)
g109=Not(g105)
g113=Not(g108)
g112=Not(g108)
g114=Not(g111)
g115=And(g112,g107)
g116=And(g114,g109)
g118=Not(g115)
g117=And(g105,g115)
out2=g116
g121=And(g110,g118)
g120=Not(g117)
g119=Not(g117)
g123=Not(g121)
g122=And(g113,g120)
g125=Not(g122)
g126=And(g123,g119)
g124=And(g96,g122)
g127=Not(g124)
g128=And(g93,g125)
out3=g126
g130=Not(g128)
g129=Not(g128)
g132=And(g90,g130)
g131=And(g129,g127)
out4=g131
g133=Not(g132)
out5=g133

exact_out0=Int('exact_out0')
exact_out0=out0*1
exact_out1=Int('exact_out1')
exact_out1=out1*2
exact_out2=Int('exact_out2')
exact_out2=out2*4
exact_out3=Int('exact_out3')
exact_out3=out3*8
exact_out4=Int('exact_out4')
exact_out4=out4*16
exact_out5=Int('exact_out5')
exact_out5=out5*32
exact_out = Int('exact_out')
exact_out=exact_out0+exact_out1+exact_out2+exact_out3+exact_out4+exact_out5
results = []
f_exact = Function('f', IntSort(), IntSort())
s = Solver()
s.add(f_exact(exact_out) == exact_out)
s.push()
s.add(in0==False, in1==True, in2==False, in3==False, in4==True, in5==True, in6==True, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==False, in4==False, in5==False, in6==False, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==False, in4==False, in5==False, in6==True, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==True, in3==False, in4==False, in5==False, in6==False, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==False, in4==False, in5==True, in6==False, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==False, in3==False, in4==True, in5==False, in6==False, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==True, in3==True, in4==False, in5==False, in6==False, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==False, in4==False, in5==False, in6==True, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==True, in4==True, in5==False, in6==False, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==False, in4==True, in5==True, in6==True, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==True, in4==True, in5==False, in6==False, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==False, in4==False, in5==False, in6==False, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==False, in4==True, in5==False, in6==True, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==False, in4==False, in5==False, in6==False, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==False, in3==False, in4==True, in5==True, in6==False, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==False, in3==True, in4==False, in5==True, in6==True, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==False, in4==False, in5==True, in6==True, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==False, in4==True, in5==False, in6==True, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==False, in3==True, in4==False, in5==True, in6==True, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==True, in3==False, in4==False, in5==False, in6==True, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==True, in4==True, in5==True, in6==False, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==False, in4==False, in5==True, in6==False, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==True, in4==False, in5==True, in6==False, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==False, in4==False, in5==False, in6==True, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==True, in4==True, in5==False, in6==False, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==True, in4==True, in5==False, in6==False, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==False, in4==False, in5==True, in6==False, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==True, in4==True, in5==False, in6==True, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==False, in4==True, in5==True, in6==False, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==True, in4==False, in5==True, in6==False, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==False, in3==True, in4==True, in5==True, in6==False, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==True, in4==False, in5==False, in6==True, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==True, in4==False, in5==True, in6==False, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==False, in4==False, in5==True, in6==True, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==True, in3==False, in4==True, in5==True, in6==True, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==True, in4==False, in5==True, in6==True, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==False, in4==False, in5==False, in6==False, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==True, in4==False, in5==True, in6==True, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==False, in4==False, in5==True, in6==False, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==False, in4==False, in5==True, in6==False, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==False, in4==False, in5==True, in6==True, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==True, in4==False, in5==True, in6==False, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==False, in4==False, in5==True, in6==True, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==True, in3==True, in4==False, in5==False, in6==False, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==True, in4==True, in5==True, in6==True, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==True, in4==True, in5==True, in6==True, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==True, in4==True, in5==True, in6==False, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==False, in4==True, in5==True, in6==False, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==False, in4==True, in5==True, in6==False, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==True, in3==False, in4==False, in5==True, in6==True, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==False, in4==True, in5==True, in6==False, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==True, in3==False, in4==True, in5==True, in6==False, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==True, in4==False, in5==False, in6==True, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==True, in4==False, in5==True, in6==False, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==True, in3==False, in4==False, in5==False, in6==True, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==False, in4==False, in5==False, in6==True, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==True, in4==True, in5==False, in6==True, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==True, in3==True, in4==False, in5==True, in6==False, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==False, in4==False, in5==False, in6==False, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==False, in4==True, in5==True, in6==True, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==True, in4==True, in5==False, in6==False, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==True, in4==True, in5==False, in6==True, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==True, in3==True, in4==True, in5==True, in6==True, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==False, in4==True, in5==True, in6==False, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==True, in4==True, in5==False, in6==True, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==False, in4==True, in5==False, in6==True, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==False, in4==True, in5==False, in6==True, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==False, in4==True, in5==True, in6==False, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==False, in4==True, in5==False, in6==True, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==True, in4==True, in5==True, in6==True, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==False, in4==True, in5==False, in6==False, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==True, in3==False, in4==False, in5==True, in6==False, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==False, in4==True, in5==True, in6==False, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==False, in4==False, in5==True, in6==False, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==True, in4==True, in5==True, in6==False, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==True, in4==False, in5==False, in6==True, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==True, in4==False, in5==True, in6==False, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==True, in4==False, in5==False, in6==True, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==False, in3==False, in4==False, in5==True, in6==False, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==True, in4==False, in5==True, in6==False, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==True, in4==True, in5==False, in6==False, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==True, in4==True, in5==False, in6==False, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==False, in3==True, in4==True, in5==False, in6==False, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==True, in3==False, in4==False, in5==False, in6==False, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==False, in4==True, in5==False, in6==True, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==False, in4==True, in5==True, in6==False, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==True, in4==True, in5==False, in6==True, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==True, in4==True, in5==True, in6==False, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==True, in4==False, in5==True, in6==False, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==True, in4==True, in5==False, in6==False, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==True, in4==True, in5==True, in6==True, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==True, in4==True, in5==False, in6==False, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==True, in3==True, in4==True, in5==False, in6==True, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==False, in4==False, in5==True, in6==True, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==False, in4==True, in5==False, in6==False, in7==True, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==True, in3==False, in4==True, in5==False, in6==False, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==False, in4==False, in5==True, in6==True, in7==True, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==True, in4==False, in5==True, in6==False, in7==False, in8==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==False, in3==True, in4==True, in5==False, in6==False, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==True, in4==False, in5==False, in6==False, in7==False, in8==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

with open('test/z3/madd_i9_o6.txt', 'w') as f:
	for line in results:
		f.write(line)
		f.write('\n')
print(f'{results = }')