import numpy as np
from numpy import random
from src.graph import Graph
from src.verilog import Verilog
from src.z3solver import Z3solver
from src.argument import Arguments
from src.utils import *


def main():
    args = Arguments.parse()
    print(f'{args = }')

    # 1) create a clean verilog out of exact and approximate circuits
    verilog_obj_exact = Verilog(args.benchmark_name)
    verilog_obj_exact.export_circuit()

    verilog_obj_approx = Verilog(args.approximate_benchmark)
    verilog_obj_approx.export_circuit()

    convert_verilog_to_gv(args.benchmark_name)
    convert_verilog_to_gv(args.approximate_benchmark)

    # 2) convert clean exact and approximate circuits into their gv formats
    graph_obj_exact = Graph(args.benchmark_name)
    graph_obj_approx = Graph(args.approximate_benchmark)

    graph_obj_exact.export_graph()
    graph_obj_approx.export_graph()

    # 3) create a qor z3py scripts
    z3py_obj_qor = Z3solver(args.benchmark_name, args.approximate_benchmark)
    if args.strategy is MC:
        my_max = 2 ** z3py_obj_qor.graph.num_inputs - 1
        if 2 ** z3py_obj_qor.graph.num_inputs < args.num_samples:
            print(f'Exhaustive Simulation...')
            rand_array = np.array(range(my_max))
        else:
            print(f'Monte Carlo Simulation...')
            rand_array = random.randint(0, my_max, size=args.num_samples)

        z3py_obj_qor.set_samples(rand_array)


    z3py_obj_qor.convert_gv_to_z3pyscript_maxerror_qor(args.strategy)

    print(f'evaluating the wce with {args.strategy}...')

    z3py_obj_qor.export_z3pyscript()
    z3py_obj_qor.run_z3pyscript_qor()

    print(f'wce is evaluated!')


if __name__ == "__main__":
    main()
