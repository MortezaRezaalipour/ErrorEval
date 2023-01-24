# tools
YOSYS = 'yosys'
SLANG = 'slang'
LSORACLE = 'lsoracle'
IVERILOG = 'iverilog'
VVP = 'vvp'
DOT = 'dot'

# regex constants
POSSIBLE_GATES=f'and|AND|or|OR|not|NOT'
Z3_GATES_DICTIONARY = {
    'and':'And',
    'AND':'And',
    'or':'Or',
    'OR':'Or',
    'not':'Not',
    'NOT':'Not'
}
REDUNDANT_FIELDS=[
    'height', 'width', 'pos',
    'color', 'fontcolor',
    'rects',
    'contraction', 'contraction'
]

# random constants
TMP = 'tmp'
LOG = 'log'
Z3BOOL = 'Bool'
PYTHON3 = 'python3'
Z3 = 'z3py'