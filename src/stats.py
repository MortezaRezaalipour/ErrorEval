import csv
import re
from src.config.config import *


class Stats:
    def __init__(self, file_path: str):
        """
        stores a csv file contents as a an object where each row of the csv file is an attribute
        :param file_path: the path to a csv file
        """
        self.__name = None
        self.__experiment = None
        self.__wce = None
        self.___runtime = None
        self.__sat_runtime = None
        self.__unsat_runtime = None
        self.__num_sats = None
        self.__num_unsats = None
        self.__jumps = None
        self.__file_in_path = file_path
        self.import_csv()

    @property
    def name(self):
        return self.__name

    @property
    def path(self):
        return self.__file_in_path

    @property
    def experiment(self):
        return self.__experiment

    @experiment.setter
    def experiment(self, experiment):
        self.__experiment = experiment

    @property
    def wce(self):
        return self.__wce

    @wce.setter
    def wce(self, wce):
        self.__wce = wce

    @property
    def total_runtime(self):
        return self.___runtime

    @total_runtime.setter
    def total_runtime(self, total_runtime):
        self.___runtime = total_runtime

    @property
    def sat_runtime(self):
        return self.__sat_runtime

    @sat_runtime.setter
    def sat_runtime(self, sat_runtime):
        self.__sat_runtime = sat_runtime

    @property
    def num_sats(self):
        return self.__num_sats

    @num_sats.setter
    def num_sats(self, num_sats):
        self.__num_sats = num_sats

    @property
    def unsat_runtime(self):
        return self.__unsat_runtime

    @unsat_runtime.setter
    def unsat_runtime(self, unsat_runtime):
        self.__unsat_runtime = unsat_runtime

    @property
    def num_unsats(self):
        return self.__num_unsats

    @num_unsats.setter
    def num_unsats(self, num_unsats):
        self.__num_unsats = num_unsats

    @property
    def jump_list(self):
        return self.__jumps

    @jump_list.setter
    def jump_list(self, jump_list):
        self.__jumps = jump_list

    def import_csv(self):
        with open(self.path, 'r') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                if re.search(EXPERIMENT, row[0]):
                    self.experiment = row[1]
                elif re.search(WCE, row[0]):
                    self.wce = row[1]
                elif re.search(TOTAL_RUNTIME, row[0]):
                    self.total_runtime = row[1]
                elif re.search(SAT_RUNTIME, row[0]):
                    self.sat_runtime = row[1]
                elif re.search(UNSAT_RUNTIME, row[0]):
                    self.unsat_runtime = row[1]
                elif re.search(N_SATS, row[0]):
                    self.num_sats = row[1]
                elif re.search(N_UNSATS, row[0]):
                    self.num_unsats = row[1]
                elif re.search(JUMPS, row[0]):
                    self.jump_list = row[1]


    def __repr__(self):
        return f'An object of class Stats:\n' \
               f'{self.name = }\n' \
               f'{self.experiment = }\n' \
               f'{self.wce = }\n' \
               f'{self.total_runtime = }\n' \
               f'{self.sat_runtime = }\n' \
               f'{self.unsat_runtime}\n' \
               f'{self.num_sats = }\n' \
               f'{self.num_unsats = }\n' \
               f'{self.jump_list = }\n' \
               f''
