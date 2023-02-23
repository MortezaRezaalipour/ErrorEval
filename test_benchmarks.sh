#!/bin/bash


METRIC=$1
for BENCH in input/ver/*.v
  do
#    cd ../../
    echo $BENCH
    # run label gates monotonic
    python3 script/label_gates.py $BENCH -strategy monotonic -metric $METRIC
    # run label gates biseciton
    python3 script/label_gates.py $BENCH -strategy bisection -metric $METRIC
    # run label gates kind
    python3 script/label_gates.py $BENCH -strategy kind -metric $METRIC
    # compare them
    python3 script/test_results_mc_bisection_monotonic.py $BENCH -metric $METRIC

  done

