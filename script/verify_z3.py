from numpy import random
import numpy as np
from src.argument import Arguments
from src.verilog import Verilog
from src.z3solver import Z3solver
from src.graph import Graph
from src.utils import *


def main():
    args = Arguments.parse()
    print(f'{args = }')

    # clean and prepare:

    # 1) create testbench and samples
    verilog_obj = Verilog(args.benchmark_name)
    print(f'{verilog_obj = }')

    verilog_obj.synthesize_to_gate_level()
    verilog_obj.unwrap_variables()
    print(f'Synthesized to Gate-level!')
    convert_verilog_to_gv(args.benchmark_name)
    print(f'Converted into a gv by Yosys!')
    graph_obj = Graph(args.benchmark_name)
    print(f'{graph_obj = }')

    graph_obj.export_graph()

    # TODO: Fix it later!
    # To prevent ValueError: high is out of bounds for int64
    if verilog_obj.num_inputs < 64:
        my_max = 2 ** verilog_obj.num_inputs - 1
    else:
        my_max = 2 ** 63 - 1
    print(verilog_obj.num_inputs)
    if 2 ** verilog_obj.num_inputs < args.num_samples:
        print(f'Exhaustive Simulation...')
        rand_array = np.array(range(my_max))
    else:
        print(f'Monte Carlo Simulation...')
        rand_array = random.randint(0, my_max, size=args.num_samples, dtype=np.int64)

    verilog_obj.set_samples(rand_array)
    verilog_obj.create_test_bench()
    # 2) run testbench on the samples and store the results
    verilog_obj.run_test_bench()

    # 3) create z3py script
    z3py_obj = Z3solver(args.benchmark_name)
    z3py_obj.set_samples(rand_array)
    z3py_obj.convert_gv_to_z3pyscript_test()
    z3py_obj.export_z3pyscript()

    # 4) run z3py script and store the results
    z3py_obj.run_z3pyscript_test()

    # 5) compare the results
    count = 0
    if len(z3py_obj.sample_results) == len(verilog_obj.sample_results):
        print(f'TEST -> PASS')
        for idx, res in enumerate(z3py_obj.sample_results):
            if z3py_obj.sample_results[idx] == verilog_obj.sample_results[idx]:
                count += 1
            else:
                print(f'ERROR!!!')

        if count == len(verilog_obj.sample_results):
            print(f'TEST -> PASS')
            with open(f'test/{args.benchmark_name}.txt', 'w') as v:
                v.write('PASSED!')
        else:
            print(f'{count = }')
    else:
        print(f'ERROR!!!')


if __name__ == "__main__":
    main()
