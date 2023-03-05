#!/bin/bash


for BENCH in input/ver/*.v
  do
#    cd ../../
    echo $BENCH
    # without optimization
    python3 script/verify_z3.py $BENCH


  done