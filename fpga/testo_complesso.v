`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/11/2024 09:52:11 AM
// Design Name: 
// Module Name: testo_complesso
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


module testo_complesso(
    input wire A,
    input wire B,
    input wire C,
    output wire D,
    output wire E

    );
    assign D = A & (B & C);
    assign E =  A ^ (B & C);
endmodule
