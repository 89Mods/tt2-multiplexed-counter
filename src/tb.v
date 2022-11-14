`default_nettype none
`timescale 1ns/1ps

module tb (
	input CLK,
	input RST,
	output [6:0] dout,
	output SEL
	);

	initial begin
		$dumpfile ("tb.vcd");
		$dumpvars (0, tb);
		#1;
	end

	wire [7:0] inputs = {6'b0, RST, CLK};
	wire [7:0] outputs;
	assign dout = outputs[6:0];
	assign SEL = outputs[7];

	tt2_tholin_multiplexed_counter tt2_tholin_multiplexed_counter (
		`ifdef GL_TEST
			.vccd1( 1'b1),
			.vssd1( 1'b0),
		`endif
		.io_in (inputs),
		.io_out (outputs)
	);

endmodule
