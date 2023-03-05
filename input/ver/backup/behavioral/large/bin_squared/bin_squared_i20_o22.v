module bin_squared_i20_o22 (a, b, r);
input [9:0] a, b;
output [21:0] r;


assign r = (a - b) * (a - b);

endmodule 
 
