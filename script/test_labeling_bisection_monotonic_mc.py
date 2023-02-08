import numpy as np
from numpy import random
from src.graph import Graph
from src.verilog import Verilog
from src.z3solver import Z3solver
from src.argument import Arguments
from src.utils import *
from src.config import *


def main():
    args = Arguments.parse()
    print(f'{args = }')

    # 1) create a clean verilog out of exact and approximate circuits
    verilog_obj = Verilog(args.benchmark_name)
    verilog_obj.export_circuit()

    convert_verilog_to_gv(args.benchmark_name)

    # 2) convert clean exact and approximate circuits into their gv formats
    graph_obj = Graph(args.benchmark_name)
    graph_obj.export_graph()

    # 3) create a qor z3py scripts
    z3py_obj = Z3solver(args.benchmark_name)

    my_max = 2 ** z3py_obj.graph.num_inputs - 1
    if 2 ** z3py_obj.graph.num_inputs < args.num_samples:
        print(f'Exhaustive Simulation...')
        rand_array = np.array(range(my_max))
    else:
        print(f'Monte Carlo Simulation...')
        rand_array = random.randint(0, my_max, size=args.num_samples)
    z3py_obj.set_samples(rand_array)

    print(f'labeling with bisection...')
    z3py_obj.convert_gv_to_z3pyscript_maxerror_labeling(BISECTION)
    z3py_obj.export_z3pyscript()
    z3py_obj.run_z3pyscript_labeling()
    print(f'done!')

    print(f'labeling with monotonic...')
    z3py_obj.convert_gv_to_z3pyscript_maxerror_labeling(MONOTONIC)
    z3py_obj.export_z3pyscript()
    z3py_obj.run_z3pyscript_labeling()
    print(f'done!')

    print(f'labeling with mc over {args.num_samples} samples...')
    z3py_obj.convert_gv_to_z3pyscript_maxerror_labeling(MC)
    z3py_obj.export_z3pyscript()
    z3py_obj.run_z3pyscript_labeling()
    print(f'done!')


if __name__ == "__main__":
    main()
