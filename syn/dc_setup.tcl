#set SYN  /afs/ir/class/ee/synopsys/syn/M-2016.12-SP2/libraries/syn/
set OPENCELL_45 ../lib

set link_library [list NangateOpenCellLibrary.db dw_foundation.sldb] 
#set link_library [list standard.sldb gtech.db dw_foundation.sldb] 
set target_library [list NangateOpenCellLibrary.db] 
#set target_library [list gtech.db] 
set symbol_library [list generic.slib]
set synthetic_library [list dw_foundation.sldb] 

set search_path [list ./ ../rtl ../rtl /cad/synopsys/syn/L-2016.03-SP5-5/libraries/syn/ ../lib]

file mkdir $syn_dir/work
define_design_lib work -path $syn_dir/work
set alib_library_analysis_path $syn_dir

#set tluplus_path ../lib/NangateOpenCellLibrary.tluplus

#set tech_file ../lib/NangateOpenCellLibrary.tf 
#set map_file ../lib/NangateOpenCellLibrary.map

#set mw_reference_libraries  ../../lib/NangateOpenCellLibrary

#set mw_design_library $syn_dir/${design_name}_mwlib

#file delete -force $mw_design_library

#create_mw_lib -technology $tech_file -mw_reference_library $mw_reference_libraries -bus_naming_style {[%d]} $mw_design_library

#open_mw_lib $mw_design_library

#check_library

#set_tlu_plus_files -max_tluplus $max_tlu_file  -tech2itf_map $prs_map_file

#check_tlu_plus_files
