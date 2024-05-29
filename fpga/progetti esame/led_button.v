`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/11/2024 11:23:18 AM
// Design Name: 
// Module Name: led_button
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


module led_button(
    input clk,
    input btnC,
    output reg[1:0] led
    );
    reg pressed_last_cycle;
    reg led_state;
    
    always @ (posedge clk) begin
    
        if (btnC & (~ pressed_last_cycle)) begin
            led_state <= ~led_state;
            led[0] <= led_state;
        end
        pressed_last_cycle <= btnC;
    end
    
endmodule
