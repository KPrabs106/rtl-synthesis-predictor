#!/bin/bash

N=10
(
for i in `cat names`
do 
   ((j=j%N)); ((j++==0)) && wait
   ./run.sh $i & 
done
)
