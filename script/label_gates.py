import subprocess
from src.graph import Graph
from src.verilog import Verilog
from src.z3solver import Z3solver
from src.argument import Arguments
from src.utils import *


def main():
    args = Arguments.parse()
    print(f'{args = }')

    # read input verilog and clean it
    verilog_obj = Verilog(args.benchmark_name)
    verilog_obj.synthesize_to_gate_level()
    verilog_obj.unwrap_variables()

    # convert verilog to gv and clean it
    convert_verilog_to_gv(args.benchmark_name)
    graph_obj = Graph(args.benchmark_name)
    graph_obj.export_graph()

    # convert gv to z3 expression
    z3py_obj = Z3solver(args.benchmark_name)
    print(f'labeling...')
    z3py_obj.convert_gv_to_z3pyscript_maxerror_labeling()
    z3py_obj.run_z3pyscript_labeling()
    print(f'labeling is completed!')


if __name__ == "__main__":
    main()
