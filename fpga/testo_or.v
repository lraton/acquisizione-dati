`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/11/2024 09:39:21 AM
// Design Name: 
// Module Name: testo_or
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


module testo_or(
    input wire A,
    input wire B,
    output wire C
    
    );
    
    assign C =  A | B;
    
endmodule
