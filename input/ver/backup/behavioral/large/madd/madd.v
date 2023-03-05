module madd (a, b, c, r);
input [1:0] a, b, c;
output [2:0] r;


assign r = (a * b) + c;

endmodule  
