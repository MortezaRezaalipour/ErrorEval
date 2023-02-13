import argparse
import sys
from src.utils import *


class Arguments:
    def __init__(self, tmp_args):

        benchmark = get_pure_name(tmp_args.benchmark)
        approximate_benchmark = get_pure_name(tmp_args.approximate_benchmark)
        self.__benchmark_name = benchmark
        self.__approximate_benchmark = approximate_benchmark
        self.__mc_samples = tmp_args.samples
        self.__wce = tmp_args.wce
        self.__strategy = tmp_args.strategy
        self.__experiment = tmp_args.experiment
        self.__pruning_percentage = tmp_args.pruning_percentage
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
    def wce(self):
        return self.__wce

    @property
    def strategy(self):
        return self.__strategy

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
               f'{self.wce = }\n' \
               f'{self.strategy = }\n' \
               f'{self.experiment = }\n' \
               f'{self.pruning_percentage = }\n' \
               f'{self.clean = }\n' \


    @classmethod
    def parse(cls):
        my_parser = argparse.ArgumentParser(description='converts different formats to one another',
                                            prog=sys.argv[0],
                                            usage='%(prog)s benchmark-name|benchmark-path')

        my_parser.add_argument('benchmark',
                               type=str,
                               help='benchmark-name')

        my_parser.add_argument('--samples', '-s',
                               default=100,
                               type=int,
                               help='number-of-monte-carlo-samples')
        my_parser.add_argument('--approximate_benchmark', '-app',
                               type=str,
                               default=None,
                               help='approximate-benchmark-name in gv/verilog format')
        my_parser.add_argument('--wce', '-metric',
                               type=str,
                               default=WAE,
                               help='the-desired-worst-case-error-metric')
        my_parser.add_argument('--strategy', '-strategy',
                               type=str,
                               default=MONOTONIC,
                               help='the-solver-strategy-to-find-wce')
        my_parser.add_argument('--experiment', '-e',
                               type=str,
                               default=SINGLE,
                               help="the-experiment-name [SINGLE|QOR|RANDOM]")
        my_parser.add_argument('--pruning_percentage', '-pp',
                               type=int,
                               default=10,
                               help='gate-percentage-carved-out')
        # my_parser.add_argument('--approach', '-a',
        #                        type=str,
        #                        default='exact',
        #                        help='exact or monte carlo')
        my_parser.add_argument('--clean',
                               type=bool,
                               default=False)

        tmp_args = my_parser.parse_args()

        return Arguments(tmp_args)
