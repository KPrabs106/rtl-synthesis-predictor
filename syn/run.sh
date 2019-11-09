#!/bin/bash

export design_name=$1 
dc_shell -f 00_run.tcl 2>&1 | tee output.log
