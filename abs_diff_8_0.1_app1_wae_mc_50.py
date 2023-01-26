from z3 import *
import sys

import time
import os
### This is circuit abs_diff_8_0.1

def abs(x):
	return If(x >= 0,x,-x)

# Boolean variables declaration for the exact circuit, list of gates (included primary inputs)
i0 = Bool('i0')
i1 = Bool('i1')
i2 = Bool('i2')
i3 = Bool('i3')
i4 = Bool('i4')
i5 = Bool('i5')
i6 = Bool('i6')
i7 = Bool('i7')
i8 = Bool('i8')
i9 = Bool('i9')
i10 = Bool('i10')
i11 = Bool('i11')
i12 = Bool('i12')
i13 = Bool('i13')
i14 = Bool('i14')
i15 = Bool('i15')
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

# Exact circuit: edges and node types (logic functions) description
g16 = False
g17 = Not(i15)
g18 = Not(i14)
g19 = Not(i12)
g20 = Not(i8)
g21 = And(i7,g17)
g22 = Not(i7)
g23 = And(i15,g22)
g24 = Or(g21,g23)
g25 = And(i6,g18)
g26 = Not(i6)
g27 = And(i14,g26)
g28 = Or(g23,g27)
g29 = Or(g25,g28)
g30 = Or(g24,g29)
g31 = Or(g25,g27)
g32 = And(g23,g31)
g33 = Not(g32)
g34 = And(g29,g33)
g35 = Not(g34)
g36 = Or(i14,g26)
g37 = And(g28,g36)
g38 = Not(g37)
g39 = Not(i5)
g40 = Or(i13,g39)
g41 = And(g38,g40)
g42 = And(g37,g40)
g43 = Not(g42)
g44 = And(i13,g39)
g45 = Or(g37,g44)
g46 = And(g40,g45)
g47 = Or(i12,g46)
g48 = And(i12,g46)
g49 = Not(g44)
g50 = And(g41,g49)
g51 = And(g40,g49)
g52 = Not(g51)
g53 = And(g37,g52)
g54 = Or(g50,g53)
g55 = Not(g54)
g56 = Or(g30,g55)
g57 = And(g43,g49)
g58 = And(i4,g19)
g59 = Not(i4)
g60 = And(g47,g59)
g61 = Or(g48,g60)
g62 = And(i12,g59)
g63 = Or(g58,g62)
g64 = And(g57,g63)
g65 = Not(g63)
g66 = And(g46,g65)
g67 = Or(g64,g66)
g68 = Or(g56,g67)
g69 = Not(i3)
g70 = Or(i11,g69)
g71 = And(g61,g70)
g72 = And(i11,g69)
g73 = Or(g61,g72)
g74 = And(g70,g73)
g75 = Not(g74)
g76 = Not(g72)
g77 = And(g71,g76)
g78 = And(g70,g76)
g79 = Or(g61,g78)
g80 = Not(g79)
g81 = Or(g77,g80)
g82 = Or(g68,g81)
g83 = Not(i2)
g84 = Or(i10,g83)
g85 = And(g74,g84)
g86 = And(i10,g83)
g87 = Or(g85,g86)
g88 = Not(g86)
g89 = And(g84,g88)
g90 = And(g75,g89)
g91 = Not(g89)
g92 = And(g74,g91)
g93 = Or(g90,g92)
g94 = Not(g93)
g95 = Or(g82,g94)
g96 = Not(i1)
g97 = Or(i9,g96)
g98 = And(g87,g97)
g99 = And(i9,g96)
g100 = Or(g98,g99)
g101 = Not(g99)
g102 = And(g98,g101)
g103 = And(g97,g101)
g104 = Or(g87,g103)
g105 = Not(g104)
g106 = Or(g102,g105)
g107 = Or(g95,g106)
g108 = Or(i0,g100)
g109 = And(g20,g108)
g110 = And(i0,g100)
g111 = Or(g109,g110)
g112 = And(g24,g111)
g113 = And(g35,g112)
g114 = Not(g112)
g115 = And(g34,g114)
g116 = Or(g113,g115)
g117 = And(g30,g111)
g118 = And(g54,g117)
g119 = Not(g117)
g120 = And(g55,g119)
g121 = Or(g118,g120)
g122 = And(g56,g111)
g123 = Or(g67,g122)
g124 = And(g67,g111)
g125 = And(g56,g124)
g126 = Not(g125)
g127 = And(g123,g126)
g128 = And(g68,g111)
g129 = And(g81,g128)
g130 = Not(g129)
g131 = Or(g81,g128)
g132 = And(g130,g131)
g133 = And(g82,g111)
g134 = Or(g94,g133)
g135 = And(g94,g133)
g136 = Not(g135)
g137 = And(g134,g136)
g138 = And(g95,g111)
g139 = And(g106,g138)
g140 = Not(g139)
g141 = Or(g106,g138)
g142 = And(g140,g141)
g143 = And(g107,g111)
g144 = Or(g100,g143)
g145 = Not(g144)
g146 = And(g100,g143)
g147 = Or(g145,g146)
g148 = And(i0,g20)
g149 = Not(i0)
g150 = And(i8,g149)
g151 = Or(g148,g150)
g152 = And(g147,g151)

# Primary output vector, i.e. list of gate indexes corresponding to each primary output, starting from the LSB
out_vec = [16,152,142,137,132,127,121,116,24]

# Declaration of integer variables for the weights of each primaty output bit, followed by the weight assignment
w_exa_o0 = Int('w_exa_o0')
w_exa_o0 = g16* 2/2
w_exa_o1 = Int('w_exa_o1')
w_exa_o1 = g152*2
w_exa_o2 = Int('w_exa_o2')
w_exa_o2 = g142*4
w_exa_o3 = Int('w_exa_o3')
w_exa_o3 = g137*8
w_exa_o4 = Int('w_exa_o4')
w_exa_o4 = g132*16
w_exa_o5 = Int('w_exa_o5')
w_exa_o5 = g127*32
w_exa_o6 = Int('w_exa_o6')
w_exa_o6 = g121*64
w_exa_o7 = Int('w_exa_o7')
w_exa_o7 = g116*128
w_exa_o8 = Int('w_exa_o8')
w_exa_o8 = g24*256

# Definition and expression of the integer value of the output for the exact circuit
int_exa_out = Int('int_exa_out')
int_exa_out = w_exa_o0 + w_exa_o1 + w_exa_o2 + w_exa_o3 + w_exa_o4 + w_exa_o5 + w_exa_o6 + w_exa_o7 + w_exa_o8
### This is circuit the approximate part gv/abs_diff_8_0.1_app1.gv
# Boolean variables declaration for the approximate circuit
i0 = Bool('i0')
i1 = Bool('i1')
i2 = Bool('i2')
i3 = Bool('i3')
i4 = Bool('i4')
i5 = Bool('i5')
i6 = Bool('i6')
i7 = Bool('i7')
i8 = Bool('i8')
i9 = Bool('i9')
i10 = Bool('i10')
i11 = Bool('i11')
i12 = Bool('i12')
i13 = Bool('i13')
i14 = Bool('i14')
i15 = Bool('i15')
a16 = Bool('a16')
a17 = Bool('a17')
a18 = Bool('a18')
a19 = Bool('a19')
a20 = Bool('a20')
a21 = Bool('a21')
a22 = Bool('a22')
a23 = Bool('a23')
a24 = Bool('a24')
a25 = Bool('a25')
a26 = Bool('a26')
a27 = Bool('a27')
a28 = Bool('a28')
a29 = Bool('a29')
a30 = Bool('a30')
a31 = Bool('a31')
a32 = Bool('a32')
a33 = Bool('a33')
a34 = Bool('a34')
a35 = Bool('a35')
a36 = Bool('a36')
a37 = Bool('a37')
a38 = Bool('a38')
a39 = Bool('a39')
a40 = Bool('a40')
a41 = Bool('a41')
a42 = Bool('a42')
a43 = Bool('a43')
a44 = Bool('a44')
a45 = Bool('a45')
a46 = Bool('a46')
a47 = Bool('a47')
a48 = Bool('a48')
a49 = Bool('a49')
a50 = Bool('a50')
a51 = Bool('a51')
a52 = Bool('a52')
a53 = Bool('a53')
a54 = Bool('a54')
a55 = Bool('a55')
a56 = Bool('a56')
a57 = Bool('a57')
a58 = Bool('a58')
a59 = Bool('a59')
a60 = Bool('a60')
a61 = Bool('a61')
a62 = Bool('a62')
a63 = Bool('a63')
a64 = Bool('a64')
a65 = Bool('a65')
a66 = Bool('a66')
a67 = Bool('a67')
a68 = Bool('a68')
a69 = Bool('a69')
a70 = Bool('a70')
a71 = Bool('a71')
a72 = Bool('a72')
a73 = Bool('a73')
a74 = Bool('a74')
a75 = Bool('a75')
a76 = Bool('a76')
a77 = Bool('a77')
a78 = Bool('a78')
a79 = Bool('a79')
a80 = Bool('a80')
a81 = Bool('a81')
a82 = Bool('a82')
a83 = Bool('a83')
a84 = Bool('a84')
a85 = Bool('a85')
a86 = Bool('a86')
a87 = Bool('a87')
a88 = Bool('a88')
a89 = Bool('a89')
a90 = Bool('a90')
a91 = Bool('a91')
a92 = Bool('a92')
a93 = Bool('a93')
a94 = Bool('a94')
a95 = Bool('a95')
a96 = Bool('a96')
a97 = Bool('a97')
a98 = Bool('a98')
a99 = Bool('a99')
a100 = Bool('a100')
a101 = Bool('a101')
a102 = Bool('a102')
a103 = Bool('a103')
a104 = Bool('a104')
a105 = Bool('a105')
a106 = Bool('a106')
a107 = Bool('a107')
a108 = Bool('a108')
a109 = Bool('a109')
a110 = Bool('a110')
a111 = Bool('a111')
a112 = Bool('a112')
a113 = Bool('a113')
a114 = Bool('a114')
a115 = Bool('a115')
a116 = Bool('a116')
a117 = Bool('a117')
a118 = Bool('a118')
a119 = Bool('a119')
a120 = Bool('a120')
a121 = Bool('a121')
a122 = Bool('a122')
a123 = Bool('a123')
a124 = Bool('a124')
a125 = Bool('a125')
a126 = Bool('a126')
a127 = Bool('a127')
a128 = Bool('a128')
a129 = Bool('a129')
a130 = Bool('a130')
a131 = Bool('a131')
a132 = Bool('a132')
a133 = Bool('a133')
a134 = Bool('a134')
a135 = Bool('a135')
a136 = Bool('a136')
a137 = Bool('a137')
a138 = Bool('a138')
a139 = Bool('a139')
a140 = Bool('a140')
a141 = Bool('a141')
a142 = Bool('a142')
a143 = Bool('a143')
a144 = Bool('a144')
a145 = Bool('a145')
a146 = Bool('a146')
a147 = Bool('a147')

# Approximate circuit: edges and node types (logic functions) description
a16 = False
a17 = Not(i14)
a18 = Not(i11)
a19 = Not(i10)
a20 = Not(i9)
a21 = Not(i8)
a22 = Not(i7)
a23 = And(i15,a22)
a24 = And(i14,a23)
a25 = Or(i14,a23)
a26 = Not(a23)
a27 = Or(i15,a22)
a28 = And(a26,a27)
a29 = Not(a28)
a30 = And(i6,a17)
a31 = Not(i6)
a32 = And(i14,a31)
a33 = Or(a30,a32)
a34 = Not(a33)
a35 = And(a28,a34)
a36 = Or(a24,a31)
a37 = And(a25,a36)
a38 = Not(i5)
a39 = And(i13,a38)
a40 = Or(a37,a39)
a41 = Not(a40)
a42 = Or(i13,a38)
a43 = And(a40,a42)
a44 = And(a41,a42)
a45 = Not(a42)
a46 = Or(a39,a45)
a47 = And(a37,a46)
a48 = Or(a44,a47)
a49 = Not(a48)
a50 = Not(i4)
a51 = Or(i12,a50)
a52 = And(a48,a51)
a53 = And(a43,a51)
a54 = And(i12,a50)
a55 = Or(a43,a54)
a56 = And(a51,a55)
a57 = Not(a55)
a58 = And(a35,a57)
a59 = And(a52,a58)
a60 = Or(a53,a54)
a61 = And(i3,a18)
a62 = Not(i3)
a63 = Or(i11,a62)
a64 = And(a56,a63)
a65 = And(i11,a62)
a66 = Or(a64,a65)
a67 = Not(a66)
a68 = Or(a61,a65)
a69 = Not(a68)
a70 = And(a59,a69)
a71 = Not(a70)
a72 = Or(i2,a19)
a73 = And(a67,a72)
a74 = And(i2,a19)
a75 = Or(a73,a74)
a76 = Or(a67,a74)
a77 = And(a72,a76)
a78 = Not(a74)
a79 = And(a72,a78)
a80 = And(a67,a79)
a81 = Not(a79)
a82 = And(a66,a81)
a83 = Or(a80,a82)
a84 = And(a70,a83)
a85 = Not(a84)
a86 = Or(i1,a75)
a87 = And(a20,a86)
a88 = And(i1,a75)
a89 = Or(a87,a88)
a90 = Not(a89)
a91 = And(a21,a90)
a92 = And(i1,a20)
a93 = Not(i1)
a94 = And(i9,a93)
a95 = Or(a92,a94)
a96 = And(a77,a95)
a97 = Not(a96)
a98 = Or(a75,a95)
a99 = And(a97,a98)
a100 = Not(a99)
a101 = Or(i0,a90)
a102 = And(a21,a101)
a103 = And(i0,a90)
a104 = Or(a102,a103)
a105 = And(a29,a104)
a106 = And(a26,a105)
a107 = Not(a105)
a108 = And(a23,a107)
a109 = Or(a106,a108)
a110 = And(a34,a109)
a111 = Not(a109)
a112 = And(a33,a111)
a113 = Or(a110,a112)
a114 = And(a68,a104)
a115 = And(a71,a104)
a116 = Or(a83,a115)
a117 = Not(a116)
a118 = And(a83,a115)
a119 = Or(a117,a118)
a120 = And(a85,a104)
a121 = Or(a100,a120)
a122 = And(a100,a104)
a123 = And(a85,a122)
a124 = Not(a123)
a125 = And(a121,a124)
a126 = And(a84,a104)
a127 = And(a99,a126)
a128 = Not(a104)
a129 = Or(a35,a128)
a130 = And(a49,a129)
a131 = Not(a129)
a132 = And(a48,a131)
a133 = Or(a130,a132)
a134 = And(a69,a128)
a135 = Or(a114,a134)
a136 = Or(a56,a135)
a137 = Not(a136)
a138 = And(a60,a135)
a139 = Or(a59,a138)
a140 = Or(a137,a139)
a141 = And(a71,a140)
a142 = And(i0,a91)
a143 = Or(a127,a142)
a144 = Not(i0)
a145 = And(a89,a144)
a146 = And(i8,a145)
a147 = Or(a143,a146)

# Primary output vector, i.e. list of gate indexes corresponding to each primary output, starting from the LSB
out_vec = [16,147,125,119,141,71,133,113,29]


# Approx. circuit: Declaration of integer variables for the weights of each primaty output bit, followed by the weight assignment
w_app_o0 = Int('w_app_o0')
w_app_o0 = a16* 2/2
w_app_o1 = Int('w_app_o1')
w_app_o1 = a147*2
w_app_o2 = Int('w_app_o2')
w_app_o2 = a125*4
w_app_o3 = Int('w_app_o3')
w_app_o3 = a119*8
w_app_o4 = Int('w_app_o4')
w_app_o4 = a141*16
w_app_o5 = Int('w_app_o5')
w_app_o5 = a71*32
w_app_o6 = Int('w_app_o6')
w_app_o6 = a133*64
w_app_o7 = Int('w_app_o7')
w_app_o7 = a113*128
w_app_o8 = Int('w_app_o8')
w_app_o8 = a29*256

# Definition and expression of the integer value of the output for the exact circuit
int_app_out = Int('int_app_out')
int_app_out = w_app_o0 + w_app_o1 + w_app_o2 + w_app_o3 + w_app_o4 + w_app_o5 + w_app_o6 + w_app_o7 + w_app_o8
f = Function('f', IntSort(), IntSort(), IntSort())
foundWAE = False
WAE = 0
start_whole = time.time()
s = Solver()
s.add(f(int_exa_out, int_app_out) == abs(int_exa_out - int_app_out))


s.push()
s.add(i0==True, i1==False, i2==True, i3==True, i4==False, i5==False, i6==False, i7==False, i8==False, i9==True, i10==True, i11==True, i12==True, i13==False, i14==False, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==True, i2==False, i3==True, i4==True, i5==True, i6==True, i7==False, i8==True, i9==False, i10==True, i11==False, i12==True, i13==True, i14==False, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==False, i2==True, i3==False, i4==True, i5==True, i6==True, i7==True, i8==True, i9==False, i10==False, i11==True, i12==True, i13==False, i14==False, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==True, i2==True, i3==True, i4==True, i5==False, i6==True, i7==True, i8==False, i9==False, i10==True, i11==False, i12==True, i13==True, i14==False, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==False, i2==False, i3==False, i4==False, i5==True, i6==True, i7==False, i8==False, i9==False, i10==False, i11==False, i12==False, i13==True, i14==False, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==False, i2==False, i3==True, i4==False, i5==False, i6==True, i7==False, i8==True, i9==True, i10==True, i11==True, i12==True, i13==True, i14==True, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==True, i2==True, i3==False, i4==True, i5==False, i6==False, i7==True, i8==False, i9==True, i10==False, i11==False, i12==True, i13==True, i14==True, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==False, i2==True, i3==False, i4==False, i5==False, i6==False, i7==False, i8==False, i9==False, i10==True, i11==False, i12==False, i13==True, i14==True, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==True, i2==True, i3==False, i4==False, i5==True, i6==True, i7==True, i8==True, i9==False, i10==False, i11==True, i12==True, i13==True, i14==True, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==False, i2==True, i3==True, i4==False, i5==False, i6==True, i7==False, i8==True, i9==True, i10==True, i11==False, i12==False, i13==False, i14==False, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==False, i2==True, i3==False, i4==False, i5==False, i6==False, i7==False, i8==True, i9==False, i10==False, i11==False, i12==False, i13==True, i14==True, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==True, i2==True, i3==False, i4==True, i5==True, i6==True, i7==True, i8==False, i9==False, i10==True, i11==False, i12==True, i13==True, i14==False, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==False, i2==True, i3==False, i4==False, i5==True, i6==False, i7==False, i8==True, i9==True, i10==True, i11==False, i12==False, i13==True, i14==False, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==True, i2==False, i3==False, i4==True, i5==True, i6==False, i7==True, i8==False, i9==False, i10==True, i11==False, i12==True, i13==False, i14==True, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==True, i2==False, i3==False, i4==True, i5==False, i6==True, i7==True, i8==False, i9==False, i10==True, i11==False, i12==True, i13==True, i14==False, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==False, i2==True, i3==True, i4==True, i5==True, i6==False, i7==False, i8==True, i9==False, i10==True, i11==False, i12==True, i13==False, i14==True, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==True, i2==True, i3==True, i4==False, i5==False, i6==True, i7==False, i8==False, i9==False, i10==True, i11==True, i12==False, i13==True, i14==False, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==True, i2==False, i3==True, i4==True, i5==True, i6==False, i7==True, i8==False, i9==True, i10==True, i11==True, i12==True, i13==True, i14==False, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==True, i2==True, i3==True, i4==True, i5==True, i6==True, i7==False, i8==False, i9==False, i10==False, i11==True, i12==True, i13==False, i14==False, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==True, i2==False, i3==False, i4==True, i5==False, i6==False, i7==False, i8==False, i9==False, i10==True, i11==True, i12==False, i13==False, i14==False, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==True, i2==True, i3==True, i4==False, i5==False, i6==False, i7==False, i8==False, i9==True, i10==False, i11==False, i12==True, i13==False, i14==False, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==True, i2==False, i3==True, i4==True, i5==True, i6==False, i7==True, i8==True, i9==False, i10==True, i11==True, i12==False, i13==True, i14==True, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==True, i2==True, i3==False, i4==False, i5==False, i6==False, i7==True, i8==True, i9==True, i10==False, i11==True, i12==False, i13==False, i14==False, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==False, i2==False, i3==False, i4==False, i5==False, i6==False, i7==False, i8==True, i9==False, i10==True, i11==False, i12==False, i13==True, i14==False, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==False, i2==True, i3==False, i4==True, i5==True, i6==False, i7==False, i8==False, i9==False, i10==False, i11==False, i12==True, i13==True, i14==True, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==True, i2==False, i3==False, i4==False, i5==True, i6==False, i7==True, i8==False, i9==False, i10==True, i11==True, i12==True, i13==False, i14==True, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==True, i2==True, i3==False, i4==False, i5==True, i6==True, i7==True, i8==True, i9==False, i10==True, i11==True, i12==True, i13==False, i14==False, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==False, i2==True, i3==False, i4==False, i5==True, i6==True, i7==False, i8==True, i9==False, i10==False, i11==True, i12==True, i13==True, i14==False, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==False, i2==True, i3==True, i4==False, i5==False, i6==True, i7==False, i8==True, i9==True, i10==False, i11==False, i12==True, i13==True, i14==True, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==True, i2==False, i3==True, i4==True, i5==False, i6==False, i7==True, i8==False, i9==True, i10==False, i11==True, i12==True, i13==False, i14==True, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==True, i2==True, i3==True, i4==True, i5==True, i6==True, i7==True, i8==True, i9==False, i10==False, i11==True, i12==True, i13==False, i14==False, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==False, i2==True, i3==False, i4==True, i5==True, i6==True, i7==True, i8==False, i9==False, i10==False, i11==True, i12==True, i13==True, i14==False, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==False, i2==False, i3==False, i4==True, i5==True, i6==True, i7==True, i8==True, i9==True, i10==False, i11==True, i12==True, i13==False, i14==True, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==False, i2==False, i3==True, i4==True, i5==False, i6==False, i7==True, i8==True, i9==True, i10==False, i11==True, i12==False, i13==False, i14==True, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==True, i2==True, i3==True, i4==False, i5==True, i6==False, i7==False, i8==True, i9==True, i10==False, i11==True, i12==False, i13==False, i14==False, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==False, i2==False, i3==False, i4==True, i5==False, i6==False, i7==False, i8==False, i9==True, i10==False, i11==True, i12==False, i13==False, i14==True, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==False, i2==False, i3==False, i4==True, i5==True, i6==False, i7==True, i8==False, i9==False, i10==True, i11==False, i12==True, i13==True, i14==True, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==True, i2==False, i3==True, i4==False, i5==True, i6==True, i7==True, i8==True, i9==False, i10==True, i11==True, i12==False, i13==False, i14==True, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==True, i2==True, i3==True, i4==False, i5==True, i6==False, i7==False, i8==True, i9==True, i10==False, i11==True, i12==True, i13==False, i14==False, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==False, i2==False, i3==True, i4==True, i5==True, i6==True, i7==True, i8==True, i9==True, i10==False, i11==True, i12==False, i13==False, i14==True, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==True, i2==True, i3==False, i4==False, i5==False, i6==True, i7==False, i8==False, i9==False, i10==False, i11==True, i12==False, i13==False, i14==False, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==False, i2==True, i3==True, i4==True, i5==True, i6==True, i7==True, i8==True, i9==False, i10==False, i11==True, i12==False, i13==True, i14==False, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==False, i2==False, i3==True, i4==True, i5==False, i6==True, i7==False, i8==True, i9==True, i10==False, i11==True, i12==False, i13==True, i14==False, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==False, i2==True, i3==False, i4==True, i5==True, i6==False, i7==False, i8==False, i9==False, i10==False, i11==True, i12==False, i13==False, i14==False, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==True, i2==False, i3==False, i4==False, i5==True, i6==True, i7==True, i8==False, i9==True, i10==False, i11==True, i12==False, i13==True, i14==False, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==True, i2==False, i3==False, i4==True, i5==True, i6==False, i7==True, i8==False, i9==False, i10==True, i11==True, i12==False, i13==False, i14==True, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==False, i2==False, i3==False, i4==True, i5==False, i6==False, i7==True, i8==True, i9==True, i10==True, i11==True, i12==True, i13==True, i14==False, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==False, i2==True, i3==True, i4==True, i5==True, i6==False, i7==False, i8==False, i9==False, i10==False, i11==False, i12==False, i13==True, i14==True, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==False, i1==True, i2==False, i3==True, i4==False, i5==False, i6==False, i7==False, i8==False, i9==False, i10==True, i11==True, i12==True, i13==True, i14==False, i15==True)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()

s.push()
s.add(i0==True, i1==False, i2==True, i3==False, i4==False, i5==False, i6==False, i7==False, i8==False, i9==False, i10==True, i11==True, i12==True, i13==False, i14==True, i15==False)
sol = s.check()
m = s.model()
print("Model = ", m)
print(sol)

cur_WAE = m[m[len(m)-1]].else_value().as_long()
if cur_WAE < 0:
	cur_WAE = -1 * cur_WAE
if cur_WAE > WAE:
	WAE = cur_WAE
s.pop()
end_whole = time.time()
print("Finished processing, WAE == ", WAE)
	
	
	
	
output_file_name = "weights_wae_acc_abs_diff_8_0.1_app_abs_diff_8_0.1_app1_mc_50.txt"
output_file = "weights/"+output_file_name
if os.path.isfile(output_file):
	os.remove(output_file)
f = open(output_file, "a")
f.write(str(WAE)+"\n")
f.close()



output_time_file_name = "log_wae_acc_abs_diff_8_0.1_app_abs_diff_8_0.1_app1_mc_50.txt"
output_time_file = "log/"+output_time_file_name
if os.path.isfile(output_time_file):
	os.remove(output_time_file)
f = open(output_time_file, "a")
f.write(str(end_whole-start_whole))
f.close()
