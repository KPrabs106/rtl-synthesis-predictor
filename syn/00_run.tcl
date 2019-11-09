set_host_options -max_cores 8

set user_name $::env(USER)
set design_name $::env(design_name) 

set rtl_dir ../rtl
set syn_dir ./$design_name

file mkdir $syn_dir

source -echo dc_setup.tcl
source -echo synth.tcl
