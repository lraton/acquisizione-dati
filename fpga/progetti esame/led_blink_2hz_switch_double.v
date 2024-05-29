`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/11/2024 10:06:55 AM
// Design Name: 
// Module Name: led_blink_2hz_switch_double
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


module led_blink_2hz_switch_double(
    input clk,
    input wire [1:0] sw,
    output reg [1:0] led
    );

    reg [25:0] counter;
    
    initial
        counter = 0;
    always @ (posedge clk) begin
        led[0] <= counter[25];

        if(sw[0]==0)begin
            counter <= counter + 1;
        end else begin
            counter <= counter + 2;
        end
    end
endmodule
