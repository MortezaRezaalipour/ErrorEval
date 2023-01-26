import sys
from src.argument import Arguments
from src.graph import Graph
from src.utils import *


def v2gv():
    args = Arguments.parse()
    print(f'{args = }')

    convert_verilog_to_gv(args.benchmark_name)

    graph_obj = Graph(args.benchmark_name)
    print(f'{graph_obj = }')


    graph_obj.export_graph()



if __name__ == "__main__":
    v2gv()
