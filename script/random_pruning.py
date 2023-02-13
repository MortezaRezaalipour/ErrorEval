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

    # read input verilog and clean it
    verilog_obj = Verilog(args.benchmark_name)
    verilog_obj.export_circuit()

    # convert verilog to gv and clean it
    convert_verilog_to_gv(args.benchmark_name)
    graph_obj = Graph(args.benchmark_name)
    graph_obj.export_graph()

    # create pruned gates list

    num_pruned_gates = args.pruning_percentage * (graph_obj.num_inputs+graph_obj.num_gates) // 100
    pruned_gates = random.randint(0, graph_obj.num_inputs+graph_obj.num_gates, size=num_pruned_gates)

    # convert gv to z3 expression
    z3py_obj = Z3solver(args.benchmark_name, pruned_gates=pruned_gates, experiment=args.experiment)

    if args.strategy == MC:
        my_max = 2 ** z3py_obj.graph.num_inputs - 1
        if 2 ** z3py_obj.graph.num_inputs < args.num_samples:
            print(f'Exhaustive Simulation...')
            rand_array = np.array(range(my_max))
        else:
            print(f'Monte Carlo Simulation...')
            rand_array = random.randint(0, my_max, size=args.num_samples)

        z3py_obj.set_samples(rand_array)

    print(f'random pruning with {args.strategy}')
    z3py_obj.convert_gv_to_z3pyscript_maxerror_random_pruning(MONOTONIC)
    z3py_obj.run_z3pyscript_random()
    print(f'random pruning is completed!')


if __name__ == "__main__":
    main()
