`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/11/2024 11:03:29 AM
// Design Name: 
// Module Name: contatore_binario
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module contatore_binario(
    input clk,
    output reg[15:0] led
    );
    reg[38:0] counter;
    integer i;
    
    initial
        counter = 0;
        
    always @ (posedge clk) begin
        for(i = 0; i < 16; i = i + 1) begin
            led[i] <= counter[23 + i];
        end
        counter <= counter + 1;
    end
endmodule
