module abs_diff_i12_o7_tb;
reg [11:0] pi;
wire [5:0] po;
abs_diff_i12_o7 dut( pi[0] , pi[1] , pi[2] , pi[3] , pi[4] , pi[5] , pi[6] , pi[7] , pi[8] , pi[9] , pi[10] , pi[11] , po[0] , po[1] , po[2] , po[3] , po[4] , po[5] );
initial
begin
# 1  pi=12'b000101000111;
#1 $display("%b", po);
# 1  pi=12'b010111101010;
#1 $display("%b", po);
# 1  pi=12'b011100101110;
#1 $display("%b", po);
# 1  pi=12'b111010001110;
#1 $display("%b", po);
# 1  pi=12'b100110100110;
#1 $display("%b", po);
# 1  pi=12'b110011001100;
#1 $display("%b", po);
# 1  pi=12'b000001000101;
#1 $display("%b", po);
# 1  pi=12'b001101001000;
#1 $display("%b", po);
# 1  pi=12'b000000100110;
#1 $display("%b", po);
# 1  pi=12'b100110110110;
#1 $display("%b", po);
# 1  pi=12'b111000110010;
#1 $display("%b", po);
# 1  pi=12'b000110010110;
#1 $display("%b", po);
# 1  pi=12'b001010101010;
#1 $display("%b", po);
# 1  pi=12'b100110111011;
#1 $display("%b", po);
# 1  pi=12'b001010100110;
#1 $display("%b", po);
# 1  pi=12'b010001110011;
#1 $display("%b", po);
# 1  pi=12'b011101011111;
#1 $display("%b", po);
# 1  pi=12'b000001111111;
#1 $display("%b", po);
# 1  pi=12'b110110111100;
#1 $display("%b", po);
# 1  pi=12'b011011110111;
#1 $display("%b", po);
# 1  pi=12'b010001100111;
#1 $display("%b", po);
# 1  pi=12'b111000000101;
#1 $display("%b", po);
# 1  pi=12'b010100110100;
#1 $display("%b", po);
# 1  pi=12'b000011111011;
#1 $display("%b", po);
# 1  pi=12'b011111100010;
#1 $display("%b", po);
# 1  pi=12'b110100000000;
#1 $display("%b", po);
# 1  pi=12'b001101110000;
#1 $display("%b", po);
# 1  pi=12'b100011010100;
#1 $display("%b", po);
# 1  pi=12'b011000100011;
#1 $display("%b", po);
# 1  pi=12'b100000110011;
#1 $display("%b", po);
# 1  pi=12'b110100000011;
#1 $display("%b", po);
# 1  pi=12'b111011111101;
#1 $display("%b", po);
# 1  pi=12'b011000010111;
#1 $display("%b", po);
# 1  pi=12'b111110010001;
#1 $display("%b", po);
# 1  pi=12'b101010110100;
#1 $display("%b", po);
# 1  pi=12'b101110010100;
#1 $display("%b", po);
# 1  pi=12'b101000110101;
#1 $display("%b", po);
# 1  pi=12'b100100001000;
#1 $display("%b", po);
# 1  pi=12'b001001000100;
#1 $display("%b", po);
# 1  pi=12'b011110010101;
#1 $display("%b", po);
# 1  pi=12'b110110101110;
#1 $display("%b", po);
# 1  pi=12'b101001101111;
#1 $display("%b", po);
# 1  pi=12'b010000011111;
#1 $display("%b", po);
# 1  pi=12'b011000010001;
#1 $display("%b", po);
# 1  pi=12'b001001011001;
#1 $display("%b", po);
# 1  pi=12'b101110000100;
#1 $display("%b", po);
# 1  pi=12'b110101101101;
#1 $display("%b", po);
# 1  pi=12'b010001111111;
#1 $display("%b", po);
# 1  pi=12'b111001010110;
#1 $display("%b", po);
# 1  pi=12'b101001110110;
#1 $display("%b", po);
# 1  pi=12'b110101111101;
#1 $display("%b", po);
# 1  pi=12'b111101110111;
#1 $display("%b", po);
# 1  pi=12'b101000011000;
#1 $display("%b", po);
# 1  pi=12'b101000011010;
#1 $display("%b", po);
# 1  pi=12'b100110101110;
#1 $display("%b", po);
# 1  pi=12'b110110011000;
#1 $display("%b", po);
# 1  pi=12'b111010000001;
#1 $display("%b", po);
# 1  pi=12'b110100010101;
#1 $display("%b", po);
# 1  pi=12'b010001000111;
#1 $display("%b", po);
# 1  pi=12'b010001101101;
#1 $display("%b", po);
# 1  pi=12'b111110101101;
#1 $display("%b", po);
# 1  pi=12'b000111000110;
#1 $display("%b", po);
# 1  pi=12'b101111110110;
#1 $display("%b", po);
# 1  pi=12'b011011011110;
#1 $display("%b", po);
# 1  pi=12'b100011110000;
#1 $display("%b", po);
# 1  pi=12'b000111000101;
#1 $display("%b", po);
# 1  pi=12'b111001000110;
#1 $display("%b", po);
# 1  pi=12'b101100100101;
#1 $display("%b", po);
# 1  pi=12'b011011111101;
#1 $display("%b", po);
# 1  pi=12'b111100000111;
#1 $display("%b", po);
# 1  pi=12'b000010101110;
#1 $display("%b", po);
# 1  pi=12'b100101001111;
#1 $display("%b", po);
# 1  pi=12'b100101001111;
#1 $display("%b", po);
# 1  pi=12'b111001011100;
#1 $display("%b", po);
# 1  pi=12'b011000000101;
#1 $display("%b", po);
# 1  pi=12'b101100111000;
#1 $display("%b", po);
# 1  pi=12'b010100110110;
#1 $display("%b", po);
# 1  pi=12'b001111000100;
#1 $display("%b", po);
# 1  pi=12'b111011110010;
#1 $display("%b", po);
# 1  pi=12'b011011110011;
#1 $display("%b", po);
# 1  pi=12'b001100001001;
#1 $display("%b", po);
# 1  pi=12'b011000100001;
#1 $display("%b", po);
# 1  pi=12'b011110110000;
#1 $display("%b", po);
# 1  pi=12'b111111000001;
#1 $display("%b", po);
# 1  pi=12'b100001000101;
#1 $display("%b", po);
# 1  pi=12'b010111101111;
#1 $display("%b", po);
# 1  pi=12'b001011110110;
#1 $display("%b", po);
# 1  pi=12'b010101100011;
#1 $display("%b", po);
# 1  pi=12'b010001110000;
#1 $display("%b", po);
# 1  pi=12'b110111001010;
#1 $display("%b", po);
# 1  pi=12'b010110010100;
#1 $display("%b", po);
# 1  pi=12'b010100110010;
#1 $display("%b", po);
# 1  pi=12'b101011001010;
#1 $display("%b", po);
# 1  pi=12'b010001111101;
#1 $display("%b", po);
# 1  pi=12'b100011100110;
#1 $display("%b", po);
# 1  pi=12'b101110000011;
#1 $display("%b", po);
# 1  pi=12'b111011111100;
#1 $display("%b", po);
# 1  pi=12'b010110010111;
#1 $display("%b", po);
# 1  pi=12'b010011001101;
#1 $display("%b", po);
# 1  pi=12'b100100000011;
#1 $display("%b", po);
end
endmodule