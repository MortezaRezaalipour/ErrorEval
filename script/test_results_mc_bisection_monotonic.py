import numpy as np
from src.result import Result
from src.specs import Specs
from src.argument import Arguments
from src.config.config import *
from src.verilog import Verilog
from src.graph import Graph
from src.z3solver import Z3solver
from src.utils import *
from numpy import random


def main():
    args = Arguments.parse()
    print(f'{args = }')

    verilog_obj = Verilog(args.benchmark_name)
    verilog_obj.export_circuit()

    convert_verilog_to_gv(args.benchmark_name)
    graph_obj = Graph(args.benchmark_name)
    graph_obj.export_graph()

    # 1) Run the experiment
    if args.experiment == RANDOM:
        # create pruned gates list
        num_pruned_gates = args.pruning_percentage * (graph_obj.num_inputs + graph_obj.num_gates) // 100
        pruned_gates = random.randint(0, graph_obj.num_inputs + graph_obj.num_gates, size=num_pruned_gates)

        # convert gv to z3 expression
        z3py_obj = Z3solver(args.benchmark_name, pruned_gates=pruned_gates, experiment=args.experiment,
                            metric=args.metric)
        z3py_obj.convert_gv_to_z3pyscript_maxerror_random_pruning(MONOTONIC)
        z3py_obj.run_z3pyscript_random()
        z3py_obj.convert_gv_to_z3pyscript_maxerror_random_pruning(BISECTION)
        z3py_obj.run_z3pyscript_random()

        my_max = 2 ** z3py_obj.graph.num_inputs - 1
        if 2 ** z3py_obj.graph.num_inputs < args.num_samples:
            print(f'Exhaustive Simulation...')
            rand_array = np.array(range(my_max))
        else:
            print(f'Monte Carlo Simulation...')
            rand_array = random.randint(0, my_max, size=args.num_samples)
        z3py_obj.set_samples(rand_array)
        z3py_obj.convert_gv_to_z3pyscript_maxerror_random_pruning(MC)
        z3py_obj.run_z3pyscript_random()

    # 2) Collect all the results mc, bisection, and monotonic
    # specs_mc = Specs(args.benchmark_name, args.approximate_benchmark, args.experiment, MC, None, None)
    specs_bisection = Specs(args.benchmark_name, args.approximate_benchmark, args.experiment, BISECTION, metric=args.metric, precision=args.precision, optimization=args.optimization)
    specs_monotonic = Specs(args.benchmark_name, args.approximate_benchmark, args.experiment, MONOTONIC, metric=args.metric, precision=args.precision, optimization=args.optimization)

    # result_mc = Result(specs_mc)
    result_bisection = Result(specs_bisection)
    result_monotonic = Result(specs_monotonic)


    # assert len(result_mc.reports) == len(result_bisection.reports) and len(result_mc.reports) == len(
    #     result_monotonic.reports)
    assert len(result_monotonic.reports) == len(
        result_monotonic.reports)
    print(f'TEST -> OK')

    count = 0
    for idx, report in enumerate(result_monotonic.reports):
        # if (float(report.metric) <= float(result_bisection.reports[idx].metric) == float(result_monotonic.reports[idx].metric)):
        if float(result_bisection.reports[idx].wce) == float(result_monotonic.reports[idx].wce):
            count += 1
        else:
            print(f'ERROR!')
            print(f'{result_monotonic.reports[idx].file_path = }')
            print(f'{result_bisection.reports[idx].file_path = }')
            print(f'for file id{idx}')
            print(f'{float(report.wce) = }')
            print(f'{float(result_bisection.reports[idx].wce) = }')
            print(f'{float(result_monotonic.reports[idx].wce) = }')
            break
    if count == len(result_monotonic.reports):
        print(f'TEST -> OK')
        with open(f'{args.benchmark_name}_{args.metric}', 'w') as f:
            f.write('PASSED!')


if __name__ == "__main__":
    main()
