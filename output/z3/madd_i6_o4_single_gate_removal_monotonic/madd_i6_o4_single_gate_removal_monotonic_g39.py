from z3 import *
import sys
import time
import csv

def z3_abs(x):
	return If(x >= 0, x, -x)

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
out0 = Bool('out0')
out3 = Bool('out3')
out1 = Bool('out1')
out2 = Bool('out2')
g0=Not(in5)
g1=Not(in4)
g2=And(in3,in1)
g3=And(in2,in1)
g4=And(in3,in0)
g5=And(in2,in0)
g6=Not(g2)
g7=Not(g3)
g8=And(in5,g3)
g9=Not(g4)
g10=Not(g5)
g11=And(in4,g5)
g12=And(g0,g7)
g13=Not(g8)
g14=Not(g8)
g15=And(g1,g10)
g16=Not(g11)
g17=Not(g11)
g18=Not(g12)
g19=Not(g15)
g20=And(g14,g18)
g21=And(g17,g19)
g22=Not(g20)
g23=And(g4,g20)
out0 = g21

g24=And(g9,g22)
g25=Not(g23)
g26=Not(g23)
g27=Not(g24)
g28=And(g13,g25)
g29=And(g26,g27)
g30=And(g6,g28)
g31=Not(g28)
g32=Not(g29)
g33=And(g11,g29)
g34=Not(g30)
g35=And(g2,g31)
g36=And(g16,g32)
g37=Not(g33)
g38=Not(g33)
g39=Not(g35)
out3 = g35

g40=Not(g36)
g41=And(g34,g39)
g42=And(g38,g40)
g43=Not(g41)
out1 = g42

g44=And(g37,g43)
g45=Not(g44)
out2 = g45


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
app_g39 = Bool('app_g39')
g40 = Bool('g40')
g41 = Bool('g41')
g42 = Bool('g42')
g43 = Bool('g43')
g44 = Bool('g44')
g45 = Bool('g45')
out0 = Bool('out0')
out3 = Bool('out3')
out1 = Bool('out1')
out2 = Bool('out2')






g0=Not(in5)
g1=Not(in4)
g2=And(in3,in1)
g3=And(in2,in1)
g4=And(in3,in0)
g5=And(in2,in0)
g6=Not(g2)
g7=Not(g3)
g8=And(in5,g3)
g9=Not(g4)
g10=Not(g5)
g11=And(in4,g5)
g12=And(g0,g7)
g13=Not(g8)
g14=Not(g8)
g15=And(g1,g10)
g16=Not(g11)
g17=Not(g11)
g18=Not(g12)
g19=Not(g15)
g20=And(g14,g18)
g21=And(g17,g19)
g22=Not(g20)
g23=And(g4,g20)
out0 = g21

g24=And(g9,g22)
g25=Not(g23)
g26=Not(g23)
g27=Not(g24)
g28=And(g13,g25)
g29=And(g26,g27)
g30=And(g6,g28)
g31=Not(g28)
g32=Not(g29)
g33=And(g11,g29)
g34=Not(g30)
g35=And(g2,g31)
g36=And(g16,g32)
g37=Not(g33)
g38=Not(g33)
app_g39 = True
out3 = g35

g40=Not(g36)
g41=And(g34,app_g39)
g42=And(g38,g40)
g43=Not(g41)
out1 = g42

g44=And(g37,g43)
g45=Not(g44)
out2 = g45


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
with open('output/report/madd_i6_o4_single_gate_removal_monotonic/madd_i6_o4_single_gate_removal_monotonic_g39.csv', 'w') as f:
	csvwriter = csv.writer(f)
	header = ['field', 'value']
	csvwriter.writerow(['Experiment', 'qor-evaluation'])
	csvwriter.writerow(['WCE', stats['wce']])
	csvwriter.writerow(['Total Runtime', stats['sat_runtime'] + stats['unsat_runtime']])
	csvwriter.writerow(['SAT Runtime', stats['sat_runtime']])
	csvwriter.writerow(['UNSAT Runtime', stats['unsat_runtime']])
	csvwriter.writerow(['Number of SAT calls', stats['num_sats']])
	csvwriter.writerow(['Number of UNSAT calls', stats['num_unsats']])
