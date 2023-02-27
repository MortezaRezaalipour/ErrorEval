module circuit (i7, i6, i5, i4, i3, i2, i1, i0, o4, o3, o2, o1, o0);
input i7, i6, i5, i4, i3, i2, i1, i0;
output o4, o3, o2, o1, o0;
wire o0_t0, o0_t1, o1_t0, o1_t1, o2_t0, o2_t1, o3_t0, o3_t1;
wire	a8,a12,a13,a14,a15,a37,a38,a39,a40,a41,a42,a43,a44,a45;
   

// output 0
assign o0_t0 = i4 & i5;
assign o0_t1 = 1;
assign o0 = o0_t0 | o0_t1;

// output 1
assign o1_t0 = i5 & ~i6;
assign o1_t1 = ~i1 & ~i5;
assign o1 = o1_t0 | o1_t1;

// output 2
assign o2_t0 = i1 & ~i6;
assign o2_t1 = i2;
assign o2 = o2_t0 | o2_t1;

// output 3 --> a37
assign o3_t0 = i5 & i6;
assign o3_t1 = i1 & i6;
//assign o3 = o3_t0 | o3_t1;
assign a37 = o3_t0 | o3_t1;

   
// COMPLETED: output 4

assign    a8 = ~i7;
assign    a12 = ~i3;
assign    a13 = i7 & a12;
assign    a14 = i3 & a8;
assign    a15 = a13 | a14;

assign    a38 = i3 & a37;
assign    a39 = i3 | a37;
assign    a40 = i7 & a39;
assign    a41 = a38 | a40;
assign    a42 = a15 | a37;
assign    a43 = a15 & a37;
assign    a44 = ~a43;
assign    a45 = a42 & a44;

assign    o3 = a45;
assign    o4 = a41;

   
endmodule
