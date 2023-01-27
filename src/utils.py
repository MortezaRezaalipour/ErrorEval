import re
import subprocess
from .config.path import *
from .config.config import *

def get_pure_name(file_name: str) -> str:
    if file_name is None:
        return file_name
    name = file_name
    if re.search('/', file_name):
        name = file_name.split('/')[-1]
    if re.search('\.', name):
        name = name.split('.')[0]
    return name

def fix_direction(file_name: str) -> str:
    file_name = get_pure_name(file_name)
    folder, extension = OUTPUT_PATH['dot']
    dot_in_path = f'{folder}/{file_name}.{extension}'
    folder, extension = OUTPUT_PATH['gv']
    gv_out_path = f'{folder}/{file_name}.{extension}'

    dot_command = f'{DOT} {dot_in_path} -Grankdir=TB -o {gv_out_path}'
    subprocess.call([dot_command], shell=True)

def convert_verilog_to_gv(file_name: str) -> None:
    file_name = get_pure_name(file_name)

    folder, extension = OUTPUT_PATH['ver']
    verilog_in_path = f'{folder}/{file_name}.{extension}'

    folder, extension = OUTPUT_PATH['gv']
    gv_out_path = f'{folder}/{file_name}.{extension}'

    yosys_command = f"""
        read_verilog {verilog_in_path}
        show -prefix {gv_out_path[:-3]} -format gv
        """
    with open(f'yosys_graph.log', 'w') as y:
        subprocess.call([YOSYS, '-p', yosys_command], stdout=y)
    fix_direction(file_name)