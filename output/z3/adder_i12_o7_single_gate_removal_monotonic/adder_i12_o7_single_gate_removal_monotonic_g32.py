from z3 import *
import sys
import time
import csv

def z3_abs(x):
	return If(x >= 0, x, -x)

in11 = Bool('in11')
in10 = Bool('in10')
in09 = Bool('in09')
in08 = Bool('in08')
in07 = Bool('in07')
in06 = Bool('in06')
in05 = Bool('in05')
in04 = Bool('in04')
in03 = Bool('in03')
in02 = Bool('in02')
in01 = Bool('in01')
in00 = Bool('in00')

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
out0 = Bool('out0')
out1 = Bool('out1')
out2 = Bool('out2')
out3 = Bool('out3')
out4 = Bool('out4')
out5 = Bool('out5')
out6 = Bool('out6')
g0=Not(in11)
g1=Not(in10)
g2=Not(in09)
g3=Not(in08)
g4=Not(in07)
g5=Not(in06)
g6=And(in11,in05)
g7=Not(in05)
g8=And(in10,in04)
g9=Not(in04)
g10=And(in09,in03)
g11=Not(in03)
g12=And(in08,in02)
g13=Not(in02)
g14=And(in07,in01)
g15=Not(in01)
g16=And(in06,in00)
g17=Not(in00)
g18=Not(g6)
g19=Not(g6)
g20=And(g0,g7)
g21=Not(g8)
g22=Not(g8)
g23=And(g1,g9)
g24=Not(g10)
g25=Not(g10)
g26=And(g2,g11)
g27=Not(g12)
g28=Not(g12)
g29=And(g3,g13)
g30=Not(g14)
g31=Not(g14)
g32=And(g4,g15)
g33=Not(g16)
g34=Not(g16)
g35=And(g5,g17)
g36=Not(g20)
g37=Not(g23)
g38=Not(g26)
g39=Not(g29)
g40=Not(g32)
g41=Not(g35)
g42=And(g19,g36)
g43=And(g22,g37)
g44=And(g25,g38)
g45=And(g28,g39)
g46=And(g31,g40)
g47=And(g34,g41)
g48=Not(g42)
g49=Not(g43)
g50=Not(g44)
g51=Not(g45)
g52=Not(g46)
g53=And(g16,g46)
out0 = g47

g54=And(g33,g52)
g55=Not(g53)
g56=Not(g53)
g57=Not(g54)
g58=And(g30,g55)
g59=And(g56,g57)
g60=And(g51,g58)
g61=Not(g58)
out1 = g59

g62=Not(g60)
g63=And(g45,g61)
g64=Not(g63)
g65=Not(g63)
g66=And(g27,g64)
g67=And(g62,g65)
g68=And(g50,g66)
g69=Not(g66)
out2 = g67

g70=Not(g68)
g71=And(g44,g69)
g72=Not(g71)
g73=Not(g71)
g74=And(g24,g72)
g75=And(g70,g73)
g76=And(g49,g74)
g77=Not(g74)
out3 = g75

g78=Not(g76)
g79=And(g43,g77)
g80=Not(g79)
g81=Not(g79)
g82=And(g21,g80)
g83=And(g78,g81)
g84=And(g48,g82)
g85=Not(g82)
out4 = g83

g86=Not(g84)
g87=And(g42,g85)
g88=Not(g87)
g89=Not(g87)
g90=And(g18,g88)
g91=And(g86,g89)
g92=Not(g90)
out5 = g91

out6 = g92


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
exact_out6=Int('exact_out6')
exact_out6=out6*64
exact_out = Int('exact_out')
exact_out=exact_out0+exact_out1+exact_out2+exact_out3+exact_out4+exact_out5+exact_out6
in11 = Bool('in11')
in10 = Bool('in10')
in09 = Bool('in09')
in08 = Bool('in08')
in07 = Bool('in07')
in06 = Bool('in06')
in05 = Bool('in05')
in04 = Bool('in04')
in03 = Bool('in03')
in02 = Bool('in02')
in01 = Bool('in01')
in00 = Bool('in00')

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
app_g32 = Bool('app_g32')
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
out0 = Bool('out0')
out1 = Bool('out1')
out2 = Bool('out2')
out3 = Bool('out3')
out4 = Bool('out4')
out5 = Bool('out5')
out6 = Bool('out6')












g0=Not(in11)
g1=Not(in10)
g2=Not(in09)
g3=Not(in08)
g4=Not(in07)
g5=Not(in06)
g6=And(in11,in05)
g7=Not(in05)
g8=And(in10,in04)
g9=Not(in04)
g10=And(in09,in03)
g11=Not(in03)
g12=And(in08,in02)
g13=Not(in02)
g14=And(in07,in01)
g15=Not(in01)
g16=And(in06,in00)
g17=Not(in00)
g18=Not(g6)
g19=Not(g6)
g20=And(g0,g7)
g21=Not(g8)
g22=Not(g8)
g23=And(g1,g9)
g24=Not(g10)
g25=Not(g10)
g26=And(g2,g11)
g27=Not(g12)
g28=Not(g12)
g29=And(g3,g13)
g30=Not(g14)
g31=Not(g14)
app_g32 = True
g33=Not(g16)
g34=Not(g16)
g35=And(g5,g17)
g36=Not(g20)
g37=Not(g23)
g38=Not(g26)
g39=Not(g29)
g40=Not(app_g32)
g41=Not(g35)
g42=And(g19,g36)
g43=And(g22,g37)
g44=And(g25,g38)
g45=And(g28,g39)
g46=And(g31,g40)
g47=And(g34,g41)
g48=Not(g42)
g49=Not(g43)
g50=Not(g44)
g51=Not(g45)
g52=Not(g46)
g53=And(g16,g46)
out0 = g47

g54=And(g33,g52)
g55=Not(g53)
g56=Not(g53)
g57=Not(g54)
g58=And(g30,g55)
g59=And(g56,g57)
g60=And(g51,g58)
g61=Not(g58)
out1 = g59

g62=Not(g60)
g63=And(g45,g61)
g64=Not(g63)
g65=Not(g63)
g66=And(g27,g64)
g67=And(g62,g65)
g68=And(g50,g66)
g69=Not(g66)
out2 = g67

g70=Not(g68)
g71=And(g44,g69)
g72=Not(g71)
g73=Not(g71)
g74=And(g24,g72)
g75=And(g70,g73)
g76=And(g49,g74)
g77=Not(g74)
out3 = g75

g78=Not(g76)
g79=And(g43,g77)
g80=Not(g79)
g81=Not(g79)
g82=And(g21,g80)
g83=And(g78,g81)
g84=And(g48,g82)
g85=Not(g82)
out4 = g83

g86=Not(g84)
g87=And(g42,g85)
g88=Not(g87)
g89=Not(g87)
g90=And(g18,g88)
g91=And(g86,g89)
g92=Not(g90)
out5 = g91

out6 = g92


approx_out0=Int('approx_out0')
approx_out0=out0*1*2/2
approx_out1=Int('approx_out1')
approx_out1=out1*2*2/2
approx_out2=Int('approx_out2')
approx_out2=out2*4*2/2
approx_out3=Int('approx_out3')
approx_out3=out3*8*2/2
approx_out4=Int('approx_out4')
approx_out4=out4*16*2/2
approx_out5=Int('approx_out5')
approx_out5=out5*32*2/2
approx_out6=Int('approx_out6')
approx_out6=out6*64*2/2
approx_out = Int('approx_out')
approx_out=approx_out0+approx_out1+approx_out2+approx_out3+approx_out4+approx_out5+approx_out6
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
with open('output/report/adder_i12_o7_single_gate_removal_monotonic/adder_i12_o7_single_gate_removal_monotonic_g32.csv', 'w') as f:
	csvwriter = csv.writer(f)
	header = ['field', 'value']
	csvwriter.writerow(['Experiment', 'qor-evaluation'])
	csvwriter.writerow(['WCE', stats['wce']])
	csvwriter.writerow(['Total Runtime', stats['sat_runtime'] + stats['unsat_runtime']])
	csvwriter.writerow(['SAT Runtime', stats['sat_runtime']])
	csvwriter.writerow(['UNSAT Runtime', stats['unsat_runtime']])
	csvwriter.writerow(['Number of SAT calls', stats['num_sats']])
	csvwriter.writerow(['Number of UNSAT calls', stats['num_unsats']])
