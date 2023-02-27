module circuit (i7, i6, i5, i4, i3, i2, i1, i0, o4, o3, o2, o1, o0);
input i7, i6, i5, i4, i3, i2, i1, i0;
output o4, o3, o2, o1, o0;
wire o0_t0, o0_t1, o0_t2, o0_t3, o0_t4, o0_t5, o1_t0, o1_t1, o1_t2, o1_t3, o1_t4, o1_t5, o2_t0, o2_t1, o2_t2, o2_t3, o2_t4, o2_t5, o3_t0, o3_t1, o3_t2, o3_t3, o3_t4, o3_t5, o4_t0, o4_t1, o4_t2, o4_t3, o4_t4, o4_t5;

// output 0
assign o0_t0 = i1 & i4 & ~i5 & i7;
assign o0_t1 = i0 & i3 & ~i5 & i7;
assign o0_t2 = i0 & i1 & ~i2 & i7;
assign o0_t3 = 1;
assign o0_t4 = 1;
assign o0_t5 = 1;
assign o0 = o0_t0 | o0_t1 | o0_t2 | o0_t3 | o0_t4 | o0_t5;

// output 1
assign o1_t0 = i2 & ~i6 & i7;
assign o1_t1 = i2 & ~i6 & ~i7;
assign o1_t2 = i1 & i2 & i5 & i6;
assign o1_t3 = ~i0 & ~i2 & i5 & i6;
assign o1_t4 = i1 & i5 & i6;
assign o1_t5 = ~i1 & ~i2 & ~i5 & i6;
assign o1 = o1_t0 | o1_t1 | o1_t2 | o1_t3 | o1_t4 | o1_t5;

// output 2
assign o2_t0 = i4 & i5 & i6 & i7;
assign o2_t1 = i1 & i4 & i6 & i7;
assign o2_t2 = i2 & i4 & ~i6 & ~i7;
assign o2_t3 = i1 & i4 & ~i6 & ~i7;
assign o2_t4 = i5;
assign o2_t5 = i1;
assign o2 = o2_t0 | o2_t1 | o2_t2 | o2_t3 | o2_t4 | o2_t5;

// output 3
assign o3_t0 = i2 & i3 & i6 & i7;
assign o3_t1 = ~i2 & ~i3 & i6 & i7;
assign o3_t2 = ~i3 & ~i6 & i7;
assign o3_t3 = i2 & ~i3 & i6 & ~i7;
assign o3_t4 = i2 & i3 & ~i6 & ~i7;
assign o3_t5 = ~i2 & i3 & ~i7;
assign o3 = o3_t0 | o3_t1 | o3_t2 | o3_t3 | o3_t4 | o3_t5;

// output 4
assign o4_t0 = i2 & i6 & i7;
assign o4_t1 = i2 & i3 & ~i6 & i7;
assign o4_t2 = i3 & i7;
assign o4_t3 = i3 & i7;
assign o4_t4 = i3 & i7;
assign o4_t5 = i2 & i3 & i6;
assign o4 = o4_t0 | o4_t1 | o4_t2 | o4_t3 | o4_t4 | o4_t5;

endmodule