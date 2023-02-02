from z3 import *
import sys
import time
import csv

def z3_abs(x):
	return If(x >= 0, x, -x)

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
g13 = Bool('g13')
g14 = Bool('g14')
g15 = Bool('g15')
g16 = Bool('g16')
g17 = Bool('g17')
g18 = Bool('g18')
g19 = Bool('g19')
g20 = Bool('g20')
g21 = Bool('g21')
g22 = Bool('g22')
g23 = Bool('g23')
g24 = Bool('g24')
g25 = Bool('g25')
g26 = Bool('g26')
g27 = Bool('g27')
g28 = Bool('g28')
g29 = Bool('g29')
g30 = Bool('g30')
g31 = Bool('g31')
g32 = Bool('g32')
g33 = Bool('g33')
g34 = Bool('g34')
g35 = Bool('g35')
g36 = Bool('g36')
g37 = Bool('g37')
g38 = Bool('g38')
g39 = Bool('g39')
g40 = Bool('g40')
g41 = Bool('g41')
g42 = Bool('g42')
g43 = Bool('g43')
g44 = Bool('g44')
g45 = Bool('g45')
g46 = Bool('g46')
g47 = Bool('g47')
g48 = Bool('g48')
g49 = Bool('g49')
g50 = Bool('g50')
g51 = Bool('g51')
g52 = Bool('g52')
g53 = Bool('g53')
g54 = Bool('g54')
g55 = Bool('g55')
g56 = Bool('g56')
g57 = Bool('g57')
g58 = Bool('g58')
g59 = Bool('g59')
g60 = Bool('g60')
g61 = Bool('g61')
g62 = Bool('g62')
g63 = Bool('g63')
g64 = Bool('g64')
g65 = Bool('g65')
g66 = Bool('g66')
g67 = Bool('g67')
g68 = Bool('g68')
g69 = Bool('g69')
g70 = Bool('g70')
g71 = Bool('g71')
g72 = Bool('g72')
g73 = Bool('g73')
g74 = Bool('g74')
g75 = Bool('g75')
g76 = Bool('g76')
g77 = Bool('g77')
g78 = Bool('g78')
g79 = Bool('g79')
g80 = Bool('g80')
g81 = Bool('g81')
g82 = Bool('g82')
g83 = Bool('g83')
g84 = Bool('g84')
g85 = Bool('g85')
g86 = Bool('g86')
g87 = Bool('g87')
g88 = Bool('g88')
g89 = Bool('g89')
g90 = Bool('g90')
g91 = Bool('g91')
g92 = Bool('g92')
g93 = Bool('g93')
g94 = Bool('g94')
g95 = Bool('g95')
g96 = Bool('g96')
g97 = Bool('g97')
g98 = Bool('g98')
g99 = Bool('g99')
g100 = Bool('g100')
g101 = Bool('g101')
g102 = Bool('g102')
g103 = Bool('g103')
g104 = Bool('g104')
g105 = Bool('g105')
g106 = Bool('g106')
g107 = Bool('g107')
g108 = Bool('g108')
g109 = Bool('g109')
g110 = Bool('g110')
g111 = Bool('g111')
g112 = Bool('g112')
g113 = Bool('g113')
g114 = Bool('g114')
g115 = Bool('g115')
g116 = Bool('g116')
out0 = Bool('out0')
out3 = Bool('out3')
out2 = Bool('out2')
out1 = Bool('out1')
g0=Not(in7)
g1=Not(in6)
g2=Not(in5)
g3=Not(in4)
g4=Not(in3)
g5=Not(in2)
g6=Not(in1)
g7=Not(in0)
g8=And(in3,g0)
g9=And(in2,g1)
g10=And(in1,g2)
g11=And(in0,g3)
g12=And(in7,g4)
g13=And(in6,g5)
g14=And(in5,g6)
g15=And(in4,g7)
g16=Not(g8)
g17=Not(g8)
g18=Not(g9)
g19=Not(g9)
g20=Not(g9)
g21=Not(g10)
g22=Not(g10)
g23=Not(g10)
g24=Not(g11)
g25=Not(g11)
g26=Not(g11)
g27=Not(g12)
g28=Not(g12)
g29=Not(g13)
g30=Not(g13)
g31=Not(g13)
g32=Not(g14)
g33=Not(g14)
g34=Not(g14)
g35=Not(g15)
g36=Not(g15)
g37=And(g15,g21)
g38=And(g22,g25)
g39=And(g8,g29)
g40=And(g19,g30)
g41=And(g23,g34)
g42=And(g26,g36)
g43=Not(g37)
g44=Not(g38)
g45=Not(g40)
g46=Not(g41)
g47=Not(g42)
g48=And(g32,g43)
g49=And(g33,g44)
out0 = g47

g50=Not(g48)
g51=Not(g48)
g52=Not(g49)
g53=Not(g49)
g54=And(g18,g50)
g55=And(g20,g53)
g56=Not(g54)
g57=Not(g55)
g58=And(g39,g56)
g59=And(g31,g57)
g60=Not(g58)
g61=Not(g59)
g62=Not(g59)
g63=And(g28,g59)
g64=And(g12,g61)
g65=And(g16,g62)
g66=Not(g63)
g67=Not(g64)
g68=Not(g65)
g69=And(g17,g66)
g70=And(g60,g67)
g71=And(g27,g68)
g72=Not(g69)
g73=Not(g69)
g74=Not(g69)
g75=Not(g69)
g76=Not(g70)
g77=Not(g71)
g78=Not(g71)
g79=Not(g71)
g80=Not(g71)
g81=And(g48,g72)
g82=And(g51,g73)
g83=And(g15,g74)
g84=And(g35,g75)
out3 = g76

g85=And(g52,g77)
g86=And(g49,g78)
g87=And(g11,g79)
g88=And(g24,g80)
g89=Not(g81)
g90=Not(g82)
g91=Not(g83)
g92=Not(g84)
g93=Not(g85)
g94=Not(g86)
g95=Not(g87)
g96=Not(g88)
g97=And(g89,g93)
g98=And(g90,g94)
g99=And(g91,g95)
g100=And(g92,g96)
g101=Not(g97)
g102=Not(g98)
g103=Not(g99)
g104=Not(g100)
g105=And(g45,g101)
g106=And(g40,g102)
g107=And(g41,g103)
g108=And(g46,g104)
g109=Not(g105)
g110=Not(g106)
g111=Not(g107)
g112=Not(g108)
g113=And(g109,g110)
g114=And(g111,g112)
g115=Not(g113)
g116=Not(g114)
out2 = g115

out1 = g116


exact_out0=Int('exact_out0')
exact_out0=out0*1
exact_out1=Int('exact_out1')
exact_out1=out1*2
exact_out2=Int('exact_out2')
exact_out2=out2*4
exact_out3=Int('exact_out3')
exact_out3=out3*8
exact_out = Int('exact_out')
exact_out=exact_out0+exact_out1+exact_out2+exact_out3
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
g13 = Bool('g13')
g14 = Bool('g14')
g15 = Bool('g15')
g16 = Bool('g16')
g17 = Bool('g17')
g18 = Bool('g18')
g19 = Bool('g19')
g20 = Bool('g20')
g21 = Bool('g21')
g22 = Bool('g22')
g23 = Bool('g23')
g24 = Bool('g24')
g25 = Bool('g25')
g26 = Bool('g26')
g27 = Bool('g27')
g28 = Bool('g28')
g29 = Bool('g29')
g30 = Bool('g30')
g31 = Bool('g31')
g32 = Bool('g32')
g33 = Bool('g33')
g34 = Bool('g34')
g35 = Bool('g35')
g36 = Bool('g36')
g37 = Bool('g37')
g38 = Bool('g38')
g39 = Bool('g39')
g40 = Bool('g40')
g41 = Bool('g41')
g42 = Bool('g42')
g43 = Bool('g43')
g44 = Bool('g44')
g45 = Bool('g45')
g46 = Bool('g46')
g47 = Bool('g47')
g48 = Bool('g48')
g49 = Bool('g49')
g50 = Bool('g50')
g51 = Bool('g51')
g52 = Bool('g52')
g53 = Bool('g53')
g54 = Bool('g54')
g55 = Bool('g55')
g56 = Bool('g56')
g57 = Bool('g57')
g58 = Bool('g58')
g59 = Bool('g59')
g60 = Bool('g60')
g61 = Bool('g61')
g62 = Bool('g62')
g63 = Bool('g63')
g64 = Bool('g64')
g65 = Bool('g65')
g66 = Bool('g66')
g67 = Bool('g67')
g68 = Bool('g68')
g69 = Bool('g69')
g70 = Bool('g70')
g71 = Bool('g71')
g72 = Bool('g72')
g73 = Bool('g73')
g74 = Bool('g74')
g75 = Bool('g75')
g76 = Bool('g76')
g77 = Bool('g77')
g78 = Bool('g78')
g79 = Bool('g79')
g80 = Bool('g80')
g81 = Bool('g81')
g82 = Bool('g82')
g83 = Bool('g83')
g84 = Bool('g84')
g85 = Bool('g85')
g86 = Bool('g86')
g87 = Bool('g87')
g88 = Bool('g88')
g89 = Bool('g89')
g90 = Bool('g90')
g91 = Bool('g91')
g92 = Bool('g92')
g93 = Bool('g93')
g94 = Bool('g94')
g95 = Bool('g95')
g96 = Bool('g96')
g97 = Bool('g97')
g98 = Bool('g98')
g99 = Bool('g99')
g100 = Bool('g100')
g101 = Bool('g101')
g102 = Bool('g102')
app_g103 = Bool('app_g103')
g104 = Bool('g104')
g105 = Bool('g105')
g106 = Bool('g106')
g107 = Bool('g107')
g108 = Bool('g108')
g109 = Bool('g109')
g110 = Bool('g110')
g111 = Bool('g111')
g112 = Bool('g112')
g113 = Bool('g113')
g114 = Bool('g114')
g115 = Bool('g115')
g116 = Bool('g116')
out0 = Bool('out0')
out3 = Bool('out3')
out2 = Bool('out2')
out1 = Bool('out1')








g0=Not(in7)
g1=Not(in6)
g2=Not(in5)
g3=Not(in4)
g4=Not(in3)
g5=Not(in2)
g6=Not(in1)
g7=Not(in0)
g8=And(in3,g0)
g9=And(in2,g1)
g10=And(in1,g2)
g11=And(in0,g3)
g12=And(in7,g4)
g13=And(in6,g5)
g14=And(in5,g6)
g15=And(in4,g7)
g16=Not(g8)
g17=Not(g8)
g18=Not(g9)
g19=Not(g9)
g20=Not(g9)
g21=Not(g10)
g22=Not(g10)
g23=Not(g10)
g24=Not(g11)
g25=Not(g11)
g26=Not(g11)
g27=Not(g12)
g28=Not(g12)
g29=Not(g13)
g30=Not(g13)
g31=Not(g13)
g32=Not(g14)
g33=Not(g14)
g34=Not(g14)
g35=Not(g15)
g36=Not(g15)
g37=And(g15,g21)
g38=And(g22,g25)
g39=And(g8,g29)
g40=And(g19,g30)
g41=And(g23,g34)
g42=And(g26,g36)
g43=Not(g37)
g44=Not(g38)
g45=Not(g40)
g46=Not(g41)
g47=Not(g42)
g48=And(g32,g43)
g49=And(g33,g44)
out0 = g47

g50=Not(g48)
g51=Not(g48)
g52=Not(g49)
g53=Not(g49)
g54=And(g18,g50)
g55=And(g20,g53)
g56=Not(g54)
g57=Not(g55)
g58=And(g39,g56)
g59=And(g31,g57)
g60=Not(g58)
g61=Not(g59)
g62=Not(g59)
g63=And(g28,g59)
g64=And(g12,g61)
g65=And(g16,g62)
g66=Not(g63)
g67=Not(g64)
g68=Not(g65)
g69=And(g17,g66)
g70=And(g60,g67)
g71=And(g27,g68)
g72=Not(g69)
g73=Not(g69)
g74=Not(g69)
g75=Not(g69)
g76=Not(g70)
g77=Not(g71)
g78=Not(g71)
g79=Not(g71)
g80=Not(g71)
g81=And(g48,g72)
g82=And(g51,g73)
g83=And(g15,g74)
g84=And(g35,g75)
out3 = g76

g85=And(g52,g77)
g86=And(g49,g78)
g87=And(g11,g79)
g88=And(g24,g80)
g89=Not(g81)
g90=Not(g82)
g91=Not(g83)
g92=Not(g84)
g93=Not(g85)
g94=Not(g86)
g95=Not(g87)
g96=Not(g88)
g97=And(g89,g93)
g98=And(g90,g94)
g99=And(g91,g95)
g100=And(g92,g96)
g101=Not(g97)
g102=Not(g98)
app_g103 = True
g104=Not(g100)
g105=And(g45,g101)
g106=And(g40,g102)
g107=And(g41,app_g103)
g108=And(g46,g104)
g109=Not(g105)
g110=Not(g106)
g111=Not(g107)
g112=Not(g108)
g113=And(g109,g110)
g114=And(g111,g112)
g115=Not(g113)
g116=Not(g114)
out2 = g115

out1 = g116


approx_out0=Int('approx_out0')
approx_out0=out0*1*2/2
approx_out1=Int('approx_out1')
approx_out1=out1*2*2/2
approx_out2=Int('approx_out2')
approx_out2=out2*4*2/2
approx_out3=Int('approx_out3')
approx_out3=out3*8*2/2
approx_out = Int('approx_out')
approx_out=approx_out0+approx_out1+approx_out2+approx_out3
f_exact = Function('f_exact', IntSort(), IntSort())
f_approx = Function('f_approx', IntSort(), IntSort())
f_error = Function('f_error', IntSort(), IntSort(), IntSort())

foundWCE = False
stats: dict = {}
stats['wce'] = 0
stats['et'] = 0
stats['num_sats'] = 0
stats['num_unsats'] = 0
stats['sat_runtime'] = 0.0
stats['unsat_runtime'] = 0.0
stats['jumps'] = []
start_whole = time.time()
s = Solver()
stats['jumps'].append(stats['et'])
while(not foundWCE):
	start_iteration = time.time()
	s.push()
	s.add(f_exact(exact_out) == exact_out)
	s.add(f_approx(approx_out) == approx_out)
	s.add(f_error(exact_out, approx_out) == exact_out - approx_out)
	s.add(z3_abs(f_error(exact_out, approx_out)) > stats['et'])
	response = s.check()
	if response == sat:
		print(f'sat')
		returned_model = s.model()
		print(f'{returned_model = }')
		print(f"{returned_model[f_exact].else_value() = }")
		print(f"{returned_model[f_approx].else_value() = }")
		print(f"{returned_model[f_error].else_value() = }")
		returned_value = abs(int(returned_model[f_error].else_value().as_long()))
		returned_value_reval = abs(int(returned_model.evaluate(f_error(exact_out, approx_out)).as_long()))
		if returned_value == returned_value_reval:
			print(f'double-check is passed!')
		else:
			print(f'ERROR!!! double-check failed! exiting...')
			exit()
		end_iteration = time.time()
		stats['et'] = returned_value
		stats['num_sats'] += 1
		stats['sat_runtime'] += (end_iteration - start_iteration)
		stats['jumps'].append(returned_value)

	if response == unsat:
		print('unsat')
		end_iteration = time.time()
		foundWCE = True
		stats['num_unsats'] += 1
		stats['unsat_runtime'] += (end_iteration - start_iteration)
		stats['wce'] = stats['et']
end_whole = time.time()
with open('output/report/abs_diff_i8_o5_single_gate_removal_monotonic/abs_diff_i8_o5_single_gate_removal_monotonic_g103.csv', 'w') as f:
	csvwriter = csv.writer(f)
	header = ['field', 'value']
	csvwriter.writerow(['Experiment', 'qor-evaluation'])
	csvwriter.writerow(['WCE', stats['wce']])
	csvwriter.writerow(['Total Runtime', stats['sat_runtime'] + stats['unsat_runtime']])
	csvwriter.writerow(['SAT Runtime', stats['sat_runtime']])
	csvwriter.writerow(['UNSAT Runtime', stats['unsat_runtime']])
	csvwriter.writerow(['Number of SAT calls', stats['num_sats']])
	csvwriter.writerow(['Number of UNSAT calls', stats['num_unsats']])
