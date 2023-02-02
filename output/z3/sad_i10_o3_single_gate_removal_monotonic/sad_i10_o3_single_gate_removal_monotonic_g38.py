from z3 import *
import sys
import time
import csv

def z3_abs(x):
	return If(x >= 0, x, -x)

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
g117 = Bool('g117')
g118 = Bool('g118')
g119 = Bool('g119')
g120 = Bool('g120')
g121 = Bool('g121')
g122 = Bool('g122')
g123 = Bool('g123')
g124 = Bool('g124')
g125 = Bool('g125')
g126 = Bool('g126')
g127 = Bool('g127')
g128 = Bool('g128')
g129 = Bool('g129')
g130 = Bool('g130')
g131 = Bool('g131')
g132 = Bool('g132')
g133 = Bool('g133')
g134 = Bool('g134')
g135 = Bool('g135')
g136 = Bool('g136')
g137 = Bool('g137')
g138 = Bool('g138')
g139 = Bool('g139')
g140 = Bool('g140')
g141 = Bool('g141')
g142 = Bool('g142')
g143 = Bool('g143')
g144 = Bool('g144')
g145 = Bool('g145')
g146 = Bool('g146')
g147 = Bool('g147')
g148 = Bool('g148')
g149 = Bool('g149')
g150 = Bool('g150')
g151 = Bool('g151')
g152 = Bool('g152')
g153 = Bool('g153')
g154 = Bool('g154')
g155 = Bool('g155')
g156 = Bool('g156')
g157 = Bool('g157')
g158 = Bool('g158')
g159 = Bool('g159')
g160 = Bool('g160')
g161 = Bool('g161')
g162 = Bool('g162')
g163 = Bool('g163')
g164 = Bool('g164')
g165 = Bool('g165')
out0 = Bool('out0')
out1 = Bool('out1')
out2 = Bool('out2')
g0=Not(in09)
g1=Not(in08)
g2=Not(in07)
g3=Not(in06)
g4=Not(in05)
g5=Not(in04)
g6=Not(in04)
g7=Not(in03)
g8=And(in04,in02)
g9=Not(in02)
g10=Not(in02)
g11=Not(in01)
g12=Not(in01)
g13=Not(in01)
g14=Not(in01)
g15=Not(in00)
g16=Not(in00)
g17=Not(in00)
g18=Not(in00)
g19=Not(in00)
g20=And(in00,g1)
g21=And(in00,g3)
g22=And(in01,g4)
g23=And(in00,g5)
g24=And(in01,g7)
g25=Not(g8)
g26=Not(g8)
g27=And(in00,g9)
g28=And(g6,g10)
g29=And(in03,g13)
g30=And(in05,g14)
g31=And(in02,g16)
g32=And(in04,g17)
g33=And(in08,g18)
g34=And(in06,g19)
g35=Not(g20)
g36=Not(g20)
g37=Not(g21)
g38=Not(g21)
g39=Not(g23)
g40=And(in00,g25)
g41=Not(g27)
g42=Not(g28)
g43=Not(g28)
g44=Not(g31)
g45=Not(g32)
g46=Not(g33)
g47=Not(g33)
g48=Not(g34)
g49=Not(g34)
g50=And(g11,g35)
g51=And(g12,g37)
g52=And(g30,g39)
g53=Not(g40)
g54=And(g29,g41)
g55=And(g15,g42)
g56=And(g26,g43)
g57=And(g24,g44)
g58=And(g22,g45)
g59=And(in01,g46)
g60=And(g36,g47)
g61=And(in01,g48)
g62=And(g38,g49)
g63=Not(g50)
g64=Not(g51)
g65=Not(g52)
g66=Not(g54)
g67=Not(g55)
g68=Not(g56)
g69=Not(g57)
g70=Not(g58)
g71=Not(g59)
g72=Not(g60)
g73=Not(g61)
g74=Not(g62)
g75=And(g56,g62)
g76=And(in09,g63)
g77=And(in07,g64)
g78=And(g53,g67)
g79=And(g66,g69)
g80=And(g65,g70)
g81=And(g0,g71)
g82=And(g2,g73)
g83=And(g68,g74)
g84=Not(g75)
g85=Not(g75)
g86=Not(g76)
g87=Not(g77)
g88=Not(g78)
g89=Not(g79)
g90=And(g79,g80)
g91=Not(g80)
g92=Not(g81)
g93=Not(g82)
g94=Not(g83)
g95=And(g84,g88)
g96=Not(g90)
g97=And(g89,g91)
g98=And(g86,g92)
g99=And(g87,g93)
g100=And(g85,g94)
g101=Not(g95)
g102=Not(g97)
g103=Not(g97)
g104=Not(g98)
g105=Not(g99)
g106=And(g60,g100)
g107=Not(g100)
g108=And(g96,g103)
g109=Not(g106)
g110=And(g72,g107)
g111=And(g99,g108)
g112=Not(g108)
g113=Not(g110)
g114=Not(g110)
g115=Not(g111)
g116=Not(g111)
g117=And(g105,g112)
g118=And(g109,g114)
g119=And(g102,g115)
g120=Not(g117)
out0 = g118

g121=Not(g119)
g122=Not(g119)
g123=And(g116,g120)
g124=And(g95,g123)
g125=Not(g123)
g126=Not(g124)
g127=Not(g124)
g128=And(g101,g125)
g129=Not(g128)
g130=And(g127,g129)
g131=And(g98,g130)
g132=Not(g130)
g133=Not(g131)
g134=Not(g131)
g135=And(g104,g132)
g136=And(g126,g133)
g137=Not(g135)
g138=Not(g136)
g139=And(g119,g136)
g140=And(g122,g136)
g141=Not(g136)
g142=And(g134,g137)
g143=And(g121,g138)
g144=Not(g139)
g145=Not(g140)
g146=And(g119,g141)
g147=Not(g142)
g148=And(g110,g142)
g149=Not(g143)
g150=Not(g146)
g151=And(g113,g147)
g152=Not(g148)
g153=Not(g148)
g154=And(g144,g149)
g155=And(g145,g150)
g156=Not(g151)
g157=Not(g154)
g158=Not(g155)
g159=And(g153,g156)
g160=And(g148,g157)
g161=And(g152,g158)
out1 = g159

g162=Not(g160)
g163=Not(g161)
g164=And(g162,g163)
g165=Not(g164)
out2 = g165


exact_out0=Int('exact_out0')
exact_out0=out0*1
exact_out1=Int('exact_out1')
exact_out1=out1*2
exact_out2=Int('exact_out2')
exact_out2=out2*4
exact_out = Int('exact_out')
exact_out=exact_out0+exact_out1+exact_out2
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
app_g38 = Bool('app_g38')
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
g117 = Bool('g117')
g118 = Bool('g118')
g119 = Bool('g119')
g120 = Bool('g120')
g121 = Bool('g121')
g122 = Bool('g122')
g123 = Bool('g123')
g124 = Bool('g124')
g125 = Bool('g125')
g126 = Bool('g126')
g127 = Bool('g127')
g128 = Bool('g128')
g129 = Bool('g129')
g130 = Bool('g130')
g131 = Bool('g131')
g132 = Bool('g132')
g133 = Bool('g133')
g134 = Bool('g134')
g135 = Bool('g135')
g136 = Bool('g136')
g137 = Bool('g137')
g138 = Bool('g138')
g139 = Bool('g139')
g140 = Bool('g140')
g141 = Bool('g141')
g142 = Bool('g142')
g143 = Bool('g143')
g144 = Bool('g144')
g145 = Bool('g145')
g146 = Bool('g146')
g147 = Bool('g147')
g148 = Bool('g148')
g149 = Bool('g149')
g150 = Bool('g150')
g151 = Bool('g151')
g152 = Bool('g152')
g153 = Bool('g153')
g154 = Bool('g154')
g155 = Bool('g155')
g156 = Bool('g156')
g157 = Bool('g157')
g158 = Bool('g158')
g159 = Bool('g159')
g160 = Bool('g160')
g161 = Bool('g161')
g162 = Bool('g162')
g163 = Bool('g163')
g164 = Bool('g164')
g165 = Bool('g165')
out0 = Bool('out0')
out1 = Bool('out1')
out2 = Bool('out2')










g0=Not(in09)
g1=Not(in08)
g2=Not(in07)
g3=Not(in06)
g4=Not(in05)
g5=Not(in04)
g6=Not(in04)
g7=Not(in03)
g8=And(in04,in02)
g9=Not(in02)
g10=Not(in02)
g11=Not(in01)
g12=Not(in01)
g13=Not(in01)
g14=Not(in01)
g15=Not(in00)
g16=Not(in00)
g17=Not(in00)
g18=Not(in00)
g19=Not(in00)
g20=And(in00,g1)
g21=And(in00,g3)
g22=And(in01,g4)
g23=And(in00,g5)
g24=And(in01,g7)
g25=Not(g8)
g26=Not(g8)
g27=And(in00,g9)
g28=And(g6,g10)
g29=And(in03,g13)
g30=And(in05,g14)
g31=And(in02,g16)
g32=And(in04,g17)
g33=And(in08,g18)
g34=And(in06,g19)
g35=Not(g20)
g36=Not(g20)
g37=Not(g21)
app_g38 = True
g39=Not(g23)
g40=And(in00,g25)
g41=Not(g27)
g42=Not(g28)
g43=Not(g28)
g44=Not(g31)
g45=Not(g32)
g46=Not(g33)
g47=Not(g33)
g48=Not(g34)
g49=Not(g34)
g50=And(g11,g35)
g51=And(g12,g37)
g52=And(g30,g39)
g53=Not(g40)
g54=And(g29,g41)
g55=And(g15,g42)
g56=And(g26,g43)
g57=And(g24,g44)
g58=And(g22,g45)
g59=And(in01,g46)
g60=And(g36,g47)
g61=And(in01,g48)
g62=And(app_g38,g49)
g63=Not(g50)
g64=Not(g51)
g65=Not(g52)
g66=Not(g54)
g67=Not(g55)
g68=Not(g56)
g69=Not(g57)
g70=Not(g58)
g71=Not(g59)
g72=Not(g60)
g73=Not(g61)
g74=Not(g62)
g75=And(g56,g62)
g76=And(in09,g63)
g77=And(in07,g64)
g78=And(g53,g67)
g79=And(g66,g69)
g80=And(g65,g70)
g81=And(g0,g71)
g82=And(g2,g73)
g83=And(g68,g74)
g84=Not(g75)
g85=Not(g75)
g86=Not(g76)
g87=Not(g77)
g88=Not(g78)
g89=Not(g79)
g90=And(g79,g80)
g91=Not(g80)
g92=Not(g81)
g93=Not(g82)
g94=Not(g83)
g95=And(g84,g88)
g96=Not(g90)
g97=And(g89,g91)
g98=And(g86,g92)
g99=And(g87,g93)
g100=And(g85,g94)
g101=Not(g95)
g102=Not(g97)
g103=Not(g97)
g104=Not(g98)
g105=Not(g99)
g106=And(g60,g100)
g107=Not(g100)
g108=And(g96,g103)
g109=Not(g106)
g110=And(g72,g107)
g111=And(g99,g108)
g112=Not(g108)
g113=Not(g110)
g114=Not(g110)
g115=Not(g111)
g116=Not(g111)
g117=And(g105,g112)
g118=And(g109,g114)
g119=And(g102,g115)
g120=Not(g117)
out0 = g118

g121=Not(g119)
g122=Not(g119)
g123=And(g116,g120)
g124=And(g95,g123)
g125=Not(g123)
g126=Not(g124)
g127=Not(g124)
g128=And(g101,g125)
g129=Not(g128)
g130=And(g127,g129)
g131=And(g98,g130)
g132=Not(g130)
g133=Not(g131)
g134=Not(g131)
g135=And(g104,g132)
g136=And(g126,g133)
g137=Not(g135)
g138=Not(g136)
g139=And(g119,g136)
g140=And(g122,g136)
g141=Not(g136)
g142=And(g134,g137)
g143=And(g121,g138)
g144=Not(g139)
g145=Not(g140)
g146=And(g119,g141)
g147=Not(g142)
g148=And(g110,g142)
g149=Not(g143)
g150=Not(g146)
g151=And(g113,g147)
g152=Not(g148)
g153=Not(g148)
g154=And(g144,g149)
g155=And(g145,g150)
g156=Not(g151)
g157=Not(g154)
g158=Not(g155)
g159=And(g153,g156)
g160=And(g148,g157)
g161=And(g152,g158)
out1 = g159

g162=Not(g160)
g163=Not(g161)
g164=And(g162,g163)
g165=Not(g164)
out2 = g165


approx_out0=Int('approx_out0')
approx_out0=out0*1*2/2
approx_out1=Int('approx_out1')
approx_out1=out1*2*2/2
approx_out2=Int('approx_out2')
approx_out2=out2*4*2/2
approx_out = Int('approx_out')
approx_out=approx_out0+approx_out1+approx_out2
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
with open('output/report/sad_i10_o3_single_gate_removal_monotonic/sad_i10_o3_single_gate_removal_monotonic_g38.csv', 'w') as f:
	csvwriter = csv.writer(f)
	header = ['field', 'value']
	csvwriter.writerow(['Experiment', 'qor-evaluation'])
	csvwriter.writerow(['WCE', stats['wce']])
	csvwriter.writerow(['Total Runtime', stats['sat_runtime'] + stats['unsat_runtime']])
	csvwriter.writerow(['SAT Runtime', stats['sat_runtime']])
	csvwriter.writerow(['UNSAT Runtime', stats['unsat_runtime']])
	csvwriter.writerow(['Number of SAT calls', stats['num_sats']])
	csvwriter.writerow(['Number of UNSAT calls', stats['num_unsats']])
