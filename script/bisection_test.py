from src.graph import Graph
from src.verilog import Verilog
from src.z3solver import Z3solver
from src.argument import Arguments
from src.utils import *
from src.config import *


def main():
    args = Arguments.parse()
    print(f'{args = }')

    verilog_obj = Verilog(args.benchmark_name)
    verilog_obj.export_circuit()

    convert_verilog_to_gv(args.benchmark_name)
    graph_obj = Graph(args.benchmark_name)
    graph_obj.export_graph()

    z3py_obj = Z3solver(args.benchmark_name)
    print(f'labeling with bisection...')
    z3py_obj.convert_gv_to_z3pyscript_maxerror_labeling(BISECTION)
    z3py_obj.export_z3pyscript()
    z3py_obj.run_z3pyscript_labeling()
    print(f'labeling completed!')


if __name__ == "__main__":
    main()
