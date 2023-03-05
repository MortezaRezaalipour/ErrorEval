module bin_squared_i40_o42 (a, b, r);
input [19:0] a, b;
output [39:0] r;


assign r = (a - b) * (a - b);

endmodule 
 
