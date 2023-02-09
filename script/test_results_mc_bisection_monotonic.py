from src.result import Result
from src.stats import Stats
from src.specs import Specs
from src.argument import Arguments
from src.config.config import *


def main():
    args = Arguments.parse()
    print(f'{args = }')

    specs_mc = Specs(args.benchmark_name, args.approximate_benchmark, args.experiment, MC, None, None)
    specs_bisection = Specs(args.benchmark_name, args.approximate_benchmark, args.experiment, BISECTION, None, None)
    specs_monotonic = Specs(args.benchmark_name, args.approximate_benchmark, args.experiment, MONOTONIC, None, None)

    # 1) Run the experiment
    # Not now

    # 2) Collect all the results mc, bisection, and monotonic
    result_mc = Result(specs_mc)
    result_bisection = Result(specs_bisection)
    result_monotonic = Result(specs_monotonic)

    # 3) Compare them and print TEST -> OK if they are passed!
    print(f'{result_mc = }')
    print(f'{result_bisection = }')
    print(f'{result_monotonic = }')

    assert len(result_mc.reports) == len(result_bisection.reports) and len(result_mc.reports) == len(
        result_monotonic.reports)
    print(f'TEST -> OK')

    for idx, report in enumerate(result_mc.reports):
        if (float(report.wce) <= float(result_bisection.reports[idx].wce) == float(result_monotonic.reports[idx].wce)):
            print(f'TEST -> OK')
        else:
            print(f'ERROR!')
            break


if __name__ == "__main__":
    main()
