module bin_squared_i36_o38 (a, b, r);
input [17:0] a, b;
output [37:0] r;


assign r = (a - b) * (a - b);

endmodule 
 
