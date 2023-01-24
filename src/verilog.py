import os
import regex as re
import random
import numpy as np
import subprocess
import sys
from src.config.path import *
from src.config.config import *
from src.argument import Arguments
from src.utils import *


class Verilog:
    def __init__(self, benchmark_name: str, samples: list = []):
        self.__circuit_name = get_pure_name(benchmark_name)

        folder, extension = INPUT_PATH['ver']
        self.__circuit_in_path = f'{folder}/{benchmark_name}.{extension}'

        folder, extension = OUTPUT_PATH['ver']
        self.__circuit_out_path = f'{folder}/{benchmark_name}.{extension}'

        folder, extension = OUTPUT_PATH['aig']
        self.__aig_out_path = f'{folder}/{benchmark_name}.{extension}'

        folder, extension = TEST_PATH['tb']
        self.__testbench_out_path = f'{folder}/{benchmark_name}_tb.{extension}'

        folder, extension = TEST_PATH['tb']
        self.__tmp_verilog = f'{folder}/{TMP}.{extension}'

        folder, extension = TEST_PATH['iver']
        self.__iverilog_out_path = f'{folder}/{benchmark_name}.{extension}'

        folder, extension = LOG_PATH['iver']
        self.__iverilog_log_path = f'{folder}/{benchmark_name}_{IVERILOG}_{LOG}.{extension}'

        folder, extension = TEST_PATH['vvp']
        self.__vvp_out_path = f'{folder}/{benchmark_name}.{extension}'

        self.__num_inputs, self.__num_outputs = self.extract_module_io()
        self.__sample_results = None
        self.__samples = samples

    @property
    def name(self):
        return self.__circuit_name

    @property
    def num_inputs(self):
        return self.__num_inputs

    @property
    def num_outputs(self):
        return self.__num_outputs

    @property
    def in_path(self):
        return self.__circuit_in_path

    @property
    def out_path(self):
        return self.__circuit_out_path

    @property
    def aig_out_path(self):
        return self.__aig_out_path

    @property
    def cleaned_verilog(self):
        return self.__circuit_out_path

    @property
    def tmp(self):
        return self.__tmp_verilog

    @property
    def testbench(self):
        return self.__testbench_out_path

    @property
    def samples(self):
        return self.__samples

    @property
    def iverilog_out_path(self):
        return self.__iverilog_out_path

    @property
    def iverilog_log_path(self):
        return self.__iverilog_log_path

    @property
    def vvp_in_path(self):
        return self.__iverilog_out_path

    @property
    def vvp_out_path(self):
        return self.__vvp_out_path

    def set_samples(self, samples: np.array or list):
        self.__samples = samples

    @property
    def sample_results(self):
        return self.__sample_results

    def set_sample_results(self, results):
        self.__sample_results = results

    # methods
    def import_results(self):
        arr = []
        with open(self.vvp_out_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.replace('\n', '')
                arr.append(int(line, 2))
        results = np.array(arr)

        return results

    def import_circuit(self):
        with open(self.in_path, 'r') as f:
            lines = f.readlines()
        return lines

    def synthesize_to_gate_level(self):
        yosys_command = f"""
        read_verilog {self.in_path}
        synth -flatten
        opt
        opt_clean -purge
        abc -g AND,OR
        write_verilog -noattr {self.out_path}
        abc -g NAND;
        aigmap;
        opt;
        opt_clean -purge;
        write_aiger {self.aig_out_path};
        """
        with open('log.txt', 'w') as y:
            subprocess.call([YOSYS, '-p', yosys_command], stdout=y)

    def unwrap_variables(self) -> None:
        """

        :return:
        """
        lsoracle_command = f"""
        read_aig {self.aig_out_path};
        write_verilog {self.out_path}
        """
        with open('lsoracle_log.txt', 'w') as f:
            subprocess.call([LSORACLE, '-c', lsoracle_command], stdout=f)
        self.fix_module_name()

    def fix_module_name(self):
        with open(self.out_path, 'r') as f:
            lines = f.readlines()
        with open(self.out_path, 'w') as g:
            for idx, line in enumerate(lines):
                if re.search('top', line):
                    line = line.replace('top', self.name)
                    lines[idx] = line
                    break
            for line in lines:
                g.write(line)

    def create_test_bench(self, samples: 'list[int]' = []):

        # read a clean verilog
        # create a test bench for it
        num = len(self.samples)
        with open(self.testbench, 'w') as f:
            modulename, port_list, inp, n_inputs, out, n_outputs = self.extract_module_info()

            f.write("module " + modulename + "_tb;\n")
            f.write('reg [' + str(n_inputs - 1) + ':0] pi;\n')
            f.write('wire [' + str(n_outputs - 1) + ':0] po;\n')
            f.write(modulename + ' dut(')

            first = True
            inp_count = 0
            out_count = 0

            for i in port_list:
                if not first:
                    f.write(',')
                first = False

                if i in inp:
                    if inp[i] > 1:
                        f.write(' pi[{}:{}] '.format(inp_count + inp[i] - 1, inp_count))
                    else:
                        f.write(' pi[{}] '.format(inp_count))
                    inp_count += inp[i]

                elif i in out:
                    if out[i] > 1:
                        f.write(' po[{}:{}] '.format(out_count + out[i] - 1, out_count))
                    else:
                        f.write(' po[{}] '.format(out_count))
                    out_count += out[i]

                else:
                    print('[Error] Port {} is not defined as input or output.'.format(i))
                    sys.exit(0)

            f.write(');\n')

            f.write("initial\n")
            f.write("begin\n")

            for idx, sample in enumerate(self.samples):
                f.write('# 1  pi=' + str(n_inputs) + '\'b')
                f.write('{0:0>{1}}'.format(str(bin(sample))[2:], n_inputs))
                f.write(';\n')
                f.write("#1 $display(\"%b\", po);\n")

            f.write("end\n")
            f.write("endmodule\n")

    def extract_module_io(self) -> (int, int):
        clean_verilog = self.in_path
        yosys_command = 'read_verilog ' + clean_verilog + '; synth -flatten; opt; opt_clean; techmap; write_verilog ' + self.tmp + ';\n'
        subprocess.call([YOSYS, '-p', yosys_command], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        with open(self.tmp) as tmp_file:
            inp = {}
            inp_count = 0
            out = {}
            out_count = 0
            modulename = None
            line = tmp_file.readline()
            while line:
                tokens = re.split('[ ()]', line.strip().strip(';').strip())

                if len(tokens) > 0 and tokens[0] == 'module' and modulename is None:
                    modulename = tokens[1]
                    port_list = re.split('[,()]', line.strip().strip(';').strip())[1:]
                    port_list = [s.strip() for s in port_list if s.strip() != '']

                if len(tokens) == 2 and (tokens[0] == 'input' or tokens[0] == 'output'):
                    if tokens[0] == 'input':
                        inp[tokens[1]] = 1
                        inp_count += 1
                    if tokens[0] == 'output':
                        out[tokens[1]] = 1
                        out_count += 1

                if len(tokens) == 3 and (tokens[0] == 'input' or tokens[0] == 'output'):
                    range_str = tokens[1][1:-1].split(':')
                    range_int = list(map(int, range_str))
                    length = max(range_int) - min(range_int) + 1
                    if tokens[0] == 'input':
                        inp[tokens[2]] = length
                        inp_count += length
                    if tokens[0] == 'output':
                        out[tokens[2]] = length
                        out_count += length

                line = tmp_file.readline()

        os.remove(self.tmp)

        return inp_count, out_count

    def extract_module_info(self) -> 'tuple(str, list(str), dict, int, dict, int)':
        """
        reads a verilog file and extracts the signature
        :return: a tuple containing the modulename, the list of input and output names, two dictionary that hold the bitwidth
        of all inputs and outputs, and the number of inputs and outputs
        """
        clean_verilog = self.out_path
        yosys_command = 'read_verilog ' + clean_verilog + '; synth -flatten; opt; opt_clean; techmap; write_verilog ' + self.tmp + ';\n'
        subprocess.call([YOSYS, '-p', yosys_command], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

        with open(self.tmp) as tmp_file:
            inp = {}
            inp_count = 0
            out = {}
            out_count = 0
            modulename = None
            line = tmp_file.readline()
            while line:
                tokens = re.split('[ ()]', line.strip().strip(';').strip())

                if len(tokens) > 0 and tokens[0] == 'module' and modulename is None:
                    modulename = tokens[1]
                    port_list = re.split('[,()]', line.strip().strip(';').strip())[1:]
                    port_list = [s.strip() for s in port_list if s.strip() != '']

                if len(tokens) == 2 and (tokens[0] == 'input' or tokens[0] == 'output'):
                    if tokens[0] == 'input':
                        inp[tokens[1]] = 1
                        inp_count += 1
                    if tokens[0] == 'output':
                        out[tokens[1]] = 1
                        out_count += 1

                if len(tokens) == 3 and (tokens[0] == 'input' or tokens[0] == 'output'):
                    range_str = tokens[1][1:-1].split(':')
                    range_int = list(map(int, range_str))
                    length = max(range_int) - min(range_int) + 1
                    if tokens[0] == 'input':
                        inp[tokens[2]] = length
                        inp_count += length
                    if tokens[0] == 'output':
                        out[tokens[2]] = length
                        out_count += length

                line = tmp_file.readline()

        os.remove(self.tmp)

        return modulename, port_list, inp, inp_count, out, out_count

    def run_test_bench(self):
        iverilog_command = f'{IVERILOG} -o {self.iverilog_out_path} ' \
                           f'{self.cleaned_verilog} ' \
                           f'{self.testbench} '

        vvp_command = f'{self.iverilog_out_path}'

        with open(f'{self.iverilog_log_path}', 'w') as f:
            subprocess.call(iverilog_command, shell=True, stdout=f)

        with open(f'{self.vvp_out_path}', 'w') as f:
            subprocess.call([VVP, vvp_command], stdout=f)

        os.remove(f'{self.iverilog_out_path}')

        self.set_sample_results(self.import_results())

    def export_circuit(self):
        pass

    def __repr__(self):
        return f'An object of class Verilog\n' \
               f'{self.name = }\n' \
               f'{self.in_path = }\n' \
               f'{self.out_path = }\n'
