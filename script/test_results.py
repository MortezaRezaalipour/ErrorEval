from src.result import Result
from src.stats import Stats
from src.specs import Specs
from src.argument import Arguments
from src.config.config import *

def main():
    # csv_path = 'output/report/abs_diff_i16_o9_single_gate_removal_bisection/abs_diff_i16_o9_single_gate_removal_bisection_g1.csv'
    # my_stats = Stats(csv_path)

    args = Arguments.parse()

    specs = Specs(args.benchmark_name, None,
                  SINGLE, MC,
                  None, None)
    print(f'{specs = }')

    result = Result(specs)




if __name__ == "__main__":
    main()
