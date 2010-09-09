template = """/*
    Auto Generated by Tizzy
    =======================
    File:           $filename
    Generated on:   $creation_date

    $title
*/
`timescale 1ns / 100ps
`ifndef D
    `define D #1
`endif

module $module_name (
    input   wire clock,
    input   wire reset,
$inputs
    output  reg [$msb,$lsb] state,
    output  reg [$msb,$lsb] state_next
);

/* State parameters for 1-hot encoding */
/* These parameters are indexes to the state reg */
localparam
$state_params

/* Next State Logic */
always @(*) begin
    state_next = $range'b0;
    case (1'b1)
$next_state_logic
    endcase
end

/* State Generator */
always @(posedge clock or posedge reset)
    if(reset) begin
$state_generator
    end
    else
        state <= `D state_next;
endmodule

/*

$digraph

*/
"""