from z3 import *
import sys
import time
import csv

def z3_abs(x):
	return If(x >= 0, x, -x)

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
out0 = Bool('out0')
out1 = Bool('out1')
g0=Not(in3)
g1=Not(in2)
g2=Not(in1)
g3=Not(in0)
g4=And(in1,g0)
g5=And(in0,g1)
g6=And(in3,g2)
g7=And(in2,g3)
g8=Not(g5)
g9=Not(g5)
g10=Not(g7)
g11=Not(g7)
g12=And(g6,g8)
g13=And(g4,g10)
g14=And(g9,g11)
g15=Not(g12)
g16=Not(g13)
g17=Not(g14)
g18=And(g15,g16)
out0 = g17

g19=Not(g18)
out1 = g19


exact_out0=Int('exact_out0')
exact_out0=out0*1
exact_out1=Int('exact_out1')
exact_out1=out1*2
exact_out = Int('exact_out')
exact_out=exact_out0+exact_out1
in3 = Bool('in3')
app_in2 = Bool('app_in2')
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
out0 = Bool('out0')
out1 = Bool('out1')

app_in2= True


g0=Not(in3)
g1=Not(app_in2)
g2=Not(in1)
g3=Not(in0)
g4=And(in1,g0)
g5=And(in0,g1)
g6=And(in3,g2)
g7=And(app_in2,g3)
g8=Not(g5)
g9=Not(g5)
g10=Not(g7)
g11=Not(g7)
g12=And(g6,g8)
g13=And(g4,g10)
g14=And(g9,g11)
g15=Not(g12)
g16=Not(g13)
g17=Not(g14)
g18=And(g15,g16)
out0 = g17

g19=Not(g18)
out1 = g19


approx_out0=Int('approx_out0')
approx_out0=out0*1*2/2
approx_out1=Int('approx_out1')
approx_out1=out1*2*2/2
approx_out = Int('approx_out')
approx_out=approx_out0+approx_out1
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
		end_iteration = time.time()
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
with open('output/report/abs_diff_i4_o3_single_gate_removal_monotonic/abs_diff_i4_o3_single_gate_removal_monotonic_in2.csv', 'w') as f:
	csvwriter = csv.writer(f)
	header = ['field', 'value']
	csvwriter.writerow(['Experiment', 'qor-evaluation'])
	csvwriter.writerow(['WCE', stats['wce']])
	csvwriter.writerow(['Total Runtime', stats['sat_runtime'] + stats['unsat_runtime']])
	csvwriter.writerow(['SAT Runtime', stats['sat_runtime']])
	csvwriter.writerow(['UNSAT Runtime', stats['unsat_runtime']])
	csvwriter.writerow(['Number of SAT calls', stats['num_sats']])
	csvwriter.writerow(['Number of UNSAT calls', stats['num_unsats']])
