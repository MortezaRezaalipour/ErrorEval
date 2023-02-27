#!/bin/bash


METRIC=$1
for BENCH in input/ver/*.v
  do

    echo $BENCH

    # run bisection
    python3 script/label_gates.py $BENCH -strategy kind -metric $METRIC
    # run kind bisection
    python3 script/label_gates.py $BENCH -strategy bisection -metric $METRIC

    # run kind bisection
    python3 script/label_gates.py $BENCH -strategy monotonic -metric $METRIC
    # compare them
    python3 script/test_results_mc_bisection_monotonic.py $BENCH -metric $METRIC

  done
