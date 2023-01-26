from z3 import *
from numpy import random
from src.argument import Arguments
from src.graph import Graph
from src.utils import *
from src.z3solver import Z3solver


def gv2z3():
    args = Arguments.parse()
    print(f'{args = }')

    z3py_obj = Z3solver(args.benchmark_name)
    print(f'{z3py_obj.graph.num_inputs = }')
    mymax = 2 ** z3py_obj.graph.num_inputs - 1
    rand_array = random.randint(0, mymax, size=args.num_samples)
    z3py_obj.set_samples(rand_array)
    z3py_obj.convert_gv_to_z3pyscript_test()
    z3py_obj.export_z3pyscript()
if __name__ == "__main__":
    gv2z3()
