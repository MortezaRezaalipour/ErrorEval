import numpy as np
import re
import subprocess
from src.utils import *
from src.graph import *


class Z3solver:
    def __init__(self, benchmark_name: str, approximate_benchmark_name: str = None, samples: list = []):
        self.__circuit_name = get_pure_name(benchmark_name)
        folder, extension = OUTPUT_PATH['gv']
        self.__graph_in_path = f'{folder}/{benchmark_name}.{extension}'

        folder, extension = OUTPUT_PATH['z3']
        self.__z3_out_path = f'{folder}/{benchmark_name}.{extension}'

        self.__graph = Graph(benchmark_name, True)

        folder, extension = TEST_PATH['z3']
        self.__pyscript_results_out_path = f'{folder}/{benchmark_name}.{extension}'

        folder, extension = LOG_PATH['z3']
        self.__z3_log_path = f'{folder}/{benchmark_name}_{Z3}_{LOG}.{extension}'

        self.__approximate_verilog_in_path = None
        self.__approximate_graph = None

        if approximate_benchmark_name:
            folder, extension = INPUT_PATH['app_gv']
            self.__approximate_verilog_in_path = f'{folder}/{approximate_benchmark_name}.{extension}'
            self.__approximate_graph = Graph(approximate_benchmark_name, True)
            self.relabel_approximate_graph()
            self.approximate_graph.set_input_dict(self.approximate_graph.extract_inputs())
            self.approximate_graph.set_output_dict(self.approximate_graph.extract_outputs())
            self.approximate_graph.set_gate_dict(self.approximate_graph.extract_gates())
            self.approximate_graph.set_constant_dict(self.approximate_graph.extract_constants())

        folder, extension = OUTPUT_PATH['report']
        self.__z3_report = f'{folder}/{benchmark_name}.{extension}'

        self.__samples = samples
        self.__sample_results = None

        self.__z3string = None

        self.__z3pyscript = None

        self.__strategy = DEFAULT_STRATEGY

    @property
    def name(self):
        return self.__circuit_name

    @property
    def graph_in_path(self):
        return self.__graph_in_path

    @property
    def out_path(self):
        return self.__z3_out_path

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
    def z3_report(self):
        return self.__z3_report


    # TODO
    # Deprecated
    #
    # def append_z3pyscript(self, that_script):
    #     self.__z3pyscript = f'{self.z3pyscript}\n' \
    #                         f'{that_script}'

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

    @property
    def graph(self):
        return self.__graph

    @property
    def approximate_graph(self):
        return self.__approximate_graph

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

    def convert_gv_to_z3pyscript_maxerror_qor(self):

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

    def convert_gv_to_z3pyscript_maxerror_labelling(self):
        pass

    def convert_gv_to_z3pyscript_xpat(self):
        pass

    # TODO
    # for other back-ends as well

    def declare_error_distance_function(self):
        ed_function = ''
        ed_function += f"f_exact = Function('f_exact', IntSort(), IntSort())\n" \
                       f"f_approx = Function('f_approx', IntSort(), IntSort())\n"
        ed_function += f"f_error = Function('f_error', IntSort(), IntSort(), IntSort())\n"
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
        else:
            print(f'ERROR!!! no strategy is specified!')
            exit()
        return strategy_expressed

    def declare_stats(self):
        stats = ''
        stats = f'foundWCE = False\n' \
                f'stats: dict = {{}}\n' \
                f"stats['wce'] = 0\n" \
                f"stats['et'] = 0\n" \
                f"stats['num_sats'] = 0\n" \
                f"stats['num_unsats'] = 0\n" \
                f"stats['sat_runtime'] = 0.0\n" \
                f"stats['unsat_runtime'] = 0.0\n" \
                f"stats['jumps'] = []\n"
        return stats

    def express_monotonic_while_loop(self):
        loop = ''

        loop += f'start_whole = time.time()\n' \
                f's = Solver()\n' \
                f"stats['jumps'].append(stats['et'])\n" \
                f'while(not foundWCE):\n' \
                f'{TAB}start_iteration = time.time()\n' \
                f'{TAB}s.push()\n' \
                f'{TAB}s.add(f_exact(exact_out) == exact_out)\n' \
                f'{TAB}s.add(f_approx(approx_out) == approx_out)\n' \
                f'{TAB}s.add(f_error(exact_out, approx_out) == exact_out - approx_out)\n' \
                f"{TAB}s.add(z3_abs(f_error(exact_out, approx_out)) > stats['et'])\n" \
                f"{TAB}response = s.check()\n"

        loop += self.express_monotonic_while_loop_sat()
        loop += self.express_monotonic_while_loop_unsat()

        loop += f"end_whole = time.time()\n" \
                f"with open('{self.z3_report}', 'w') as f:\n" \
                f"{TAB}csvwriter = csv.writer(f)\n" \
                f"{TAB}header = ['field', 'value']\n" \
                f"{TAB}csvwriter.writerow(['Experiment', 'qor-evaluation'])\n" \
                f"{TAB}csvwriter.writerow(['WCE', stats['wce']])\n" \
                f"{TAB}csvwriter.writerow(['Total Runtime', stats['sat_runtime'] + stats['unsat_runtime']])\n" \
                f"{TAB}csvwriter.writerow(['SAT Runtime', stats['sat_runtime']])\n" \
                f"{TAB}csvwriter.writerow(['UNSAT Runtime', stats['unsat_runtime']])\n" \
                f"{TAB}csvwriter.writerow(['Number of SAT calls', stats['num_sats']])\n" \
                f"{TAB}csvwriter.writerow(['Number of UNSAT calls', stats['num_unsats']])\n"


        return loop

    def express_monotonic_while_loop_sat(self):
        if_sat = ''
        if_sat +=   f"{TAB}if response == sat:\n" \
                    f"{TAB}{TAB}print(f'sat')\n" \
                    f"{TAB}{TAB}returned_model = s.model()\n" \
                    f"{TAB}{TAB}print(f'{{returned_model = }}')\n" \
                    f"{TAB}{TAB}print(f\"{{returned_model[f_exact].else_value() = }}\")\n" \
                    f"{TAB}{TAB}print(f\"{{returned_model[f_approx].else_value() = }}\")\n" \
                    f"{TAB}{TAB}print(f\"{{returned_model[f_error].else_value() = }}\")\n" \
                    f"{TAB}{TAB}returned_value = abs(int(returned_model[f_error].else_value().as_long()))\n" \
                    f"{TAB}{TAB}returned_value_reval = abs(int(returned_model.evaluate(f_error(exact_out, approx_out)).as_long()))\n" \
                    f"{TAB}{TAB}if returned_value == returned_value_reval:\n" \
                    f"{TAB}{TAB}{TAB}print(f'double-check is passed!')\n" \
                    f"{TAB}{TAB}else:\n" \
                    f"{TAB}{TAB}{TAB}print(f'ERROR!!! double-check failed! exiting...')\n" \
                    f"{TAB}{TAB}{TAB}exit()\n" \
                    f"{TAB}{TAB}end_iteration = time.time()\n" \
                    f"{TAB}{TAB}stats['et'] = returned_value\n" \
                    f"{TAB}{TAB}stats['num_sats'] += 1\n" \
                    f"{TAB}{TAB}stats['sat_runtime'] += (end_iteration - start_iteration)\n" \
                    f"{TAB}{TAB}stats['jumps'].append(returned_value)\n"
        return if_sat

    def express_monotonic_while_loop_unsat(self):
        if_unsat = ''
        if_unsat += f"\n" \
                    f"{TAB}if response == unsat:\n" \
                    f"{TAB}{TAB}print('unsat')\n" \
                    f"{TAB}{TAB}end_iteration = time.time()\n" \
                    f"{TAB}{TAB}foundWCE = True\n" \
                    f"{TAB}{TAB}stats['num_unsats'] += 1\n" \
                    f"{TAB}{TAB}stats['unsat_runtime'] += (end_iteration - start_iteration)\n" \
                    f"{TAB}{TAB}stats['wce'] = stats['et']\n"
        return if_unsat


    def express_monotonic_strategy(self):
        monotonic_strategy = ''
        monotonic_strategy += self.declare_stats()
        monotonic_strategy += self.express_monotonic_while_loop()
        return monotonic_strategy

    def express_mc_strategy(self):
        pass

    def express_bisection_strategy(self):
        pass

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
        # for n in self.approximate_graph.graph.nodes:
        #     print(f'{n = }, {self.approximate_graph.graph.nodes[n]= }')
        exact_circuit_declaration = ''
        # inputs
        for n in self.approximate_graph.graph.nodes:
            if re.search(r'in\d+', self.approximate_graph.graph.nodes[n]['label']):
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
        # print(f'expressing the original circuit')
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
            if self.approximate_graph.is_cleaned_gate(n):
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
        if self.approximate_graph.is_cleaned_gate(this_key):
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

        elif self.approximate_graph.is_cleaned_pi(this_key):
            pass
        elif self.approximate_graph.is_cleaned_po(this_key):
            cur_node = f'{this_key}='
            predecessor_list = list(self.approximate_graph.graph.predecessors(this_key))
            for idx, u in enumerate(predecessor_list):
                cur_node += f'{u}'
        return cur_node

    def declare_original_output(self):
        output_declaration = ''

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

        for i in range(self.approximate_graph.num_outputs):
            output_declaration += f"approx_out{i}=Int('approx_out{i}')\n"
            output_declaration += f"approx_out{i}={self.approximate_graph.output_dict[i]}*{2 ** i}\n"

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
        solver += f's = Solver()\n' \
                  f's.add(f_exact(exact_out) == exact_out)'
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

    def run_z3pyscript(self):
        # print(f'{self.out_path = }')
        with open(self.z3_log_path, 'w') as f:
            subprocess.call([PYTHON3, self.out_path], stdout=f)
        self.set_sample_results(self.import_results())
