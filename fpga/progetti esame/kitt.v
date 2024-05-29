`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/11/2024 12:36:11 PM
// Design Name: 
// Module Name: kitt
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


module kitt(
    input clk,
    output reg[15:0] led
    );
    reg going_right = 1;
    reg[15:0] arrayled = 16'b1000000000000000;
    reg[31:0] counter = 0;
    reg value_last_frame = 0;
    
    initial
        led<=arrayled;
    
    always @ (posedge clk) begin
        counter <= counter + 1;
        
        if (counter[25] != value_last_frame) begin
            if (going_right) begin
                if (arrayled[0]) begin
                    going_right <= 0;
                end else begin
                    arrayled <= arrayled >> 1;
                end
            end else begin
                if (arrayled[15]) begin
                    going_right <= 1;
                end else begin
                    arrayled <= arrayled << 1;
                end
            end
        end
        
        value_last_frame <= counter[25];
        led<=arrayled;
    end
endmodule
