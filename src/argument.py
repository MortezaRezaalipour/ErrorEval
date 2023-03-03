import argparse
import sys
from src.utils import *
import typing


class Arguments:
    def __init__(self, tmp_args: argparse):
        benchmark = get_pure_name(tmp_args.benchmark)
        approximate_benchmark = get_pure_name(tmp_args.approximate_benchmark)
        self.__benchmark_name: str = benchmark
        self.__approximate_benchmark: str = approximate_benchmark
        self.__mc_samples: int = tmp_args.samples
        self.__metric: str = tmp_args.metric
        self.__precision: int = tmp_args.precision
        self.__strategy: str = tmp_args.strategy
        self.__optimization: str = tmp_args.optimization
        self.__experiment: str = tmp_args.experiment
        self.__pruning_percentage: int = tmp_args.pruning_percentage
        self.__clean = tmp_args.clean

    @property
    def benchmark_name(self):
        return self.__benchmark_name

    @property
    def approximate_benchmark(self):
        return self.__approximate_benchmark

    @property
    def num_samples(self):
        return self.__mc_samples

    @property
    def metric(self):
        return self.__metric

    @property
    def precision(self):
        return self.__precision

    @property
    def strategy(self):
        return self.__strategy

    @property
    def optimization(self):
        return self.__optimization

    @property
    def experiment(self):
        return self.__experiment

    @property
    def pruning_percentage(self):
        return self.__pruning_percentage

    # @property
    # def approach(self):
    #     return self.__approach

    @property
    def clean(self):
        return self.__clean

    def __repr__(self):
        return f'An object of class Arguments\n' \
               f'{self.benchmark_name = }\n' \
               f'{self.approximate_benchmark = }\n' \
               f'{self.num_samples = }\n' \
               f'{self.metric = }\n' \
               f'{self.precision = }\n' \
               f'{self.strategy = }\n' \
               f'{self.optimization = }\n' \
               f'{self.experiment = }\n' \
               f'{self.pruning_percentage = }\n' \
               f'{self.clean = }\n'

    @classmethod
    def parse(cls):
        my_parser = argparse.ArgumentParser(description='converts different formats to one another',
                                            prog=sys.argv[0],
                                            usage='%(prog)s benchmark-name|benchmark-path')

        my_parser.add_argument('benchmark',
                               type=str,
                               default=None,
                               help='benchmark-name')

        my_parser.add_argument('--samples', '-s',
                               default=100,
                               type=int,
                               help='number-of-monte-carlo-samples')
        my_parser.add_argument('--approximate_benchmark', '-app',
                               type=str,
                               default=None,
                               help='approximate-benchmark-name in gv/verilog format')
        my_parser.add_argument('--metric', '-metric',
                               type=str,
                               default=WAE,
                               help='the-desired-worst-case-error-metric')
        my_parser.add_argument('--precision', '-p',
                               type=int,
                               default=2,
                               help='number-of-decimal-points-for-wre')
        my_parser.add_argument('--strategy', '-strategy',
                               type=str,
                               default=MONOTONIC,
                               help='the-solver-strategy-to-find-metric')
        my_parser.add_argument('--optimization', '-opt',
                               type=str,
                               default=None,
                               help='the-solver-optimization (Solver, Optimize, Maximize)')
        my_parser.add_argument('--experiment', '-e',
                               type=str,
                               default=SINGLE,
                               help="the-experiment-name [SINGLE|QOR|RANDOM]")
        my_parser.add_argument('--pruning_percentage', '-pp',
                               type=int,
                               default=10,
                               help='gate-percentage-carved-out')

        my_parser.add_argument('--clean',
                               type=bool,
                               default=False)

        tmp_args = my_parser.parse_args()

        return Arguments(tmp_args)
