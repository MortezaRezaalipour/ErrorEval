import subprocess
import networkx as nx
import re
from src.config.path import *
from src.config.config import *

from src.argument import Arguments


class Graph:
    def __init__(self, benchmark_name, is_clean=False):

        self.__graph_name = benchmark_name
        folder, extension = INPUT_PATH['gv']
        self.__graph_in_path = f'{folder}/{benchmark_name}.{extension}'

        folder, extension = OUTPUT_PATH['gv']
        self.__graph_out_path = f'{folder}/{benchmark_name}.{extension}'

        folder, extension = OUTPUT_PATH['dot']
        self.__dot_in_path = f'{folder}/{benchmark_name}.{extension}'

        folder, extension = OUTPUT_PATH['ver']
        self.__verilog_in_path = f'{folder}/{benchmark_name}.{extension}'

        self.__graph = self.import_graph()

        self.__num_inputs = -1
        self.__num_outputs = -1
        self.__num_gates = -1
        self.__sorted_node_list = None

        self.__is_clean = is_clean
        if not self.is_clean:
            self.clean_graph()
        self.count_iog()
        self.sort_graph()

        self.__input_dict = self.extract_inputs()
        self.__output_dict = self.extract_outputs()
        print(f'{self.input_dict = }')
        print(f'{self.output_dict = }')


    @property
    def name(self):
        return self.__graph_name

    @property
    def is_clean(self):
        return self.__is_clean

    def set_is_clean(self, is_clean: bool):
        self.__is_clean = is_clean

    @property
    def in_path(self):
        return self.__graph_in_path

    @property
    def out_path(self):
        return self.__graph_out_path

    @property
    def verilog_in_path(self):
        return self.__verilog_in_path

    @property
    def dot_in_path(self):
        return self.__dot_in_path

    @property
    def graph(self):
        return self.__graph

    def set_graph(self, graph):
        self.__graph = graph

    @property
    def input_dict(self):
        return self.__input_dict

    def set_input_dict(self, input_dict):
        self.__input_dict = input_dict

    @property
    def output_dict(self):
        return self.__output_dict

    def set_output_dict(self, output_dict):
        self.__output_dict = output_dict

    @property
    def num_inputs(self):
        return self.__num_inputs

    def set_num_inputs(self, input_count):
        self.__num_inputs = input_count

    @property
    def num_outputs(self):
        return self.__num_outputs

    def set_num_outputs(self, output_count):
        self.__num_outputs = output_count

    @property
    def num_gates(self):
        return self.__num_gates

    def set_num_gates(self, gate_count):
        self.__num_gates = gate_count

    @property
    def sorted_node_list(self):
        return self.__sorted_node_list

    def set_sorted_node_list(self, sorted_node_list):
        self.__sorted_node_list = sorted_node_list

    def extract_inputs(self):
        print(f'Extracting inputs...')
        input_dict = {}
        for n in self.graph.nodes():
            if self.is_pi(n):
                idx = re.search('\d+', n).group()
                input_dict[int(idx)] = n
        return input_dict


    def extract_outputs(self):
        print(f'Extracting outputs...')
        output_dict = {}
        for n in self.graph.nodes():
            if self.is_po(n):
                idx = re.search('\d+', n).group()
                output_dict[int(idx)] = n
        return output_dict

    # methods
    def create_sort_map(self) -> 'dict[str, str]':
        """
        sorts the nodes in topological order and returns them in a form of a list
        :return: a sorted list of node labels
        """
        sorted_node_list = list(nx.topological_sort(self.graph))

        sort_map = {}
        idx = 0
        for n in sorted_node_list:
            if re.search(r'in\d+', n):
                sort_map[n] = n
            elif re.search(r'out\d+', n):
                sort_map[n] = n
            elif re.search(r'g\d+', n):
                sort_map[n] = f'g{idx}'
                idx += 1
        return sort_map

    def sort_graph(self):
        sort_map = self.create_sort_map()
        self.set_graph(nx.relabel_nodes(self.graph, sort_map))
        self.set_sorted_node_list(list(nx.topological_sort(self.graph)))

        tmp_graph = nx.DiGraph()
        tmp_graph.add_nodes_from(self.sorted_node_list)
        tmp_graph.add_edges_from(self.graph.edges())
        for (k, v) in self.graph.nodes(data=True):
            for attr in v.keys():
                tmp_graph.nodes[k][attr] = v[attr]

        self.set_graph(tmp_graph)
        # print(f'{tmp_graph.nodes = }')

    def count_iog(self):
        """
        counts the number of primary inputs and outputs, and gates and sets the corresponding fields
        :return: Nothing
        """
        count_i = 0
        count_o = 0
        count_g = 0
        for n in self.graph.nodes:
            if re.search(r'in\d+', n) and re.search(r'in\d+', self.graph.nodes[n]['label']):
                count_i += 1
            elif re.search(r'out\d+', n) and re.search(r'out\d+', self.graph.nodes[n]['label']):
                count_o += 1
            elif re.search(r'g\d+', n) and re.search(POSSIBLE_GATES, self.graph.nodes[n]['label']):
                count_g += 1
        self.set_num_inputs(count_i)
        self.set_num_outputs(count_o)
        self.set_num_gates(count_g)

    def convert_verilog_to_gv(self):
        yosys_command = f"""
            read_verilog {self.verilog_in_path}
            show -prefix {self.out_path[:-3]} -format gv
            """
        with open(f'yosys_graph.log', 'w') as y:
            subprocess.call([YOSYS, '-p', yosys_command], stdout=y)
        self.fix_direction()

    def fix_direction(self):
        dot_command = f'{DOT} {self.dot_in_path} -Grankdir=TB -o {self.out_path}'
        subprocess.call([dot_command], shell=True)

    def clean_graph(self):
        self.clean_input_labels()
        self.clean_output_labels()
        self.clean_wire_labels()
        self.clean_gate_labels()
        self.merge_buffers_into_gates()
        self.merge_wires_into_gates()
        self.relabel_nodes()
        self.delete_extra_fields()
        self.set_is_clean(True)
        self.count_iog()

    def delete_extra_fields(self):
        for n in self.graph.nodes:
            for field in REDUNDANT_FIELDS:
                if field in self.graph.nodes[n].keys():
                    self.graph.nodes[n].pop(field)
        # delete all edge attributes
        for (n1, n2, d) in self.graph.edges(data=True):
            d.clear()

    def clean_input_labels(self):
        self.delete_extra_fields()
        for n in self.graph.nodes:
            if self.is_pi(n):
                idx = re.search('\d+', self.graph.nodes[n]['label']).group()  # pi7 => idx=7
                self.graph.nodes[n]['label'] = f'in{idx}'
                self.graph.nodes[n]['shape'] = f'circle'

    def clean_output_labels(self):
        for n in self.graph.nodes:
            if self.is_po(n):
                idx = re.search('\d+', self.graph.nodes[n]['label']).group()  # po12 => idx=12
                self.graph.nodes[n]['label'] = f'out{idx}'
                self.graph.nodes[n]['shape'] = f'doublecircle'

    def clean_wire_labels(self):
        for n in self.graph.nodes:
            if self.is_wire(n):
                idx = re.search('\d+', self.graph.nodes[n]['label']).group()  # n317 => idx=317
                self.graph.nodes[n]['label'] = f'g{idx}'
                self.graph.nodes[n]['shape'] = f'square'

    def clean_gate_labels(self):
        for n in self.graph.nodes:
            if self.is_gate(n):
                if re.search(POSSIBLE_GATES, self.graph.nodes[n]['label']):
                    cur_gate = re.search(POSSIBLE_GATES, self.graph.nodes[n]['label']).group()
                    self.graph.nodes[n]['label'] = cur_gate
                    self.graph.nodes[n]['shape'] = 'invhouse'

    def merge_buffers_into_gates(self):
        tmp_graph = self.graph.copy(as_view=False)
        for e in self.graph.edges:
            if self.graph.nodes[e[1]]['label'] == 'BUF':
                src_node = e[0]
                des_node = e[1]
                tmp_graph = nx.contracted_nodes(tmp_graph, src_node, des_node, self_loops=False)
        self.set_graph(tmp_graph)

    def merge_wires_into_gates(self):
        tmp_graph = self.graph.copy(as_view=False)
        for e in self.graph.edges:
            if (re.search(POSSIBLE_GATES, self.graph.nodes[e[0]]['label']) and
                    re.search('g\d+', self.graph.nodes[e[1]]['label'])):
                src_node = e[0]
                des_node = e[1]
                tmp_graph = nx.contracted_nodes(tmp_graph, src_node, des_node, self_loops=False)
        self.set_graph(tmp_graph)

    def relabel_nodes(self):
        tmp_graph = self.graph.copy()
        gate_idx = 0
        for n in self.graph.nodes:
            if self.is_pi(n):
                # print(f"{self.graph.nodes[n]['label'] = } is a PI")
                old_name = n
                new_name = self.graph.nodes[n]['label']
                # print(old_name)

                mapping = {old_name: new_name}
                tmp_graph = nx.relabel_nodes(tmp_graph, mapping)
            elif self.is_po(n):
                # print(f"{self.graph.nodes[n]['label'] = } is a PO")
                old_name = n
                new_name = self.graph.nodes[n]['label']
                # print(old_name)

                mapping = {old_name: new_name}
                tmp_graph = nx.relabel_nodes(tmp_graph, mapping)
            elif self.is_merged_gate(n):
                # print(f"{self.graph.nodes[n]['label'] = } is a merged gate!")
                old_name = n
                new_name = f'g{gate_idx}'
                gate_idx += 1
                # print(old_name)

                mapping = {old_name: new_name}
                tmp_graph = nx.relabel_nodes(tmp_graph, mapping)
            elif self.is_cleaned_gate(n):
                # print(f"{self.graph.nodes[n]['label'] = } is a cleaned gate!")
                old_name = n
                new_name = f'g{gate_idx}'
                gate_idx += 1
                # print(old_name)

                mapping = {old_name: new_name}
                tmp_graph = nx.relabel_nodes(tmp_graph, mapping)
            else:
                print(f'{n = }')
                print('WARNING! No mapping needed!')
        self.set_graph(tmp_graph)

    def is_pi(self, node):
        if re.search(r'pi\d+|in\d+', self.graph.nodes[node]['label']):
            return True
        else:
            return False

    def is_po(self, node):
        if re.search(r'po\d+|out\d+', self.graph.nodes[node]['label']):
            return True
        else:
            return False

    def is_wire(self, node):
        if (not self.is_pi(node) and not self.is_po(node) and not self.is_gate(node) and
                re.search('diamond', self.graph.nodes[node]['shape'])):
            return True
        else:
            return False

    def is_cleaned_gate(self, node):
        if (re.search('invhouse', self.graph.nodes[node]['shape']) and
                'contraction' not in self.graph.nodes[node].keys() and 'contractions' not in self.graph.nodes[node]):
            return True
        else:
            return False

    def is_gate(self, node):
        if re.search('record', self.graph.nodes[node]['shape']):
            return True
        else:
            return False

    def is_buff(self, node):
        if (re.search('BUF', self.graph.nodes[node]['label']) and
                re.search('box', self.graph.nodes[node]['shape'])):
            return True
        else:
            return False

    def is_merged_gate(self, node):
        if (re.search(POSSIBLE_GATES, self.graph.nodes[node]['label']) and
                re.search('invhouse', self.graph.nodes[node]['shape']) and
                ('contraction' in self.graph.nodes[node].keys() or 'contractions' in self.graph.nodes[node].keys())):
            return True
        else:
            return False

    def import_graph(self):
        DG = nx.drawing.nx_agraph.read_dot(self.out_path)
        return DG

    def export_graph(self):
        with open(self.out_path, 'w') as f:
            f.write(f"strict digraph \"\" {{\n")
            for n in self.graph.nodes:
                self.export_node(n, f)
            for e in self.graph.edges:
                self.export_edge(e, f)
            f.write(f"}}\n")
        # nx.drawing.nx_agraph.write_dot(self.graph, self.out_path)

    def export_node(self, n, file_handler: 'class _io.TextIOWrapper'):
        # in3	[label=in3,shape=circle];
        if self.is_pi(n) or self.is_po(n):
            line = f"{n} [label=\"{self.graph.nodes[n]['label']}\", shape={self.graph.nodes[n]['shape']}];\n"
        else:
            line = f"{n} [label=\"{self.graph.nodes[n]['label']}\\n{n}\", shape={self.graph.nodes[n]['shape']}];\n"

        file_handler.write(line)

    def export_edge(self, e: tuple, file_handler):
        # in3 -> g2;
        src, des = e
        line = f"{src} -> {des};\n"
        file_handler.write(line)

    def convert_to_verilog(self):
        pass

    def __repr__(self):
        return f'An object of class Graph\n' \
               f'{self.name = }\n' \
               f'{self.in_path = }\n' \
               f'{self.out_path = }\n' \
               f'{self.num_inputs = }\n' \
               f'{self.num_outputs = }\n' \
               f'{self.num_gates = }\n'
