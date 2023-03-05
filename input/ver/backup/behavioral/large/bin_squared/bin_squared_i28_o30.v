module bin_squared_i28_o30 (a, b, r);
input [13:0] a, b;
output [29:0] r;


assign r = (a - b) * (a - b);

endmodule 
 
