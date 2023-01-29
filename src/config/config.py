# tools
YOSYS = 'yosys'
SLANG = 'slang'
LSORACLE = 'lsoracle'
IVERILOG = 'iverilog'
VVP = 'vvp'
DOT = 'dot'

# regex constants
POSSIBLE_GATES=f'and|AND|or|OR|not|NOT'
CONST_1 = f"1'1"
CONST_0 = f"1'0"


# for z3
Z3_GATES_DICTIONARY = {
    'and':'And',
    'AND':'And',
    'or':'Or',
    'OR':'Or',
    'not':'Not',
    'NOT':'Not',
    'T': 'True',
    'True': 'True',
    'true': 'True',
    'TRUE': 'True',
    'F': 'False',
    'False': 'False',
    'false': 'False',
    'FALSE': 'False'
}
REDUNDANT_FIELDS=[
    'height', 'width', 'pos',
    'color', 'fontcolor',
    'rects',
    'contraction', 'contraction',
    'style'
]

# random constants
TMP = 'tmp'
LOG = 'log'
Z3BOOL = 'Bool'
PYTHON3 = 'python3'
Z3 = 'z3py'
SHAPE = 'shape'
LABEL = 'label'
TAB = '\t'

# strategies
MONOTONIC = 'monotonic'
BISECTION = 'bisection'
MC = 'mc'
DEFAULT_STRATEGY = MONOTONIC

# Experiments
QOR = 'qor'
RANDOM = 'random-pruning'
SINLE = 'single_gate_removal'
