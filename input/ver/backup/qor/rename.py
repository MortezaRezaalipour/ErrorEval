import os
import re


NAME_DICT:dict = {
    'abs_diff_8': 'abs_diff_i16_o9', 'abs_diff_10': 'abs_diff_i20_o10', 'abs_diff_8_0.1': 'abs_diff_i16_o9',
    'adder_8': 'adder_i16_o9', 'adder_16': 'adder_i32_o17',
    'bin_squared_6': 'bin_sq_i12_o14', 'bin_squared_8_5':'bin_sq_i16_o18',
    'mul_6':'mul_i12_o12', 'mul_8':'mul_i16_o16',
    'sad_4':'sad_i20_o5', 'sad_8':'sad_i40_o9',
    'madd_4':'madd_i18_o12', 'madd_8':'madd_i24_o16'
}

def find_folders():
    all_folders = [f for f in os.listdir('.')]
    rel_folders = []
    for f in all_folders:
        if f in NAME_DICT:
            rel_folders.append(f)
    return rel_folders
    
def find_files(folder:str):
    all_files = [f for f in os.listdir(folder)]
    rel_files = []
    for f in all_files:
        if f.endswith('.v'):
            rel_files.append(f)
    return rel_files

def fix_names(folder, file):
    
    old_name = f'{folder}/{file}'
    if re.search(r'_re', file):
        file  = file.replace("_re", "")
    if re.search(r'_n\d+', file):
        partitions = re.search(r'_n\d+', file).group()
        file = file.replace(partitions, "")
    for key in NAME_DICT.keys():
        if re.search(key, file):
            file = file.replace(key, NAME_DICT[key])
    
    new_name = f'{folder}/{file}'
    os.rename(old_name, new_name)


def main():
    rel_folders = find_folders()
    for folder in rel_folders:
        rel_files = find_files(folder)
        for file in rel_files:
            fix_names(folder, file)

if __name__ == "__main__":
    main()