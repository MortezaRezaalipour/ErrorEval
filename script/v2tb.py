from src.argument import Arguments
from src.verilog import Verilog
from numpy import random
import numpy as np

def main():
    args = Arguments.parse()
    print(f'{args  = }')

    verilog_obj = Verilog(args.benchmark_name)

    my_max = 2 ** verilog_obj.num_inputs - 1
    if 2 ** verilog_obj.num_inputs < args.num_samples:
        print(f'Exhaustive Simulation...')
        rand_array = np.array(range(my_max))
    else:
        print(f'Monte Carlo Simulation...')
        rand_array = random.randint(0, my_max, size=args.num_samples)


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
