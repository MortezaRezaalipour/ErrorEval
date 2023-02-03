from src.graph import Graph
from src.verilog import Verilog
from src.z3solver import Z3solver
from src.argument import Arguments
from src.utils import *


def main():
    args = Arguments.parse()
    print(f'{args = }')

    verilog_obj = Verilog(args.benchmark_name)
    verilog_obj.export_circuit()

    convert_verilog_to_gv(args.benchmark_name)
    graph_obj = Graph(args.benchmark_name)
    graph_obj.export_graph()



if __name__ == "__main__":
    main()
