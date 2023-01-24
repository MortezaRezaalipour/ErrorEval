module mul_i12_o12_tb;
reg [11:0] pi;
wire [11:0] po;
mul_i12_o12 dut( pi[0] , pi[1] , pi[2] , pi[3] , pi[4] , pi[5] , pi[6] , pi[7] , pi[8] , pi[9] , pi[10] , pi[11] , po[0] , po[1] , po[2] , po[3] , po[4] , po[5] , po[6] , po[7] , po[8] , po[9] , po[10] , po[11] );
initial
begin
# 1  pi=12'b010111111000;
#1 $display("%b", po);
# 1  pi=12'b101000011001;
#1 $display("%b", po);
# 1  pi=12'b011100100000;
#1 $display("%b", po);
# 1  pi=12'b010000111000;
#1 $display("%b", po);
# 1  pi=12'b011100011010;
#1 $display("%b", po);
# 1  pi=12'b000101100011;
#1 $display("%b", po);
# 1  pi=12'b111110010100;
#1 $display("%b", po);
# 1  pi=12'b111011100111;
#1 $display("%b", po);
# 1  pi=12'b111101001000;
#1 $display("%b", po);
# 1  pi=12'b001111001000;
#1 $display("%b", po);
# 1  pi=12'b001111011001;
#1 $display("%b", po);
# 1  pi=12'b011001111101;
#1 $display("%b", po);
# 1  pi=12'b000111100010;
#1 $display("%b", po);
# 1  pi=12'b111110100101;
#1 $display("%b", po);
# 1  pi=12'b000100110010;
#1 $display("%b", po);
# 1  pi=12'b000100110100;
#1 $display("%b", po);
# 1  pi=12'b111001101010;
#1 $display("%b", po);
# 1  pi=12'b110110011011;
#1 $display("%b", po);
# 1  pi=12'b100011001101;
#1 $display("%b", po);
# 1  pi=12'b111000010000;
#1 $display("%b", po);
# 1  pi=12'b100101001101;
#1 $display("%b", po);
# 1  pi=12'b101010110110;
#1 $display("%b", po);
# 1  pi=12'b101111111100;
#1 $display("%b", po);
# 1  pi=12'b001111001110;
#1 $display("%b", po);
# 1  pi=12'b000011111010;
#1 $display("%b", po);
# 1  pi=12'b110000001001;
#1 $display("%b", po);
# 1  pi=12'b000001011111;
#1 $display("%b", po);
# 1  pi=12'b101011001010;
#1 $display("%b", po);
# 1  pi=12'b100011111100;
#1 $display("%b", po);
# 1  pi=12'b111111100111;
#1 $display("%b", po);
# 1  pi=12'b010110010010;
#1 $display("%b", po);
# 1  pi=12'b101010111111;
#1 $display("%b", po);
# 1  pi=12'b011110001010;
#1 $display("%b", po);
# 1  pi=12'b011010010001;
#1 $display("%b", po);
# 1  pi=12'b001001111111;
#1 $display("%b", po);
# 1  pi=12'b000001000100;
#1 $display("%b", po);
# 1  pi=12'b000110110001;
#1 $display("%b", po);
# 1  pi=12'b000100111011;
#1 $display("%b", po);
# 1  pi=12'b111100010110;
#1 $display("%b", po);
# 1  pi=12'b110111000001;
#1 $display("%b", po);
# 1  pi=12'b111101011111;
#1 $display("%b", po);
# 1  pi=12'b100000111010;
#1 $display("%b", po);
# 1  pi=12'b001001110100;
#1 $display("%b", po);
# 1  pi=12'b111010101001;
#1 $display("%b", po);
# 1  pi=12'b100110110001;
#1 $display("%b", po);
# 1  pi=12'b001110010010;
#1 $display("%b", po);
# 1  pi=12'b111110001101;
#1 $display("%b", po);
# 1  pi=12'b101110101111;
#1 $display("%b", po);
# 1  pi=12'b001110101100;
#1 $display("%b", po);
# 1  pi=12'b001110001000;
#1 $display("%b", po);
# 1  pi=12'b011110100010;
#1 $display("%b", po);
# 1  pi=12'b101110101001;
#1 $display("%b", po);
# 1  pi=12'b110111001010;
#1 $display("%b", po);
# 1  pi=12'b111100100110;
#1 $display("%b", po);
# 1  pi=12'b000110111001;
#1 $display("%b", po);
# 1  pi=12'b111010101100;
#1 $display("%b", po);
# 1  pi=12'b010110111001;
#1 $display("%b", po);
# 1  pi=12'b100011010001;
#1 $display("%b", po);
# 1  pi=12'b101000000001;
#1 $display("%b", po);
# 1  pi=12'b100100110101;
#1 $display("%b", po);
# 1  pi=12'b000010100000;
#1 $display("%b", po);
# 1  pi=12'b101101001100;
#1 $display("%b", po);
# 1  pi=12'b001111111011;
#1 $display("%b", po);
# 1  pi=12'b111100110100;
#1 $display("%b", po);
# 1  pi=12'b001000101000;
#1 $display("%b", po);
# 1  pi=12'b100110111000;
#1 $display("%b", po);
# 1  pi=12'b010010110110;
#1 $display("%b", po);
# 1  pi=12'b010101000101;
#1 $display("%b", po);
# 1  pi=12'b010001111011;
#1 $display("%b", po);
# 1  pi=12'b100100110111;
#1 $display("%b", po);
# 1  pi=12'b101101100101;
#1 $display("%b", po);
# 1  pi=12'b101110111101;
#1 $display("%b", po);
# 1  pi=12'b100100111111;
#1 $display("%b", po);
# 1  pi=12'b010011011100;
#1 $display("%b", po);
# 1  pi=12'b011111111101;
#1 $display("%b", po);
# 1  pi=12'b111111111000;
#1 $display("%b", po);
# 1  pi=12'b000001111111;
#1 $display("%b", po);
# 1  pi=12'b100000100100;
#1 $display("%b", po);
# 1  pi=12'b111100111010;
#1 $display("%b", po);
# 1  pi=12'b011101001101;
#1 $display("%b", po);
# 1  pi=12'b111010010001;
#1 $display("%b", po);
# 1  pi=12'b000100011001;
#1 $display("%b", po);
# 1  pi=12'b100010110111;
#1 $display("%b", po);
# 1  pi=12'b000110001111;
#1 $display("%b", po);
# 1  pi=12'b101100110011;
#1 $display("%b", po);
# 1  pi=12'b000100010101;
#1 $display("%b", po);
# 1  pi=12'b010101010111;
#1 $display("%b", po);
# 1  pi=12'b110011101110;
#1 $display("%b", po);
# 1  pi=12'b100101011101;
#1 $display("%b", po);
# 1  pi=12'b001100001011;
#1 $display("%b", po);
# 1  pi=12'b001101111110;
#1 $display("%b", po);
# 1  pi=12'b110010001000;
#1 $display("%b", po);
# 1  pi=12'b000100101111;
#1 $display("%b", po);
# 1  pi=12'b011010101110;
#1 $display("%b", po);
# 1  pi=12'b010110011100;
#1 $display("%b", po);
# 1  pi=12'b011110010010;
#1 $display("%b", po);
# 1  pi=12'b001011110111;
#1 $display("%b", po);
# 1  pi=12'b100011000110;
#1 $display("%b", po);
# 1  pi=12'b010111110100;
#1 $display("%b", po);
# 1  pi=12'b100011110100;
#1 $display("%b", po);
end
endmodule