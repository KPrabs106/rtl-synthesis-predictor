set fname ../generic/${design_name}.v

analyze -format verilog -lib work $fname
#read_file -format verilog $fname
#read_file -format verilog $fname
echo [get_designs]
elaborate $design_name
#elaborate DW01_add -library DW01 -parameters "width=8"
link

write -format verilog -output ./top.v

# Apply timing constraints
source ./constraints.tcl

set_fix_multiple_port_nets -outputs -exclude_clock_network

compile_ultra
#compile_ultra -no_autoungroup -no_seq_output_inversion -gate_clock

remove_unconnected_ports -blast_buses [get_cells -all -hierarchical]

##
## Generate reports
##
reset_timing_derate
cd $design_name
file mkdir ./reports
report_timing -delay_type max -significant_digits 4 > ./reports/timing_report_max
report_timing -delay_type min -significant_digits 4 > ./reports/timing_report_min
report_area > ./reports/area_report
report_power > ./reports/power_report
report_design > ./reports/design_report
report_constraints -all -significant_digits 4 > ./reports/constraints_report
check_design > ./reports/design_check
check_error > ./reports/error_check

##
## Write out retimed netlist
##
change_names -hierarchy -rule verilog
define_name_rules name_rule -allowed "a-z A-Z 0-9 _" -max_length 255 -type cell 
define_name_rules name_rule -allowed "a-z A-Z 0-9 _[]" -max_length 255 -type net
define_name_rules name_rule -map {{"\\*cell\\*" "cell"}}                        
change_names -hierarchy -rules name_rule
uniquify
write -format verilog -hierarchy -output ./top.v
write_sdf ./top.sdf
exit
