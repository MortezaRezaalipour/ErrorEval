import numpy as np
import os
import copy
from typing import *
import networkx as nx
from subprocess import PIPE
from src.utils import *
from src.graph import *


class Z3solver:
    def __init__(self, benchmark_name: str, approximate_benchmark_name: str = None, samples: list = [],
                 experiment: str = SINGLE,
                 pruned_percentage: int = None, pruned_gates=None, metric: str = WAE, precision: int = 4,
                 optimization: str = None):
        """

        :param benchmark_name: the input benchmark in gv format
        :param approximate_benchmark_name: the approximate benchmark in gv format
        :param samples: number of samples for the mc evaluation; by defaults it is an empty list
        """
        self.__circuit_name = get_pure_name(benchmark_name)

        folder, extension = OUTPUT_PATH['gv']
        self.__graph_in_path = f'{folder}/{benchmark_name}.{extension}'

        self.__graph = Graph(benchmark_name, True)

        self.__pyscript_results_out_path = None

        folder, extension = LOG_PATH['z3']
        os.makedirs(f'{folder}/{benchmark_name}_{Z3}_{LOG}', exist_ok=True)
        self.__z3_log_path = f'{folder}/{benchmark_name}_{Z3}_{LOG}/{benchmark_name}_{Z3}_{LOG}.{extension}'

        self.__approximate_verilog_in_path = None
        self.__approximate_graph = None

        if approximate_benchmark_name:
            self.__approximate_circuit_name = approximate_benchmark_name
            folder, extension = INPUT_PATH['app_gv']
            self.__approximate_verilog_in_path = f'{folder}/{approximate_benchmark_name}.{extension}'
            self.__approximate_graph = Graph(approximate_benchmark_name, True)
            self.relabel_approximate_graph()
            self.approximate_graph.set_input_dict(self.approximate_graph.extract_inputs())
            self.approximate_graph.set_output_dict(self.approximate_graph.extract_outputs())
            self.approximate_graph.set_gate_dict(self.approximate_graph.extract_gates())
            self.approximate_graph.set_constant_dict(self.approximate_graph.extract_constants())

        self.__experiment = experiment
        self.__pruned_percentage = None
        # TODO
        # Later create and internal method that can generate pruned gates
        self.__pruned_gates = None
        if experiment == RANDOM:
            self.__pruned_percentage = pruned_percentage
            self.__pruned_gates = pruned_gates

        self.__metric = metric
        self.__precision = precision

        self.__z3_report = None

        self.__samples = samples
        self.__sample_results = None

        self.__z3string = None

        self.__z3pyscript = None

        self.__strategy = None

        self.__optimization = optimization

        self.__pyscript_files_for_labeling: list = []

        self.__z3_out_path = None

    @property
    def name(self):
        return self.__circuit_name

    @property
    def approximate_benchmark(self):
        return self.__approximate_circuit_name

    @property
    def graph_in_path(self):
        return self.__graph_in_path

    @property
    def out_path(self):
        return self.__z3_out_path

    def set_out_path(self, out_path: str):
        self.__z3_out_path = out_path

    @property
    def z3_log_path(self):
        return self.__z3_log_path

    @property
    def approximate_in_path(self):
        return self.__approximate_verilog_in_path

    @property
    def z3pyscript(self):
        return self.__z3pyscript

    @property
    def strategy(self):
        return self.__strategy

    def set_strategy(self, strategy: str):
        self.__strategy = strategy

    @property
    def optimization(self):
        return self.__optimization

    @optimization.setter
    def optimization(self, optimization):
        self.__optimization = optimization

    @property
    def metric(self):
        return self.__metric

    @metric.setter
    def metric(self, metric):
        self.__metric = metric

    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision):
        self.__precision = precision

    @property
    def experiment(self):
        return self.__experiment

    @experiment.setter
    def experiment(self, experiment):
        print(f'{experiment = }')
        self.__experiment = experiment

    @property
    def pruned_percentage(self):
        return self.__pruned_percentage

    @pruned_percentage.setter
    def pruned_percentage(self, pruned_percentage):
        self.__pruned_percentage = pruned_percentage

    @property
    def pruned_gates(self):
        return self.__pruned_gates

    @pruned_gates.setter
    def pruned_gates(self, pruned_gates: List[int]):
        self.__pruned_gates = pruned_gates

    @property
    def z3_report(self):
        return self.__z3_report

    def set_z3_report(self, z3_report: str):
        self.__z3_report = z3_report

    @property
    def pyscript_files_for_labeling(self):
        return self.__pyscript_files_for_labeling

    def set_pyscript_files_for_labeling(self, pyscript_files_for_labeling):
        self.__pyscript_files_for_labeling = pyscript_files_for_labeling

    def append_pyscript_files_for_labeling(self, pyscript_file):
        self.__pyscript_files_for_labeling.append(pyscript_file)

    # TODO

    @property
    def z3string(self):
        return self.__z3string

    @property
    def samples(self):
        return self.__samples

    def set_samples(self, samples: np.array or list):
        self.__samples = samples

    @property
    def sample_results(self):
        return self.__sample_results

    def set_sample_results(self, results):
        self.__sample_results = results

    def import_results(self):
        # print(f'importing results...')
        arr = []
        with open(self.pyscript_results_out_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.replace('\n', '')
                arr.append(int(line))
        results = np.array(arr)
        return results

    def append_z3string(self, new_string):
        self.__z3string = f'{self.__z3string}\n' \
                          f'{new_string}'

    def set_z3string(self, new_string):
        self.__z3string = new_string

    @property
    def pyscript_results_out_path(self):
        return self.__pyscript_results_out_path

    def set_pyscript_results_out_path(self, pyscript_results_out_path: str):
        self.__pyscript_results_out_path = pyscript_results_out_path

    @property
    def graph(self):
        return self.__graph

    @property
    def approximate_graph(self):
        return self.__approximate_graph

    def set_approximate_graph(self, tmp_graph):
        self.__approximate_graph = tmp_graph

    # TODO
    # Deprecated
    def import_z3_expression(self):
        pass

    def set_z3pyscript(self, this_script):
        self.__z3pyscript = this_script

    def relabel_approximate_graph(self):
        gate_mapping = {}
        constant_mapping = {}
        output_mapping = {}
        for key in self.approximate_graph.gate_dict.keys():
            gate_mapping[self.approximate_graph.gate_dict[key]] = f'app_{self.approximate_graph.gate_dict[key]}'
        for key in self.approximate_graph.constant_dict.keys():
            constant_mapping[
                self.approximate_graph.constant_dict[key]] = f'app_{self.approximate_graph.constant_dict[key]}'
        for key in self.approximate_graph.output_dict.keys():
            output_mapping[self.approximate_graph.output_dict[key]] = f'app_{self.approximate_graph.output_dict[key]}'
        self.approximate_graph.set_graph(nx.relabel_nodes(self.approximate_graph.graph, gate_mapping))
        self.approximate_graph.set_graph(nx.relabel_nodes(self.approximate_graph.graph, constant_mapping))
        self.approximate_graph.set_graph(nx.relabel_nodes(self.approximate_graph.graph, output_mapping))

    def convert_gv_to_z3pyscript_test(self):
        folder, extension = OUTPUT_PATH['report']
        os.makedirs(f'{folder}/{self.name}', exist_ok=True)
        self.set_z3_report(f'{folder}/{self.name}/{self.name}_{TEST}.{extension}')

        folder, extension = OUTPUT_PATH['z3']
        os.makedirs(f'{folder}/{self.name}', exist_ok=True)
        self.set_out_path(f'{folder}/{self.name}/{self.name}_{TEST}.{extension}')

        folder, extension = TEST_PATH['z3']
        os.makedirs(f'{folder}/{self.name}', exist_ok=True)
        self.set_pyscript_results_out_path(f'{folder}/{self.name}/{self.name}_{TEST}.{extension}')

        import_string = self.create_imports()
        abs_function = self.create_abs_function()
        exact_circuit_declaration = self.declare_original_circuit()
        exact_circuit_expression = self.express_original_circuit()
        output_declaration = self.declare_original_output()
        exact_function = self.declare_original_function()
        solver = self.declare_solver()
        sample_expression = self.express_samples()
        store_results = self.store_results()
        self.set_z3pyscript(import_string + abs_function + exact_circuit_declaration + exact_circuit_expression +
                            output_declaration + exact_function + solver + sample_expression + store_results)

    def convert_gv_to_z3pyscript_maxerror_qor(self, strategy: str = DEFAULT_STRATEGY):

        self.experiment = QOR
        self.set_strategy(strategy)

        if self.metric == WRE:
            folder, extension = OUTPUT_PATH['report']
            if self.optimization == OPTIMIZE or self.optimization == MAXIMIZE and (self.strategy != BISECTION):
                self.set_z3_report(
                    f'{folder}/{self.approximate_benchmark}_{self.experiment}_{self.metric}_d{self.precision}_{self.strategy}_{self.optimization}.{extension}')
            else:
                self.set_z3_report(
                    f'{folder}/{self.approximate_benchmark}_{self.experiment}_{self.metric}_d{self.precision}_{self.strategy}.{extension}')

            folder, extension = OUTPUT_PATH['z3']
            if self.optimization == OPTIMIZE or self.optimization == MAXIMIZE and (self.strategy != BISECTION):
                self.set_out_path(
                    f'{folder}/{self.approximate_benchmark}_{self.experiment}_{self.metric}_d{self.precision}_{self.strategy}_{self.optimization}.{extension}')
            else:
                self.set_out_path(
                    f'{folder}/{self.approximate_benchmark}_{self.experiment}_{self.metric}_d{self.precision}_{self.strategy}.{extension}')

        else:
            folder, extension = OUTPUT_PATH['report']
            if self.optimization == OPTIMIZE or self.optimization == MAXIMIZE and (self.strategy != BISECTION):
                self.set_z3_report(
                    f'{folder}/{self.approximate_benchmark}_{self.experiment}_{self.metric}_{self.strategy}_{self.optimization}.{extension}')
            else:
                self.set_z3_report(
                    f'{folder}/{self.approximate_benchmark}_{self.experiment}_{self.metric}_{self.strategy}.{extension}')

            folder, extension = OUTPUT_PATH['z3']
            if self.optimization == OPTIMIZE or self.optimization == MAXIMIZE and (self.strategy != BISECTION):
                self.set_out_path(
                    f'{folder}/{self.approximate_benchmark}_{self.experiment}_{self.metric}_{self.strategy}_{self.optimization}.{extension}')
            else:
                self.set_out_path(
                    f'{folder}/{self.approximate_benchmark}_{self.experiment}_{self.metric}_{self.strategy}.{extension}')


        import_string = self.create_imports()
        abs_function = self.create_abs_function()

        # exact_part
        original_circuit_declaration = self.declare_original_circuit()
        original_circuit_expression = self.express_original_circuit()
        original_output_declaration = self.declare_original_output()

        # approximate_part
        approximate_circuit_declaration = self.declare_approximate_circuit()
        approximate_circuit_expression = self.express_approximate_circuit()
        approximate_output_declaration = self.declare_approximate_output()

        # error distance function
        declare_error_distance_function = self.declare_error_distance_function()
        # strategy

        strategy = self.express_strategy()

        self.set_z3pyscript(import_string + abs_function + original_circuit_declaration + original_circuit_expression +
                            original_output_declaration + approximate_circuit_declaration + approximate_circuit_expression +
                            approximate_output_declaration + declare_error_distance_function + strategy)

    def convert_gv_to_z3pyscript_maxerror_labeling(self, strategy: str = DEFAULT_STRATEGY):
        self.experiment = SINGLE
        self.set_strategy(strategy)
        removed_gate = []
        for key in self.graph.input_dict:
            removed_gate = [self.graph.input_dict[key]]
            self.create_pruned_z3pyscript(removed_gate)
        for key in self.graph.gate_dict:
            removed_gate = [self.graph.gate_dict[key]]
            self.create_pruned_z3pyscript(removed_gate)

    def convert_gv_to_z3pyscript_maxerror_random_pruning(self, strategy: str = DEFAULT_STRATEGY):

        self.experiment = RANDOM
        self.set_strategy(strategy)

        removed_gates = []
        for idx in self.pruned_gates:
            if idx < self.graph.num_inputs:  # remove pi
                removed_gates.append(self.graph.input_dict[idx])
            else:  # remove gate
                removed_gates.append(self.graph.gate_dict[idx - self.graph.num_inputs + 1])
        # print(f'{removed_gates}')
        self.create_pruned_z3pyscript(removed_gates)

    # TODO
    # Naming problems for more than one gate removal
    def create_pruned_z3pyscript(self, gates: list):
        self.create_pruned_graph(gates)
        if self.experiment == SINGLE:
            gate = gates[0]
        # TODO
        elif self.experiment == RANDOM:
            gate = 'id0'
        folder, extension = OUTPUT_PATH['report']
        if self.metric == WRE:
            if self.optimization == OPTIMIZE or self.optimization == MAXIMIZE and (self.strategy != BISECTION):
                folder = f'{folder}/{self.name}_{self.experiment}_{self.metric}_d{self.precision}_{self.strategy}_{self.optimization}'
                os.makedirs(folder, exist_ok=True)
                self.set_z3_report(
                    f'{folder}/{self.name}_{self.experiment}_{self.metric}_d{self.precision}_{self.strategy}_{self.optimization}_{gate}.{extension}')
            else:
                folder = f'{folder}/{self.name}_{self.experiment}_{self.metric}_d{self.precision}_{self.strategy}'
                os.makedirs(folder, exist_ok=True)
                self.set_z3_report(
                    f'{folder}/{self.name}_{self.experiment}_{self.metric}_d{self.precision}_{self.strategy}_{gate}.{extension}')
        else:

            if self.optimization == OPTIMIZE or self.optimization == MAXIMIZE and (self.strategy != BISECTION):
                folder = f'{folder}/{self.name}_{self.experiment}_{self.metric}_{self.strategy}_{self.optimization}'
                os.makedirs(folder, exist_ok=True)
                self.set_z3_report(
                    f'{folder}/{self.name}_{self.experiment}_{self.metric}_{self.strategy}_{self.optimization}_{gate}.{extension}')
            else:
                folder = f'{folder}/{self.name}_{self.experiment}_{self.metric}_{self.strategy}'
                os.makedirs(folder, exist_ok=True)
                self.set_z3_report(
                    f'{folder}/{self.name}_{self.experiment}_{self.metric}_{self.strategy}_{gate}.{extension}')

        folder, extension = OUTPUT_PATH['z3']
        if self.metric == WRE:
            if self.optimization == OPTIMIZE or self.optimization == MAXIMIZE and (self.strategy != BISECTION):
                folder = f'{folder}/{self.name}_{self.experiment}_{self.metric}_d{self.precision}_{self.strategy}_{self.optimization}'
                os.makedirs(folder, exist_ok=True)
                self.set_out_path(
                    f'{folder}/{self.name}_{self.experiment}_{self.metric}_d{self.precision}_{self.strategy}_{self.optimization}_{gate}.{extension}')
            else:
                folder = f'{folder}/{self.name}_{self.experiment}_{self.metric}_d{self.precision}_{self.strategy}'
                os.makedirs(folder, exist_ok=True)
                self.set_out_path(
                    f'{folder}/{self.name}_{self.experiment}_{self.metric}_d{self.precision}_{self.strategy}_{gate}.{extension}')
        else:
            if self.optimization == OPTIMIZE or self.optimization == MAXIMIZE and (self.strategy != BISECTION):
                folder = f'{folder}/{self.name}_{self.experiment}_{self.metric}_{self.strategy}_{self.optimization}'
                os.makedirs(folder, exist_ok=True)
                self.set_out_path(
                    f'{folder}/{self.name}_{self.experiment}_{self.metric}_{self.strategy}_{self.optimization}_{gate}.{extension}')
            else:
                folder = f'{folder}/{self.name}_{self.experiment}_{self.metric}_{self.strategy}'
                os.makedirs(folder, exist_ok=True)
                self.set_out_path(
                    f'{folder}/{self.name}_{self.experiment}_{self.metric}_{self.strategy}_{gate}.{extension}')

        self.append_pyscript_files_for_labeling(self.out_path)

        import_string = self.create_imports()
        abs_function = self.create_abs_function()

        # exact_part
        original_circuit_declaration = self.declare_original_circuit()
        original_circuit_expression = self.express_original_circuit()
        original_output_declaration = self.declare_original_output()

        approximate_circuit_declaration = self.declare_approximate_circuit()
        approximate_circuit_expression = self.express_approximate_circuit()
        approximate_output_declaration = self.declare_approximate_output()

        # error distance function
        declare_error_distance_function = self.declare_error_distance_function()
        # strategy

        strategy = self.express_strategy()

        self.set_z3pyscript(
            import_string + abs_function + original_circuit_declaration + original_circuit_expression +
            original_output_declaration + approximate_circuit_declaration + approximate_circuit_expression +
            approximate_output_declaration + declare_error_distance_function + strategy)

        self.export_z3pyscript()

    def convert_gv_to_z3pyscript_xpat(self):
        pass

    def create_pruned_graph(self, gates: list):

        tmp_graph = copy.deepcopy(self.graph)
        self.set_approximate_graph(tmp_graph)
        mapping_dict = {}
        for gate in gates:
            if self.graph.is_pi(gate) or self.graph.is_cleaned_pi(gate) or self.graph.is_pruned_pi(gate):
                mapping_dict[gate] = f'app_{gate}'
        for gate in gates:
            self.approximate_graph.graph.nodes[gate][PRUNED] = True
        self.approximate_graph.set_graph(nx.relabel_nodes(self.approximate_graph.graph, mapping_dict))
        self.relabel_approximate_graph()
        self.approximate_graph.set_input_dict(self.approximate_graph.extract_inputs())
        self.approximate_graph.set_output_dict(self.approximate_graph.extract_outputs())
        self.approximate_graph.set_gate_dict(self.approximate_graph.extract_gates())
        self.approximate_graph.set_constant_dict(self.approximate_graph.extract_constants())

    # TODO
    # for other back-ends as well

    def declare_error_distance_function(self):
        ed_function = ''

        if self.metric == WAE:
            ed_function += f"f_exact = Function('f_exact', IntSort(), IntSort())\n" \
                           f"f_approx = Function('f_approx', IntSort(), IntSort())\n"
            ed_function += f"f_error = Function('f_error', IntSort(), IntSort(), IntSort())\n"
        elif self.metric == WHD:
            pass
        elif self.metric == WRE:
            ed_function += f"f_exact = Function('f_exact', IntSort(), IntSort())\n" \
                           f"f_approx = Function('f_approx', IntSort(), IntSort())\n"
            ed_function += f"f_error = Function('f_error', IntSort(), IntSort(), RealSort())\n"

        ed_function += f'\n'
        return ed_function

    def express_strategy(self, metric: str = None):
        strategy_expressed = ''
        if re.search(MONOTONIC, self.strategy):
            strategy_expressed += self.express_monotonic_strategy()
        elif re.search(BISECTION, self.strategy):
            strategy_expressed += self.express_bisection_strategy()
        elif re.search(MC, self.strategy):
            strategy_expressed += self.express_mc_strategy()
        elif re.search(KIND_BISECTION, self.strategy):
            # print(f'You are choosing kind_bisection!')
            strategy_expressed += self.express_kind_bisection_strategy()
        else:
            print(f'ERROR!!! no strategy is specified!')
            exit()
        return strategy_expressed

    def declare_stats(self):
        stats = ''
        stats = f'foundWCE = False\n' \
                f'stats: dict = {{}}\n' \
                f"stats['wce'] = 0\n"

        if self.metric == WAE:
            stats += f"stats['et'] = 0\n"
        elif self.metric == WHD:
            stats += f"stats['et'] = 0\n"
        elif self.metric == WRE:
            stats += f"stats['et'] = \"{{:.{self.precision}f}}\".format(0)\n"

        stats += f"stats['num_sats'] = 0\n" \
                 f"stats['num_unsats'] = 0\n" \
                 f"stats['sat_runtime'] = 0.0\n" \
                 f"stats['unsat_runtime'] = 0.0\n" \
                 f"stats['jumps'] = []\n" \
                 f"max = (2 ** {self.graph.num_outputs}) -1\n"
        return stats

    def express_mc_while_loop(self):
        loop = ''
        loop += f's=Solver()\n' \
                f'start_whole = time.time()\n'

        for sample in self.samples:
            loop += f's.push()\n' \
                    f's.add(f_error(exact_out, approx_out) == z3_abs(exact_out - approx_out))\n' \
                    f'{self.express_push_input_sample(sample)}' \
                    f'response=s.check()\n' \
                    f'returned_model = s.model()\n' \
                    f'returned_value = abs(int(returned_model[f_error].else_value().as_long()))\n' \
                    f'returned_value_reval = abs(int(returned_model.evaluate(f_error(exact_out, approx_out)).as_long()))\n' \
                    f'if returned_value == returned_value_reval:\n' \
                    f"{TAB}print(f'double-check is passed!')\n" \
                    f"else:\n" \
                    f"{TAB}print(f'ERROR!!! double-check failed! exiting...')\n" \
                    f"{TAB}exit()\n" \
                    f"if returned_value > stats['wce']:\n" \
                    f"{TAB}stats['wce'] = returned_value\n" \
                    f"s.pop()\n" \
                    f"\n" \
                    f""
        loop += self.express_stats()
        return loop

    def express_push_input_sample(self, sample: int):
        sample_expression = ''
        s_expression = [True if i == '1' else False for i in list(f'{sample:0{self.graph.num_inputs}b}')]
        s_expression.reverse()
        sample_expression += f's.add('
        for idx, e in enumerate(s_expression):
            if idx == len(s_expression) - 1:
                sample_expression += f'{self.graph.input_dict[idx]}=={e})\n'
            else:
                sample_expression += f'{self.graph.input_dict[idx]}=={e}, '

        return sample_expression

    def express_kind_bisection_while_loop(self):
        loop = ''
        loop += f'upper_bound = 2**({self.graph.num_outputs}) - 1\n' \
                f'lower_bound = 0 \n' \
                f'start_whole = time.time()\n'

        loop += f's = Solver()\n'

        loop += f'while(not foundWCE):\n' \
                f'{TAB}start_iteration = time.time()\n'

        if self.metric == WAE:
            loop += f"{TAB}stats['et'] = (upper_bound + lower_bound) // 2\n"
        elif self.metric == WHD:
            loop += f"{TAB}stats['et'] = (upper_bound + lower_bound) // 2\n"
        elif self.metric == WRE:
            loop += f"{TAB}stats['et'] = round(float(upper_bound + lower_bound) / 2, {self.precision})\n"

        loop += f"{TAB}stats['jumps'].append(stats['et'])\n" \
                f'{TAB}s.push()\n' \
                f'{TAB}s.add(f_exact(exact_out) == exact_out)\n' \
                f'{TAB}s.add(f_approx(approx_out) == approx_out)\n'

        if self.metric == WAE:
            loop += f'{TAB}s.add(f_error(exact_out, approx_out) == exact_out - approx_out)\n' \
                    f"{TAB}s.add(z3_abs(f_error(exact_out, approx_out)) > stats['et'])\n"
        elif self.metric == WHD:
            pass
            # TODO
        elif self.metric == WRE:
            loop += f'{TAB}s.add(f_error(exact_out, approx_out) == z3_abs(exact_out - approx_out) / (z3_abs(exact_out) + z3_abs(1.0))  )\n' \
                    f"{TAB}s.add(z3_abs(f_error(exact_out, approx_out)) > stats['et'])\n"

        loop += f"{TAB}response = s.check()\n"
        loop += self.express_kind_bisection_while_loop_sat()
        loop += self.express_kind_bisection_while_loop_unsat()
        loop += self.express_stats()

        return loop

    def express_bisection_while_loop(self):
        loop = ''
        loop += f'upper_bound = 2**({self.graph.num_outputs}) - 1\n' \
                f'lower_bound = 0 \n' \
                f'start_whole = time.time()\n'

        loop += f's = Solver()\n'

        loop += f'while(not foundWCE):\n' \
                f'{TAB}start_iteration = time.time()\n'

        if self.metric == WAE:
            loop += f"{TAB}stats['et'] = (upper_bound + lower_bound) // 2\n"
        elif self.metric == WHD:
            loop += f"{TAB}stats['et'] = (upper_bound + lower_bound) // 2\n"
        elif self.metric == WRE:
            loop += f"{TAB}stats['et'] = round(float(upper_bound + lower_bound) / 2, {self.precision})\n"

        loop += f"{TAB}stats['jumps'].append(stats['et'])\n" \
                f'{TAB}s.push()\n' \
                f'{TAB}s.add(f_exact(exact_out) == exact_out)\n' \
                f'{TAB}s.add(f_approx(approx_out) == approx_out)\n'

        if self.metric == WAE:
            loop += f'{TAB}s.add(f_error(exact_out, approx_out) == exact_out - approx_out)\n' \
                    f"{TAB}s.add(z3_abs(f_error(exact_out, approx_out)) > stats['et'])\n"
        elif self.metric == WHD:
            pass
            # TODO
        elif self.metric == WRE:
            loop += f'{TAB}s.add(f_error(exact_out, approx_out) == z3_abs(exact_out - approx_out) / (z3_abs(exact_out) + z3_abs(1.0))  )\n' \
                    f"{TAB}s.add(z3_abs(f_error(exact_out, approx_out)) > stats['et'])\n"

        loop += f"{TAB}response = s.check()\n"

        loop += self.express_bisection_while_loop_sat()
        loop += self.express_bisection_while_loop_unsat()
        loop += self.express_stats()

        return loop

    def express_monotonic_while_loop(self):
        loop = ''

        loop += f'start_whole = time.time()\n'
        # print(f'{self.optimization == MAXIMIZE = }')
        # print(f'{self.optimization = }')
        if self.optimization == OPTIMIZE or self.optimization == MAXIMIZE and (self.strategy != BISECTION):
            loop += f's = Optimize()\n'
        else:
            # print('We are here')
            loop += f's = Solver()\n'

        loop += f"stats['jumps'].append(stats['et'])\n" \
                f'while(not foundWCE):\n' \
                f'{TAB}start_iteration = time.time()\n' \
                f'{TAB}s.push()\n' \
                f'{TAB}s.add(f_exact(exact_out) == exact_out)\n' \
                f'{TAB}s.add(f_approx(approx_out) == approx_out)\n'

        if self.metric == WAE:
            if self.optimization == MAXIMIZE and (self.strategy != BISECTION):
                loop += f'{TAB}s.add(f_error(exact_out, approx_out) == exact_out - approx_out)\n' \
                        f"{TAB}s.add(z3_abs(f_error(exact_out, approx_out)) > stats['et'])\n" \
                        f"{TAB}s.maximize(z3_abs(f_error(exact_out, approx_out)))\n"
            else:
                loop += f'{TAB}s.add(f_error(exact_out, approx_out) == exact_out - approx_out)\n' \
                        f"{TAB}s.add(z3_abs(f_error(exact_out, approx_out)) > stats['et'])\n"

            # TODO add optimization thingy right here
        elif self.metric == WHD:
            if self.optimization == MAXIMIZE and (self.strategy != BISECTION):
                pass
            else:
                pass
            # TODO
        elif self.metric == WRE:
            if self.optimization == MAXIMIZE and (self.strategy != BISECTION):
                loop += f'{TAB}s.add(f_error(exact_out, approx_out) == z3_abs(exact_out - approx_out) / (z3_abs(exact_out) + z3_abs(1.0))  )\n' \
                        f"{TAB}s.add(z3_abs(f_error(exact_out, approx_out)) > stats['et'])\n" \
                        f"{TAB}s.maximize(z3_abs(f_error(exact_out, approx_out)))\n"
            else:
                loop += f'{TAB}s.add(f_error(exact_out, approx_out) == z3_abs(exact_out - approx_out) / (z3_abs(exact_out) + z3_abs(1.0))  )\n' \
                        f"{TAB}s.add(z3_abs(f_error(exact_out, approx_out)) > stats['et'])\n"
        loop += f"{TAB}response = s.check()\n"

        loop += self.express_monotonic_while_loop_sat()
        loop += self.express_monotonic_while_loop_unsat()
        loop += self.express_stats()

        return loop

    def express_kind_bisection_while_loop_sat(self):
        if_sat = ''

        if_sat += f"{TAB}if response == sat:\n" \
                  f"{TAB}{TAB}print(f'sat')\n" \
                  f"{TAB}{TAB}end_iteration = time.time()\n" \
                  f"{TAB}{TAB}returned_model = s.model()\n" \
                  f"{TAB}{TAB}print(f'{{returned_model = }}')\n" \
                  f"{TAB}{TAB}print(f\"{{returned_model[f_exact].else_value() = }}\")\n" \
                  f"{TAB}{TAB}print(f\"{{returned_model[f_approx].else_value() = }}\")\n" \
                  f"{TAB}{TAB}print(f\"{{returned_model[f_error].else_value() = }}\")\n"

        if self.metric == WAE:
            if_sat += f"{TAB}{TAB}returned_value = abs(int(returned_model[f_error].else_value().as_long()))\n" \
                      f"{TAB}{TAB}returned_value_reval = abs(int(returned_model.evaluate(f_error(exact_out, approx_out)).as_long()))\n"
        elif self.metric == WHD:
            pass
            # TODO
        elif self.metric == WRE:
            if_sat += f"{TAB}{TAB}returned_value = ((returned_model[f_error].else_value().as_decimal({self.precision})))\n" \
                      f"{TAB}{TAB}returned_value_reval = ((returned_model.evaluate(f_error(exact_out, approx_out)).as_decimal({self.precision})))\n"


        # Double-check
        if_sat += f"{TAB}{TAB}if returned_value == returned_value_reval:\n" \
                  f"{TAB}{TAB}{TAB}print(f'double-check is passed!')\n" \
                  f"{TAB}{TAB}else:\n" \
                  f"{TAB}{TAB}{TAB}print(f'ERROR!!! double-check failed! exiting...')\n" \
                  f"{TAB}{TAB}{TAB}exit()\n"

        if self.metric == WAE:
            if_sat += f"{TAB}{TAB}if upper_bound - lower_bound <= 1:\n" \
                      f"{TAB}{TAB}{TAB}foundWCE = True\n" \
                      f"{TAB}{TAB}{TAB}stats['wce'] = upper_bound\n" \
                      f"{TAB}{TAB}else:\n" \
                      f"{TAB}{TAB}{TAB}lower_bound = returned_value\n"
        elif self.metric == WHD:
            pass
        elif self.metric == WRE:
            if_sat += f"{TAB}{TAB}if round(upper_bound - lower_bound, 2) <= (10 ** -{self.precision}):\n" \
                      f"{TAB}{TAB}{TAB}foundWCE = True\n" \
                      f"{TAB}{TAB}{TAB}stats['wce'] = upper_bound\n" \
                      f"{TAB}{TAB}else:\n" \
                      f"{TAB}{TAB}{TAB}lower_bound = \"{{:.{self.precision}f}}\".format(returned_value)\n\n"

        if_sat += f"{TAB}{TAB}stats['num_sats'] += 1\n" \
                  f"{TAB}{TAB}stats['sat_runtime'] += (end_iteration - start_iteration)\n" \
                  f"{TAB}{TAB}stats['jumps'].append(returned_value)\n" \
                  f"{TAB}{TAB}if stats['et'] == max:\n" \
                  f"{TAB}{TAB}{TAB}foundWCE = True\n" \
                  f"{TAB}{TAB}{TAB}stats['wce'] = stats['et']\n"

        return if_sat

    def express_bisection_while_loop_sat(self):
        if_sat = ''

        if_sat += f"{TAB}if response == sat:\n" \
                  f"{TAB}{TAB}print(f'sat')\n" \
                  f"{TAB}{TAB}end_iteration = time.time()\n" \
                  f"{TAB}{TAB}returned_model = s.model()\n" \
                  f"{TAB}{TAB}print(f'{{returned_model = }}')\n" \
                  f"{TAB}{TAB}print(f\"{{returned_model[f_exact].else_value() = }}\")\n" \
                  f"{TAB}{TAB}print(f\"{{returned_model[f_approx].else_value() = }}\")\n" \
                  f"{TAB}{TAB}print(f\"{{returned_model[f_error].else_value() = }}\")\n"

        if self.metric == WAE:
            if_sat += f"{TAB}{TAB}returned_value = abs(int(returned_model[f_error].else_value().as_long()))\n" \
                      f"{TAB}{TAB}returned_value_reval = abs(int(returned_model.evaluate(f_error(exact_out, approx_out)).as_long()))\n"
        elif self.metric == WHD:
            pass
            # TODO
        elif self.metric == WRE:
            if_sat += f"{TAB}{TAB}returned_value = ((returned_model[f_error].else_value().as_decimal({self.precision})))\n" \
                      f"{TAB}{TAB}returned_value_reval = ((returned_model.evaluate(f_error(exact_out, approx_out)).as_decimal({self.precision})))\n"

        if_sat += f"{TAB}{TAB}if returned_value == returned_value_reval:\n" \
                  f"{TAB}{TAB}{TAB}print(f'double-check is passed!')\n" \
                  f"{TAB}{TAB}else:\n" \
                  f"{TAB}{TAB}{TAB}print(f'ERROR!!! double-check failed! exiting...')\n" \
                  f"{TAB}{TAB}{TAB}exit()\n"

        if self.metric == WAE:
            if_sat += f"{TAB}{TAB}if upper_bound - lower_bound <= 1:\n" \
                      f"{TAB}{TAB}{TAB}foundWCE = True\n" \
                      f"{TAB}{TAB}{TAB}stats['wce'] = upper_bound\n" \
                      f"{TAB}{TAB}else:\n" \
                      f"{TAB}{TAB}{TAB}lower_bound = stats['et']\n"
        elif self.metric == WHD:
            pass
        elif self.metric == WRE:
            if_sat += f"{TAB}{TAB}if round(upper_bound - lower_bound, 2) <= (10 ** -{self.precision}):\n" \
                      f"{TAB}{TAB}{TAB}foundWCE = True\n" \
                      f"{TAB}{TAB}{TAB}stats['wce'] = upper_bound\n" \
                      f"{TAB}{TAB}else:\n" \
                      f"{TAB}{TAB}{TAB}lower_bound = stats['et']\n"

        if_sat += f"{TAB}{TAB}stats['num_sats'] += 1\n" \
                  f"{TAB}{TAB}stats['sat_runtime'] += (end_iteration - start_iteration)\n" \
                  f"{TAB}{TAB}stats['jumps'].append(returned_value)\n" \
                  f"{TAB}{TAB}if stats['et'] == max:\n" \
                  f"{TAB}{TAB}{TAB}foundWCE = True\n" \
                  f"{TAB}{TAB}{TAB}stats['wce'] = stats['et']\n"

        return if_sat

    def express_monotonic_while_loop_sat(self):
        if_sat = ''
        if_sat += f"{TAB}if response == sat:\n" \
                  f"{TAB}{TAB}print(f'sat')\n" \
                  f"{TAB}{TAB}end_iteration = time.time()\n" \
                  f"{TAB}{TAB}returned_model = s.model()\n" \
                  f"{TAB}{TAB}print(f'{{returned_model = }}')\n" \
                  f"{TAB}{TAB}print(f\"{{returned_model[f_exact].else_value() = }}\")\n" \
                  f"{TAB}{TAB}print(f\"{{returned_model[f_approx].else_value() = }}\")\n" \
                  f"{TAB}{TAB}print(f\"{{returned_model[f_error].else_value() = }}\")\n"

        if self.metric == WAE:
            if_sat += f"{TAB}{TAB}returned_value = abs(int(returned_model[f_error].else_value().as_long()))\n" \
                      f"{TAB}{TAB}returned_value_reval = abs(int(returned_model.evaluate(f_error(exact_out, approx_out)).as_long()))\n"
        elif self.metric == WHD:
            pass
        elif self.metric == WRE:
            if_sat += f"{TAB}{TAB}returned_value = ((returned_model[f_error].else_value().as_decimal({self.precision})))\n" \
                      f"{TAB}{TAB}returned_value_reval = ((returned_model.evaluate(f_error(exact_out, approx_out)).as_decimal({self.precision})))\n"

        if_sat += f"{TAB}{TAB}if returned_value == returned_value_reval:\n" \
                  f"{TAB}{TAB}{TAB}print(f'double-check is passed!')\n" \
                  f"{TAB}{TAB}else:\n" \
                  f"{TAB}{TAB}{TAB}print(f'ERROR!!! double-check failed! exiting...')\n" \
                  f"{TAB}{TAB}{TAB}exit()\n"

        if self.metric == WRE:
            if_sat += f"{TAB}{TAB}if returned_value[-1] == '?':\n" \
                      f"{TAB}{TAB}{TAB}print('removing the last question mark!')\n" \
                      f"{TAB}{TAB}{TAB}returned_value = abs(float(returned_value[:-1])) + 10 ** -({self.precision})\n" \
                      f"{TAB}{TAB}else:\n" \
                      f"{TAB}{TAB}{TAB}returned_value = abs(float(returned_value))\n"

        if self.metric == WAE:
            if_sat += f"{TAB}{TAB}stats['et'] = returned_value\n"
        elif self.metric == WHD:
            if_sat += f"{TAB}{TAB}stats['et'] = returned_value\n"
        elif self.metric == WRE:
            if_sat += f"{TAB}{TAB}stats['et'] = \"{{:.{self.precision}f}}\".format(returned_value)\n"

        if_sat += f"{TAB}{TAB}stats['num_sats'] += 1\n" \
                  f"{TAB}{TAB}stats['sat_runtime'] += (end_iteration - start_iteration)\n" \
                  f"{TAB}{TAB}stats['jumps'].append(returned_value)\n" \
                  f"{TAB}{TAB}if stats['et'] == max:\n" \
                  f"{TAB}{TAB}{TAB}foundWCE = True\n" \
                  f"{TAB}{TAB}{TAB}stats['wce'] = stats['et']\n"
        return if_sat

    def express_kind_bisection_while_loop_unsat(self):
        if_unsat = ''

        if_unsat += f"\n" \
                    f"{TAB}if response == unsat:\n" \
                    f"{TAB}{TAB}print('unsat')\n" \
                    f"{TAB}{TAB}end_iteration = time.time()\n"

        if self.metric == WAE:
            if_unsat += f"{TAB}{TAB}if upper_bound - lower_bound <= 1:\n" \
                        f"{TAB}{TAB}{TAB}foundWCE = True\n" \
                        f"{TAB}{TAB}{TAB}if lower_bound == 0:\n" \
                        f"{TAB}{TAB}{TAB}{TAB}stats['wce'] = lower_bound\n" \
                        f"{TAB}{TAB}{TAB}else:\n" \
                        f"{TAB}{TAB}{TAB}{TAB}stats['wce'] = lower_bound\n"
        elif self.metric == WHD:
            pass
        elif self.metric == WRE:
            if_unsat += f"{TAB}{TAB}if round(upper_bound - lower_bound, 2) <= (10 ** -{self.precision}):\n" \
                        f"{TAB}{TAB}{TAB}foundWCE = True\n" \
                        f"{TAB}{TAB}{TAB}stats['wce'] = lower_bound\n" \
                        f"{TAB}{TAB}{TAB}if lower_bound == 0:\n" \
                        f"{TAB}{TAB}{TAB}{TAB}stats['wce'] = lower_bound\n" \
                        f"{TAB}{TAB}{TAB}else:\n" \
                        f"{TAB}{TAB}{TAB}{TAB}stats['wce'] = lower_bound\n"

        if_unsat += f"{TAB}{TAB}else:\n" \
                    f"{TAB}{TAB}{TAB}upper_bound = stats['et']\n" \
                    f"{TAB}{TAB}stats['num_unsats'] += 1\n" \
                    f"{TAB}{TAB}stats['unsat_runtime'] += (end_iteration - start_iteration)\n" \
                    f"{TAB}s.pop()\n"
        return if_unsat

    def express_bisection_while_loop_unsat(self):
        if_unsat = ''

        if_unsat += f"\n" \
                    f"{TAB}if response == unsat:\n" \
                    f"{TAB}{TAB}print('unsat')\n" \
                    f"{TAB}{TAB}end_iteration = time.time()\n"

        if self.metric == WAE:
            if_unsat += f"{TAB}{TAB}if upper_bound - lower_bound <= 1:\n" \
                        f"{TAB}{TAB}{TAB}foundWCE = True\n" \
                        f"{TAB}{TAB}{TAB}if lower_bound == 0:\n" \
                        f"{TAB}{TAB}{TAB}{TAB}stats['wce'] = lower_bound\n" \
                        f"{TAB}{TAB}{TAB}else:\n" \
                        f"{TAB}{TAB}{TAB}{TAB}stats['wce'] = upper_bound\n"
        elif self.metric == WHD:
            pass
        elif self.metric == WRE:
            if_unsat += f"{TAB}{TAB}if round(upper_bound - lower_bound, 2) <= (10 ** -{self.precision}):\n" \
                        f"{TAB}{TAB}{TAB}foundWCE = True\n" \
                        f"{TAB}{TAB}{TAB}stats['wce'] = lower_bound\n" \
                        f"{TAB}{TAB}{TAB}if lower_bound == 0:\n" \
                        f"{TAB}{TAB}{TAB}{TAB}stats['wce'] = lower_bound\n" \
                        f"{TAB}{TAB}{TAB}else:\n" \
                        f"{TAB}{TAB}{TAB}{TAB}stats['wce'] = upper_bound\n"

        if_unsat += f"{TAB}{TAB}else:\n" \
                    f"{TAB}{TAB}{TAB}upper_bound = stats['et']\n" \
                    f"{TAB}{TAB}stats['num_unsats'] += 1\n" \
                    f"{TAB}{TAB}stats['unsat_runtime'] += (end_iteration - start_iteration)\n" \
                    f"{TAB}s.pop()\n"
        return if_unsat

    def express_monotonic_while_loop_unsat(self):
        if_unsat = ''
        if_unsat += f"\n" \
                    f"{TAB}if response == unsat:\n" \
                    f"{TAB}{TAB}print('unsat')\n" \
                    f"{TAB}{TAB}end_iteration = time.time()\n" \
                    f"{TAB}{TAB}foundWCE = True\n" \
                    f"{TAB}{TAB}stats['num_unsats'] += 1\n" \
                    f"{TAB}{TAB}stats['unsat_runtime'] += (end_iteration - start_iteration)\n" \
                    f"{TAB}{TAB}stats['wce'] = stats['et']\n" \
                    f"{TAB}s.pop()\n"
        return if_unsat

    def express_stats(self):
        stats = ''
        stats += f"end_whole = time.time()\n" \
                 f"with open('{self.z3_report}', 'w') as f:\n" \
                 f"{TAB}csvwriter = csv.writer(f)\n" \
                 f"{TAB}header = ['field', 'value']\n" \
                 f"{TAB}csvwriter.writerow(['Experiment', '{self.experiment}'])\n" \
                 f"{TAB}csvwriter.writerow(['WCE', stats['wce']])\n" \
                 f"{TAB}csvwriter.writerow(['Total Runtime', end_whole - start_whole])\n" \
                 f"{TAB}csvwriter.writerow(['SAT Runtime', stats['sat_runtime']])\n" \
                 f"{TAB}csvwriter.writerow(['UNSAT Runtime', stats['unsat_runtime']])\n" \
                 f"{TAB}csvwriter.writerow(['Number of SAT calls', stats['num_sats']])\n" \
                 f"{TAB}csvwriter.writerow(['Number of UNSAT calls', stats['num_unsats']])\n" \
                 f"{TAB}csvwriter.writerow(['Jumps', stats['jumps']])\n"
        return stats

    def express_monotonic_strategy(self):
        monotonic_strategy = ''
        monotonic_strategy += self.declare_stats()
        monotonic_strategy += self.express_monotonic_while_loop()
        return monotonic_strategy

    def express_mc_strategy(self):
        mc_strategy = ''
        mc_strategy += self.declare_stats()
        mc_strategy += self.express_mc_while_loop()
        return mc_strategy

    def express_bisection_strategy(self):
        bisection_strategy = ''
        bisection_strategy += self.declare_stats()
        bisection_strategy += self.express_bisection_while_loop()

        return bisection_strategy

    def express_kind_bisection_strategy(self):
        kind_bisection_strategy = ''
        kind_bisection_strategy += self.declare_stats()
        kind_bisection_strategy += self.express_kind_bisection_while_loop()
        return kind_bisection_strategy

    def export_z3pyscript(self):
        with open(self.out_path, 'w') as z:
            z.writelines(self.z3pyscript)

    def __repr__(self):
        return f'An object of class Z3solver\n' \
               f'{self.name = }\n' \
               f'{self.graph_in_path = }\n' \
               f'{self.out_path = }\n'

    def create_imports(self):
        import_string = f'from z3 import *\n' \
                        f'import sys\n' \
                        f'import time\n' \
                        f'import csv\n' \
                        f'\n'
        return import_string

    def create_abs_function(self):
        abs_function = f'def z3_abs(x):\n' \
                       f'\treturn If(x >= 0, x, -x)\n' \
                       f'\n'

        return abs_function

    def declare_original_circuit(self):
        exact_circuit_declaration = ''
        # inputs
        for n in self.graph.graph.nodes:
            if re.search(r'in\d+', self.graph.graph.nodes[n]['label']):
                exact_circuit_declaration = f'{exact_circuit_declaration}' \
                                            f'{self.declare_gate(n)}\n'
        exact_circuit_declaration += f'\n'
        # gates
        for n in self.graph.graph.nodes:
            if re.search(r'g\d+', n):
                exact_circuit_declaration = f'{exact_circuit_declaration}' \
                                            f'{self.declare_gate(n)}\n'
        # outputs
        for n in self.graph.graph.nodes:
            if re.search(r'out\d+', self.graph.graph.nodes[n]['label']):
                exact_circuit_declaration = f'{exact_circuit_declaration}' \
                                            f'{self.declare_gate(n)}\n'
        return exact_circuit_declaration

    def declare_approximate_circuit(self):
        exact_circuit_declaration = ''
        # inputs
        for n in self.approximate_graph.graph.nodes:
            if self.approximate_graph.is_pruned_pi(n):
                exact_circuit_declaration = f'{exact_circuit_declaration}' \
                                            f'{self.declare_gate(n)}\n'
        exact_circuit_declaration += f'\n'
        # gates
        for n in self.approximate_graph.graph.nodes:
            if re.search(r'g\d+', n):
                exact_circuit_declaration = f'{exact_circuit_declaration}' \
                                            f'{self.declare_gate(n)}\n'
        # outputs
        for n in self.approximate_graph.graph.nodes:
            if re.search(r'out\d+', self.approximate_graph.graph.nodes[n]['label']):
                exact_circuit_declaration = f'{exact_circuit_declaration}' \
                                            f'{self.declare_gate(n)}\n'
        return exact_circuit_declaration

    def declare_gate(self, this_key: str):
        declaration = f"{this_key} = {Z3BOOL}('{this_key}')"
        return declaration

    def express_original_circuit(self):
        exact_circuit_function = ''
        for n in self.graph.graph.nodes:
            if self.graph.is_cleaned_gate(n):
                exact_circuit_function += f'{self.express_exact_gate(n)}\n'
            elif self.graph.is_cleaned_constant(n):
                exact_circuit_function += f'{self.express_exact_constant(n)}\n'
            elif self.graph.is_cleaned_po(n):
                exact_circuit_function += f'{self.express_exact_output(n)}\n'
        exact_circuit_function += f'\n'
        return exact_circuit_function

    def express_approximate_circuit(self):
        approximate_circuit_function = ''

        for n in self.approximate_graph.graph.nodes:
            if self.approximate_graph.is_cleaned_pi(n):
                approximate_circuit_function += f'{self.express_approximate_gate(n)}\n'
            elif self.approximate_graph.is_cleaned_gate(n):
                approximate_circuit_function += f'{self.express_approximate_gate(n)}\n'
            elif self.approximate_graph.is_cleaned_constant(n):
                approximate_circuit_function += f'{self.express_approximate_constant(n)}\n'
            elif self.approximate_graph.is_cleaned_po(n):
                approximate_circuit_function += f'{self.express_approximate_output(n)}\n'
        approximate_circuit_function += f'\n'
        return approximate_circuit_function

    def express_exact_output(self, this_key):
        cur_node = ''
        predecessor = list(self.graph.graph.predecessors(this_key))[0]
        cur_node = f'{this_key} = {predecessor}\n'

        return cur_node

    def express_exact_constant(self, this_key):
        cur_node = ''
        this_constant = re.search(r'TRUE|FALSE', self.graph.graph.nodes[this_key][LABEL]).group()
        cur_node += f'{this_key} = {Z3_GATES_DICTIONARY[this_constant]}\n'
        return cur_node

    def express_exact_gate(self, this_key: str):
        # sth like this: g110 = Not(And(g108, g109))
        cur_node = ''
        if self.graph.is_cleaned_gate(this_key):
            this_gate = re.search(POSSIBLE_GATES, self.graph.graph.nodes[this_key]['label']).group()
            cur_gate = Z3_GATES_DICTIONARY[this_gate]
            predecessor_list = list(self.graph.graph.predecessors(this_key))
            cur_node = f"{this_key}={cur_gate}("
            for idx, u in enumerate(predecessor_list):
                cur_node += f'{u}'
                if idx == len(predecessor_list) - 1:
                    cur_node += f')'
                else:
                    cur_node += f','

        elif self.graph.is_cleaned_pi(this_key):
            pass
        elif self.graph.is_cleaned_po(this_key):
            cur_node = f'{this_key}='
            predecessor_list = list(self.graph.graph.predecessors(this_key))
            for idx, u in enumerate(predecessor_list):
                cur_node += f'{u}'
        return cur_node

    def express_approximate_output(self, this_key):
        cur_node = ''
        predecessor = list(self.approximate_graph.graph.predecessors(this_key))[0]
        cur_node = f'{this_key} = {predecessor}\n'

        return cur_node

    def express_approximate_constant(self, this_key):
        cur_node = ''
        this_constant = re.search(r'TRUE|FALSE', self.approximate_graph.graph.nodes[this_key][LABEL]).group()
        cur_node += f'{this_key} = {Z3_GATES_DICTIONARY[this_constant]}\n'
        return cur_node

    def express_approximate_gate(self, this_key: str):
        # sth like this: g110 = Not(And(g108, g109))
        cur_node = ''
        if self.approximate_graph.is_pruned_gate(this_key):
            cur_node = f'{this_key} = {self.approximate_graph.graph.nodes[this_key][PRUNED]}'
        elif self.approximate_graph.is_cleaned_gate(this_key):
            this_gate = re.search(POSSIBLE_GATES, self.approximate_graph.graph.nodes[this_key]['label']).group()
            cur_gate = Z3_GATES_DICTIONARY[this_gate]
            predecessor_list = list(self.approximate_graph.graph.predecessors(this_key))
            cur_node = f"{this_key}={cur_gate}("
            for idx, u in enumerate(predecessor_list):
                cur_node += f'{u}'
                if idx == len(predecessor_list) - 1:
                    cur_node += f')'
                else:
                    cur_node += f','

        elif self.approximate_graph.is_pruned_pi(this_key):
            cur_node = f'{this_key}= {self.approximate_graph.graph.nodes[this_key][PRUNED]}'
        elif self.approximate_graph.is_cleaned_po(this_key):
            cur_node = f'{this_key}='
            predecessor_list = list(self.approximate_graph.graph.predecessors(this_key))
            for idx, u in enumerate(predecessor_list):
                cur_node += f'{u}'
        return cur_node

    def declare_original_output(self):
        output_declaration = ''
        # print(f'{self.graph.output_dict = }')

        for i in range(self.graph.num_outputs):
            output_declaration += f"exact_out{i}=Int('exact_out{i}')\n"
            output_declaration += f"exact_out{i}={self.graph.output_dict[i]}*{2 ** i}\n"

        output_declaration += f"exact_out = Int('exact_out')\n"
        output_declaration += f'exact_out='

        for i in range(self.graph.num_outputs):
            if i == self.graph.num_outputs - 1:
                output_declaration += f'exact_out{i}'
            else:
                output_declaration += f'exact_out{i}+'

        output_declaration += f'\n'
        return output_declaration

    def declare_approximate_output(self):
        output_declaration = ''
        # print(f'{self.approximate_graph.output_dict = }')

        for i in range(self.approximate_graph.num_outputs):
            output_declaration += f"approx_out{i}=Int('approx_out{i}')\n"
            output_declaration += f"approx_out{i}={self.approximate_graph.output_dict[i]}*{2 ** i}*2/2\n"
        # print(f'{self.approximate_graph.output_dict = }')
        output_declaration += f"approx_out = Int('approx_out')\n"
        output_declaration += f'approx_out='
        for i in range(self.approximate_graph.num_outputs):
            if i == self.approximate_graph.num_outputs - 1:
                output_declaration += f'approx_out{i}'
            else:
                output_declaration += f'approx_out{i}+'

        output_declaration += f'\n'
        return output_declaration

    def declare_original_function(self):
        exact_function = ''
        exact_function += f'results = []\n'
        exact_function += f"f_exact = Function('f', IntSort(), IntSort())"
        exact_function += f'\n'
        return exact_function

    def declare_approximate_function(self):
        exact_function = ''
        exact_function += f'results = []\n'
        exact_function += f"f_exact = Function('f', IntSort(), IntSort())"
        exact_function += f'\n'
        return exact_function

    def declare_solver(self):
        solver = ''
        if self.optimization == OPTIMIZE or self.optimization == MAXIMIZE:
            solver += f's = Optimize()\n'
        else:
            solver += f's = Solver()\n'

        solver += f's.add(f_exact(exact_out) == exact_out)\n'
        solver += f'\n'

        return solver

    def express_samples(self):
        sample_expression = ''
        for s in self.samples:
            sample_expression += f's.push()\n'
            s_expression = [True if i == '1' else False for i in list(f'{s:0{self.graph.num_inputs}b}')]
            # a 1101 is considered as in3,in2,in1,in0 => in3=1, in2=1, in1=0, in0=1
            s_expression.reverse()  # to keep it consistent with the verilog testbench
            sample_expression += f's.add('
            for idx, e in enumerate(s_expression):
                if idx == len(s_expression) - 1:
                    sample_expression += f'{self.graph.input_dict[idx]}=={e})\n'
                else:
                    sample_expression += f'{self.graph.input_dict[idx]}=={e}, '

            sample_expression += f'sol = s.check()\n'
            sample_expression += f'm = s.model()\n'
            sample_expression += f"print(f'{{m = }}')\n"
            sample_expression += f'cur_result = m[f_exact].else_value().as_string()\n'
            sample_expression += f'results.append(cur_result)\n'

            sample_expression += f's.pop()\n\n'

        return sample_expression

    def store_results(self):
        store_results = ''
        store_results += f"with open('{self.pyscript_results_out_path}', 'w') as f:\n" \
                         f"\tfor line in results:\n" \
                         f"\t\tf.write(line)\n" \
                         f"\t\tf.write('\\n')\n"
        store_results += f"print(f'{{results = }}')"
        return store_results

    # TODO: decorators-----------------------------
    def run_z3pyscript_qor(self):
        with open(self.z3_log_path, 'w') as f:
            process = subprocess.run([PYTHON3, self.out_path], stdout=PIPE, stderr=PIPE)

    def run_z3pyscript_labeling(self):
        # print(self.pyscript_files_for_labeling )
        for pyscript in self.pyscript_files_for_labeling:
            with open(self.z3_log_path, 'w') as f:
                process = subprocess.run([PYTHON3, pyscript], stdout=PIPE, stderr=PIPE)

    def run_z3pyscript_random(self):
        with open(self.z3_log_path, 'w') as f:
            process = subprocess.run([PYTHON3, self.out_path], stdout=PIPE, stderr=PIPE)

    def run_z3pyscript_test(self):
        with open(self.z3_log_path, 'w') as f:
            process = subprocess.run([PYTHON3, self.out_path], stdout=PIPE, stderr=PIPE)

        self.set_sample_results(self.import_results())
    # TODO: decorators (end)--------------------------
