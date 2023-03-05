module bin_squared_i32_o34 (a, b, r);
input [15:0] a, b;
output [33:0] r;


assign r = (a - b) * (a - b);

endmodule 
 
