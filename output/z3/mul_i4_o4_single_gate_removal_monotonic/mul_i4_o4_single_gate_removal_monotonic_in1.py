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
out0 = Bool('out0')
out3 = Bool('out3')
out2 = Bool('out2')
out1 = Bool('out1')
g0=And(in3,in1)
g1=And(in2,in1)
g2=And(in3,in0)
g3=And(in2,in0)
g4=Not(g1)
g5=Not(g2)
g6=And(g0,g3)
g7=Not(g3)
out0 = g3

g8=And(g4,g5)
g9=Not(g6)
out3 = g6

g10=And(g0,g7)
g11=Not(g8)
out2 = g10

g12=And(g9,g11)
out1 = g12


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
in3 = Bool('in3')
in2 = Bool('in2')
app_in1 = Bool('app_in1')
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
out0 = Bool('out0')
out3 = Bool('out3')
out2 = Bool('out2')
out1 = Bool('out1')


app_in1= True

g0=And(in3,app_in1)
g1=And(in2,app_in1)
g2=And(in3,in0)
g3=And(in2,in0)
g4=Not(g1)
g5=Not(g2)
g6=And(g0,g3)
g7=Not(g3)
out0 = g3

g8=And(g4,g5)
g9=Not(g6)
out3 = g6

g10=And(g0,g7)
g11=Not(g8)
out2 = g10

g12=And(g9,g11)
out1 = g12


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
with open('output/report/mul_i4_o4_single_gate_removal_monotonic/mul_i4_o4_single_gate_removal_monotonic_in1.csv', 'w') as f:
	csvwriter = csv.writer(f)
	header = ['field', 'value']
	csvwriter.writerow(['Experiment', 'qor-evaluation'])
	csvwriter.writerow(['WCE', stats['wce']])
	csvwriter.writerow(['Total Runtime', stats['sat_runtime'] + stats['unsat_runtime']])
	csvwriter.writerow(['SAT Runtime', stats['sat_runtime']])
	csvwriter.writerow(['UNSAT Runtime', stats['unsat_runtime']])
	csvwriter.writerow(['Number of SAT calls', stats['num_sats']])
	csvwriter.writerow(['Number of UNSAT calls', stats['num_unsats']])
