`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/18/2024 09:14:32 AM
// Design Name: 
// Module Name: calculator
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


module calculator(
    input clk,
    input wire[15:0] sw,
    input wire btnC,
    input wire btnR,
    input wire btnL,
    input wire btnU,
    input wire btnD,
    output  reg[15:0] led,
    output  reg[6:0] seg        
    );
    integer i=0;
    integer j=0;
    integer count=0;
    reg lastPressedC=0;
    reg lastPressedD=0;
    reg lastPressedU=0;
    reg lastPressedR=0;
    reg lastPressedL=0;
    reg[32:0] numberSave;
    reg[32:0] freq; 
    reg error;
    initial begin
    end
    always @ (posedge clk)
        begin

            if(error)begin 
                if(freq[25] && count < 10)begin
                    for(j=0;j<16;j = j+1) begin
                        led[j]<=~led[j];
                    end
                    count<=count+1;
                end
                else if(count == 10)begin
                    error<=0;
                end
            end // end error
            else begin
                if(lastPressedC==0 && btnC==1) begin
                    for(i=0;i<16;i = i+1) begin
                        numberSave[i]<=sw[i];
                    end
    
                end
                lastPressedC<= btnC;
                
                if(lastPressedD==0 && btnD==1) begin
                    
                    if(numberSave+sw < (2**16))begin
                        numberSave<=numberSave+sw;
                    end
                    else begin
                        count<=0;
                        error<=1;
                    end
                end
                lastPressedD<= btnD;
                
                if(lastPressedU==0 && btnU==1) begin
                    numberSave<=numberSave-sw;
                end
                lastPressedU<= btnU;
                
                if(lastPressedL==0 && btnL==1) begin
                    numberSave<=numberSave*sw;
                end
                lastPressedL<= btnL;
                
                if(lastPressedR==0 && btnR==1) begin
                    numberSave<=numberSave/sw;
                end
                lastPressedR<= btnR;            
                
    
                freq<=freq+1;            
                    for(i=0;i<16;i = i+1) begin
                        led[i]<=numberSave[i];
                    end  
            end
    end
    
    
    endmodule
