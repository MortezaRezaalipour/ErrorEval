from numpy import random
from src.argument import Arguments
from src.verilog import Verilog
from src.z3solver import Z3solver


def main():
    args = Arguments.parse()
    print(f'{args = }')

    # 1) create testbench and samples
    verilog_obj = Verilog(args.benchmark_name)
    my_max = 2 ** verilog_obj.num_inputs - 1
    rand_array = random.randint(0, my_max, size=args.num_samples)
    verilog_obj.set_samples(rand_array)
    verilog_obj.create_test_bench()
    # 2) run testbench on the samples and store the results
    verilog_obj.run_test_bench()

    # 3) create z3py script
    z3py_obj = Z3solver(args.benchmark_name)
    z3py_obj.set_samples(rand_array)
    z3py_obj.convert_gv_to_z3pyscript_Maxerror()
    z3py_obj.export_z3pyscript()

    # 4) run z3py script and store the results
    z3py_obj.run_z3pyscript()

    # 5) compare the results
    count = 0
    if len(z3py_obj.sample_results) == len(verilog_obj.sample_results):
        print(f'TEST -> PASS')
        for idx, res in enumerate(z3py_obj.sample_results):
            if z3py_obj.sample_results[idx] == verilog_obj.sample_results[idx]:
                count += 1
            else:
                print(f'ERROR!!!')

        if count == len(verilog_obj.sample_results):
            print(f'TEST -> PASS')
        else:
            print(f'{count = }')
    else:
        print(f'ERROR!!!')


if __name__ == "__main__":
    main()
