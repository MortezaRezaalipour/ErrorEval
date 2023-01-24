import numpy as np
import re
import subprocess
from src.utils import *
from src.graph import *


class Z3solver:
    def __init__(self, benchmark_name: str, samples: list = []):
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


        self.__samples = samples
        self.__sample_results = None

        self.__z3string = None

        self.__z3pyscript = None

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
    def z3pyscript(self):
        return self.__z3pyscript

    def set_z3pyscript(self, this_script):
        self.__z3pyscript = this_script

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
        print(f'importing results...')
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

    def import_z3_expression(self):
        pass

    def convert_gv_to_z3pyscript_Maxerror(self):
        import_string = self.create_imports()
        abs_function = self.create_abs_function()
        exact_circuit_declaration = self.declare_exact_circuit()
        exact_circuit_expression = self.express_exact_circuit()
        output_declaration = self.declare_exact_output()
        exact_function = self.declare_exact_function()
        solver = self.declare_solver()
        sample_expression = self.express_samples()
        store_results = self.store_results()
        self.set_z3pyscript(import_string + abs_function + exact_circuit_declaration + exact_circuit_expression +
                            output_declaration + exact_function + solver + sample_expression + store_results)

    def convert_gv_to_z3pyscript_BF(self):
        pass

    #TODO
    # for other back-ends as well

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
        abs_function = f'def abs(x):\n' \
                       f'\treturn If(x >= 0, x, -x)\n' \
                       f'\n'
        return abs_function

    def declare_exact_circuit(self):
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

    def declare_gate(self, this_key: str):
        declaration = f"{this_key} = {Z3BOOL}('{this_key}')"
        return declaration

    def express_exact_circuit(self):
        exact_circuit_function = ''
        for n in self.graph.graph.nodes:
            exact_circuit_function += f'{self.express_gate(n)}\n'
        exact_circuit_function += f'\n'
        return exact_circuit_function

    def express_gate(self, this_key: str):
        # sth like this: g110 = Not(And(g108, g109))
        cur_node = ''
        if self.is_gate(this_key):
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

        elif self.is_pi(this_key):
            pass
        elif self.is_po(this_key):
            cur_node = f'{this_key}='
            predecessor_list = list(self.graph.graph.predecessors(this_key))
            for idx, u in enumerate(predecessor_list):
                cur_node += f'{u}'
        return cur_node

    def is_gate(self, this_key):
        if re.search(r'g\d+', this_key) and re.search(POSSIBLE_GATES, self.graph.graph.nodes[this_key]['label']):
            return True
        else:
            return False

    def is_pi(self, this_key):
        if re.search(r'in\d+', this_key) and re.search(r'in\d+', self.graph.graph.nodes[this_key]['label']):
            return True
        else:
            return False

    def is_po(self, this_key):
        if re.search(r'out\d+', this_key) and re.search(r'out\d+', self.graph.graph.nodes[this_key]['label']):
            return True
        else:
            return False

    def declare_exact_output(self):
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

    def declare_exact_function(self):
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
            s_expression.reverse() # to keep it consistent with the verilog testbench
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
        print(f'{self.out_path = }')
        with open(self.z3_log_path, 'w') as f:
            subprocess.call([PYTHON3, self.out_path], stdout=f)
        self.set_sample_results(self.import_results())
