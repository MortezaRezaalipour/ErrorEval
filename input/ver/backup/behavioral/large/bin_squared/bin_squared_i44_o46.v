module bin_squared_i44_o46 (a, b, r);
input [21:0] a, b;
output [45:0] r;


assign r = (a - b) * (a - b);

endmodule 
 
