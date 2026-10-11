// ch13_timing.sdc -- timing constraints the tools actually check.
// 27 MHz = 37.037 ns period; everything else is derived from this one line.
create_clock -name clk -period 37.037 [get_ports clk]
// inputs arrive from outside: say how late they can be (25% of a clock)
set_input_delay -clock clk 9.0 [all_inputs]
set_output_delay -clock clk 9.0 [all_outputs]
