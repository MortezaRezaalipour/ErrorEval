import os
import re
import natsort

from typing import List
from copy import deepcopy

from src.stats import Stats
from src.specs import Specs
from src.config.path import *
from src.utils import *


class Result:
    def __init__(self, specifications: Specs):
        self.__benchmark: str = get_pure_name(specifications.benchmark)
        self.__approximate_benchmark: str = get_pure_name(specifications.approximate_benchmark)
        self.__experiment: str = specifications.experiment
        self.__strategy: str = specifications.strategy
        self.__optimization: str = specifications.optimization
        self.__metric: str = specifications.metric
        self.__precision: int = specifications.precision
        self.__in_paths: List[str] = self.find_input_report_paths()

        self.__reports: List[Stats] = self.import_reports()

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
    def reports(self):
        return self.__reports

    @reports.setter
    def reports(self, reports: List[Stats]):
        self.__reports = deepcopy(reports)

    @property
    def in_paths(self):
        return self.__in_paths

    #TODO
    # fix naming: include num_samples and metric

    def find_relevant_csv(self):
        relevant_csv = []
        folder, extension = INPUT_PATH['report']

        if self.metric == WRE:
            if (self.optimization == OPTIMIZE or self.optimization == MAXIMIZE) and (self.strategy != BISECTION):
                cur_dir = f'{folder}/{self.benchmark}_{self.experiment}_{self.metric}_d{self.precision}_{self.strategy}_{self.optimization}'
            else:
                cur_dir = f'{folder}/{self.benchmark}_{self.experiment}_{self.metric}_d{self.precision}_{self.strategy}'
        else:
            if self.optimization == OPTIMIZE or self.optimization == MAXIMIZE and (self.strategy != BISECTION):
                cur_dir = f'{folder}/{self.benchmark}_{self.experiment}_{self.metric}_{self.strategy}_{self.optimization}'
            else:
                cur_dir = f'{folder}/{self.benchmark}_{self.experiment}_{self.metric}_{self.strategy}'

        all_csv = [f for f in os.listdir(cur_dir)]
        for f in all_csv:
            if f.endswith(extension):
                relevant_csv.append(f'{cur_dir}/{f}')

        relevant_csv = natsort.natsorted(relevant_csv) # sorting the files alphabetically in descending order
        return relevant_csv

    def find_input_report_paths(self):
        input_paths = []
        folder, extension = INPUT_PATH['report']
        if self.experiment == SINGLE:
            input_paths = self.find_relevant_csv()
        elif self.experiment == QOR:
            if self.metric == WRE:
                if self.optimization == OPTIMIZE or self.optimization == MAXIMIZE and (self.strategy != BISECTION):
                    input_paths.append(f'{folder}/{self.approximate_benchmark}_{self.experiment}_{self.metric}_d{self.precision}_{self.strategy}_{self.optimization}.{extension}')
                else:
                    input_paths.append(f'{folder}/{self.approximate_benchmark}_{self.experiment}_{self.metric}_d{self.precision}_{self.strategy}.{extension}')
            else:
                if self.optimization == OPTIMIZE or self.optimization == MAXIMIZE and (self.strategy != BISECTION):
                    input_paths.append(f'{folder}/{self.approximate_benchmark}_{self.experiment}_{self.metric}_{self.strategy}_{self.optimization}.{extension}')
                else:
                    input_paths.append(f'{folder}/{self.approximate_benchmark}_{self.experiment}_{self.metric}_{self.strategy}.{extension}')

        elif self.experiment == RANDOM:
            pass

        return input_paths

    def import_reports(self):
        reports: List = []
        for report_path in self.in_paths:
            reports.append(Stats(report_path))
        return reports

    #TODO
    # Create iterator object
    def __iter__(self):
        pass

    def __next__(self):
        pass

    def __repr__(self):
        return f'An object of class Result\n' \
               f'{self.benchmark = }\n' \
               f'{self.approximate_benchmark = }\n' \
               f'{self.experiment = }\n' \
               f'{self.strategy = }\n' \
               f'{self.metric = }\n'

    def __len__(self):
        return len(self.__dict__)
