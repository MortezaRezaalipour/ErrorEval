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
results = []
f_exact = Function('f', IntSort(), IntSort())
s = Solver()
s.add(f_exact(exact_out) == exact_out)
s.push()
s.add(in0==False, in1==False, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==False, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==False, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==False, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==False, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==False, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==False, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==True, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==True, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==False, in2==False, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==True, in1==True, in2==False, in3==True)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

s.push()
s.add(in0==False, in1==True, in2==False, in3==False)
sol = s.check()
m = s.model()
print(f'{m = }')
cur_result = m[f_exact].else_value().as_string()
results.append(cur_result)
s.pop()

with open('test/z3/abs_diff_i4_o3.txt', 'w') as f:
	for line in results:
		f.write(line)
		f.write('\n')
print(f'{results = }')