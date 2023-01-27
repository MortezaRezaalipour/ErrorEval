from src.argument import Arguments
from src.verilog import Verilog


def v2v():
    args = Arguments.parse()
    print(f'{args = }')

    verilog_obj = Verilog(args.benchmark_name)
    print(f'{verilog_obj = }')

    verilog_obj.synthesize_to_gate_level()
    verilog_obj.unwrap_variables()


if __name__ == "__main__":
    v2v()
