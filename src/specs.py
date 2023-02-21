from src.config.path import *
from src.config.config import *


class Specs():
    def __init__(self, benchmark, approx_benchmark=None, experiment=None, strategy=MONOTONIC, metric=WAE,
                 num_samples=None, precision=2, optimization=None):
        self.__benchmark: str = benchmark
        self.__approximate_benchmark: str = approx_benchmark

        self.__experiment: str = experiment
        self.__strategy: str = strategy
        self.__optimization: str = optimization

        self.__metric: str = metric
        self.__precision: int = precision
        self.__num_samples: str = num_samples

    @property
    def benchmark(self):
        return self.__benchmark

    @property
    def approximate_benchmark(self):
        return self.__approximate_benchmark

    @property
    def experiment(self):
        return self.__experiment

    @property
    def strategy(self):
        return self.__strategy

    @property
    def optimization(self):
        return self.__optimization

    @property
    def metric(self):
        return self.__metric

    @property
    def precision(self):
        return self.__precision

    @property
    def num_samples(self):
        return self.__num_samples

    def __repr__(self):
        return f'An object of class Specs:\n' \
               f'{self.benchmark = }\n' \
               f'{self.approximate_benchmark = }\n' \
               f'{self.experiment = }\n' \
               f'{self.strategy = }\n' \
               f'{self.optimization = }\n' \
               f'{self.metric = }\n' \
               f'{self.precision = }\n' \
               f'{self.num_samples = }' \
               f''
