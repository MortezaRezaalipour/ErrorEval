import os
import re

name_dict = {
    'abs_diff_8_0.1' : 'abs_diff_i16_o9',
    'abs_diff_10' : 'abs_diff_i20_o10',
    
    'adder_8': 'adder_i16_09',
    'adder_16': 'adder_i32_o17',

    'bin_squared_6': 'bin_squared_i12_o14',
    'bin_squared_8_5': 'bin_squared_i16_o18',

    'madd_4': 'madd_i18_o12',
    'madd_8': 'madd_i24_o16',

    'mul_6': 'mul_i12_o12',
    'mul_8': 'mul_i16_o16',

    'sad_4': 'sad_i20_o5',
    'sad_8': 'sad_i40_o10'
}


def main():
    all_files = [f for f in os.listdir('.')]
    relevant_files = []
    for f in all_files:
        if f.endswith('.gv'):
            relevant_files.append(f)
    
    for name in relevant_files:
        for benchname in name_dict.keys():
            if re.search(benchname, name):
                new_name = name.replace(benchname, name_dict[benchname])
                print(f'{name} change into => {new_name}')
                os.rename(name, new_name)


if __name__ == "__main__":
    main()