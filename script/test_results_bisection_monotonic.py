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


    # 2) Collect all the results bisection, and monotonic
    # specs_mc = Specs(args.benchmark_name, args.approximate_benchmark, args.experiment, MC, None, None)
    specs_bisection = Specs(args.benchmark_name, args.approximate_benchmark, args.experiment, BISECTION, metric=args.metric, precision=args.precision, optimization=args.optimization)
    specs_monotonic = Specs(args.benchmark_name, args.approximate_benchmark, args.experiment, MONOTONIC, metric=args.metric, precision=args.precision, optimization=args.optimization)

    # result_mc = Result(specs_mc)
    result_bisection = Result(specs_bisection)
    result_monotonic = Result(specs_monotonic)


    assert len(result_monotonic.reports) == len(result_monotonic.reports)
    print(f'TEST -> OK')

    count = 0
    for idx, report in enumerate(result_monotonic.reports):
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
        with open(f'test/{args.benchmark_name}_{args.metric}', 'w') as f:
            f.write('PASSED!')

if __name__ == "__main__":
    main()
