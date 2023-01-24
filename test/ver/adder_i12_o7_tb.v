module adder_i12_o7_tb;
reg [11:0] pi;
wire [6:0] po;
adder_i12_o7 dut( pi[0] , pi[1] , pi[2] , pi[3] , pi[4] , pi[5] , pi[6] , pi[7] , pi[8] , pi[9] , pi[10] , pi[11] , po[0] , po[1] , po[2] , po[3] , po[4] , po[5] , po[6] );
initial
begin
# 1  pi=12'b000101000100;
#1 $display("%b", po);
# 1  pi=12'b010011100000;
#1 $display("%b", po);
# 1  pi=12'b010000000101;
#1 $display("%b", po);
# 1  pi=12'b101111011001;
#1 $display("%b", po);
# 1  pi=12'b000010100010;
#1 $display("%b", po);
# 1  pi=12'b011010000010;
#1 $display("%b", po);
# 1  pi=12'b100001111010;
#1 $display("%b", po);
# 1  pi=12'b001110001100;
#1 $display("%b", po);
# 1  pi=12'b001110100111;
#1 $display("%b", po);
# 1  pi=12'b100111111110;
#1 $display("%b", po);
# 1  pi=12'b110110101110;
#1 $display("%b", po);
# 1  pi=12'b011100010011;
#1 $display("%b", po);
# 1  pi=12'b110110111001;
#1 $display("%b", po);
# 1  pi=12'b010100000110;
#1 $display("%b", po);
# 1  pi=12'b001101011110;
#1 $display("%b", po);
# 1  pi=12'b111001001000;
#1 $display("%b", po);
# 1  pi=12'b110101101001;
#1 $display("%b", po);
# 1  pi=12'b000100001110;
#1 $display("%b", po);
# 1  pi=12'b011101111010;
#1 $display("%b", po);
# 1  pi=12'b001010101010;
#1 $display("%b", po);
# 1  pi=12'b101010001100;
#1 $display("%b", po);
# 1  pi=12'b101011011011;
#1 $display("%b", po);
# 1  pi=12'b101000010000;
#1 $display("%b", po);
# 1  pi=12'b110011011001;
#1 $display("%b", po);
# 1  pi=12'b001100100001;
#1 $display("%b", po);
# 1  pi=12'b101010001011;
#1 $display("%b", po);
# 1  pi=12'b100011111010;
#1 $display("%b", po);
# 1  pi=12'b110000100100;
#1 $display("%b", po);
# 1  pi=12'b111010000001;
#1 $display("%b", po);
# 1  pi=12'b010110000011;
#1 $display("%b", po);
# 1  pi=12'b001100111000;
#1 $display("%b", po);
# 1  pi=12'b101011000001;
#1 $display("%b", po);
# 1  pi=12'b011111110000;
#1 $display("%b", po);
# 1  pi=12'b111100011001;
#1 $display("%b", po);
# 1  pi=12'b100101100000;
#1 $display("%b", po);
# 1  pi=12'b000110000001;
#1 $display("%b", po);
# 1  pi=12'b101110011000;
#1 $display("%b", po);
# 1  pi=12'b000111111110;
#1 $display("%b", po);
# 1  pi=12'b110110000100;
#1 $display("%b", po);
# 1  pi=12'b110000011010;
#1 $display("%b", po);
# 1  pi=12'b110001000101;
#1 $display("%b", po);
# 1  pi=12'b010000010101;
#1 $display("%b", po);
# 1  pi=12'b011001000100;
#1 $display("%b", po);
# 1  pi=12'b011111100100;
#1 $display("%b", po);
# 1  pi=12'b100110100000;
#1 $display("%b", po);
# 1  pi=12'b011001110100;
#1 $display("%b", po);
# 1  pi=12'b111110001000;
#1 $display("%b", po);
# 1  pi=12'b110011101110;
#1 $display("%b", po);
# 1  pi=12'b110001100100;
#1 $display("%b", po);
# 1  pi=12'b111001010011;
#1 $display("%b", po);
# 1  pi=12'b010000000101;
#1 $display("%b", po);
# 1  pi=12'b100101011001;
#1 $display("%b", po);
# 1  pi=12'b011000111001;
#1 $display("%b", po);
# 1  pi=12'b011111100001;
#1 $display("%b", po);
# 1  pi=12'b010000110001;
#1 $display("%b", po);
# 1  pi=12'b000110010011;
#1 $display("%b", po);
# 1  pi=12'b000010010100;
#1 $display("%b", po);
# 1  pi=12'b011011001000;
#1 $display("%b", po);
# 1  pi=12'b010100100011;
#1 $display("%b", po);
# 1  pi=12'b101100000001;
#1 $display("%b", po);
# 1  pi=12'b011111010101;
#1 $display("%b", po);
# 1  pi=12'b101001111100;
#1 $display("%b", po);
# 1  pi=12'b000001001001;
#1 $display("%b", po);
# 1  pi=12'b010101101100;
#1 $display("%b", po);
# 1  pi=12'b101101011101;
#1 $display("%b", po);
# 1  pi=12'b010011110110;
#1 $display("%b", po);
# 1  pi=12'b010010101011;
#1 $display("%b", po);
# 1  pi=12'b010000111010;
#1 $display("%b", po);
# 1  pi=12'b011010001001;
#1 $display("%b", po);
# 1  pi=12'b100011001111;
#1 $display("%b", po);
# 1  pi=12'b000000111100;
#1 $display("%b", po);
# 1  pi=12'b000011100110;
#1 $display("%b", po);
# 1  pi=12'b010101101110;
#1 $display("%b", po);
# 1  pi=12'b110001010011;
#1 $display("%b", po);
# 1  pi=12'b100101101001;
#1 $display("%b", po);
# 1  pi=12'b110101110011;
#1 $display("%b", po);
# 1  pi=12'b001001100101;
#1 $display("%b", po);
# 1  pi=12'b000110010010;
#1 $display("%b", po);
# 1  pi=12'b101100101010;
#1 $display("%b", po);
# 1  pi=12'b000100001001;
#1 $display("%b", po);
# 1  pi=12'b001011101110;
#1 $display("%b", po);
# 1  pi=12'b001000001100;
#1 $display("%b", po);
# 1  pi=12'b001001010100;
#1 $display("%b", po);
# 1  pi=12'b111000010110;
#1 $display("%b", po);
# 1  pi=12'b111011100110;
#1 $display("%b", po);
# 1  pi=12'b010100111111;
#1 $display("%b", po);
# 1  pi=12'b011001010001;
#1 $display("%b", po);
# 1  pi=12'b111010011010;
#1 $display("%b", po);
# 1  pi=12'b000001000101;
#1 $display("%b", po);
# 1  pi=12'b100010110010;
#1 $display("%b", po);
# 1  pi=12'b001100001110;
#1 $display("%b", po);
# 1  pi=12'b100100001010;
#1 $display("%b", po);
# 1  pi=12'b111010000101;
#1 $display("%b", po);
# 1  pi=12'b011001000001;
#1 $display("%b", po);
# 1  pi=12'b000101001010;
#1 $display("%b", po);
# 1  pi=12'b011010000111;
#1 $display("%b", po);
# 1  pi=12'b110111111111;
#1 $display("%b", po);
# 1  pi=12'b111001001100;
#1 $display("%b", po);
# 1  pi=12'b011011011010;
#1 $display("%b", po);
# 1  pi=12'b110011110010;
#1 $display("%b", po);
end
endmodule