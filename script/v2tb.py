from src.argument import Arguments
from src.verilog import Verilog
from numpy import random


def main():
    args = Arguments.parse()
    print(f'{args  = }')

    verilog_obj = Verilog(args.benchmark_name)

    mymax = 2 ** verilog_obj.num_inputs - 1
    rand_array = random.randint(0, mymax, size=args.num_samples)
    #TODO
    # keep in mind that we can have a class for random numbers
    # this way we can be able to generate random numbers with any possible distribution

    #TODO
    # explain the nomenclature of the clean verilog files, the testbenches and the result file (from iverilog)
    verilog_obj.set_samples(rand_array)

    verilog_obj.create_test_bench()

    verilog_obj.run_test_bench()


if __name__ == "__main__":
    main()
