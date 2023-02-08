from src.result import Result
from src.stats import Stats
from src.specs import Specs
from src.argument import Arguments
from src.config.config import *


def main():
    args = Arguments.parse()
    print(f'{args = }')
    specs = Specs(args.benchmark_name, args.approximate_benchmark, args.experiment, args.strategy, None, None)

    result = Result(specs)




if __name__ == "__main__":
    main()
