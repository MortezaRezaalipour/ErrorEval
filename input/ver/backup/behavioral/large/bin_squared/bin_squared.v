module bin_squared (a, b, r);
input [1:0] a, b;
output [5:0] r;


assign r = (a - b) * (a - b);

endmodule 
 
