#!/bin/bash



for BENCH in input/ver/*.v
  do
#    cd ../../
    echo $BENCH
    # run label gates monotonic
    python3 script/label_gates.py $BENCH -strategy monotonic -metric wae
    # run label gates biseciton
    python3 script/label_gates.py $BENCH -strategy bisection -metric wae
    # compare them
    python3 script/test_results_mc_bisection_monotonic.py $BENCH

  done
