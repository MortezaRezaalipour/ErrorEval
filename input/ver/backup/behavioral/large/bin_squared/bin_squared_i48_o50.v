module bin_squared_i48_o50 (a, b, r);
input [23:0] a, b;
output [49:0] r;


assign r = (a - b) * (a - b);

endmodule 
 
