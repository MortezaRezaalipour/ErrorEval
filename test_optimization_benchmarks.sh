#!/bin/bash


METRIC=$1
for BENCH in input/ver/*.v
  do
#    cd ../../
    echo $BENCH
    # without optimization
    python3 script/label_gates.py $BENCH -strategy monotonic -metric $METRIC
    # with optimize
    python3 script/label_gates.py $BENCH -strategy monotonic -metric $METRIC -opt optimize
    # with maximize
    python3 script/label_gates.py $BENCH -strategy monotonic -metric $METRIC -opt maximize
    # compare them
    python3 script/test_optimization.py $BENCH -metric $METRIC

  done