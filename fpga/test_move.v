`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/11/2024 11:47:06 AM
// Design Name: 
// Module Name: test_move
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


module test_move(
    input clk,
    input btnL,
    input btnR,
    output reg[15:0] led
    );
    reg pressed_last_cycleL;
    reg pressed_last_cycleR;
    reg[15:0] arrayled = 16'b0000000010000000;
    
    initial
    led<=arrayled;
    
    always @ (posedge clk) begin
        if (btnL & (~ pressed_last_cycleL) & ~arrayled[15]) begin
            arrayled <= arrayled << 1;
        end
        pressed_last_cycleL <= btnL;
        
        if (btnR & (~ pressed_last_cycleR) & ~arrayled[0]) begin 
            arrayled <= arrayled >> 1;
        end
        pressed_last_cycleR <= btnR;
        
        led<=arrayled;
    end
endmodule
