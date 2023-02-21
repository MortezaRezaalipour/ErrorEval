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

    # 2) Collect all the results mc, bisection, and monotonic
    # specs_mc = Specs(args.benchmark_name, args.approximate_benchmark, args.experiment, MC, None, None)
    specs_solver = Specs(args.benchmark_name, args.approximate_benchmark, args.experiment, args.strategy, metric=args.metric, precision=args.precision, optimization=None)
    specs_optimize = Specs(args.benchmark_name, args.approximate_benchmark, args.experiment, args.strategy, metric=args.metric, precision=args.precision, optimization=OPTIMIZE)
    specs_maximize = Specs(args.benchmark_name, args.approximate_benchmark, args.experiment, args.strategy, metric=args.metric, precision=args.precision, optimization=MAXIMIZE)


    # result_mc = Result(specs_mc)
    result_solver = Result(specs_solver)
    result_optimize = Result(specs_optimize)
    result_maximize = Result(specs_maximize)


    assert (len(result_solver.reports) == len(result_optimize.reports) and len(result_maximize.reports) == len(result_solver.reports))
    print(f'TEST -> OK')

    count = 0
    for idx, report in enumerate(result_optimize.reports):
        if (float(result_solver.reports[idx].wce) == float(result_optimize.reports[idx].wce) and
            float(result_solver.reports[idx].wce) == float(result_maximize.reports[idx].wce)):
            count += 1
        else:
            print(f'ERROR!')
            print(f'{result_solver.reports[idx].file_path = }')
            print(f'{result_optimize.reports[idx].file_path = }')
            print(f'{result_maximize.reports[idx].file_path = }')

            print(f'for file id{idx}')
            print(f'{float(report.wce) = }')
            print(f'{float(result_solver.reports[idx].wce) = }')
            print(f'{float(result_optimize.reports[idx].wce) = }')
            print(f'{float(result_maximize.reports[idx].wce) = }')
            break
    if count == len(result_optimize.reports):
        print(f'TEST -> OK')
        with open(f'{args.benchmark_name}_{args.metric}', 'w') as f:
            f.write('PASSED!')


if __name__ == "__main__":
    main()