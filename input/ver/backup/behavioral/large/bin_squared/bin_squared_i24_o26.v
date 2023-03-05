module bin_squared_i24_o26 (a, b, r);
input [11:0] a, b;
output [25:0] r;


assign r = (a - b) * (a - b);

endmodule 
 
