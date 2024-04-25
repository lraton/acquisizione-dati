`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/11/2024 10:06:55 AM
// Design Name: 
// Module Name: led_blink
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


module led_blink(
    input clk,
    input wire [7:0] sw,
    output reg [7:0] led
    );
    reg [31:0] counter;
    initial
        counter = 0;
    always @ (posedge clk) begin 
        led[0] <= sw[0] & counter[25];
        counter <= counter + 1;
    end
endmodule
