import ast
from functools import cmp_to_key

def pair_packet_string(pkg_str):
    return [ast.literal_eval(pkg) for pkg in pkg_str.split('\n')]

with open('1.txt') as fp:
    packet_pairs = list(map(pair_packet_string, fp.read().split('\n\n')))

def comp_value(fst, snd):
    if isinstance(fst, list) and isinstance(snd, list):
        return comp_pkg_pair([fst, snd])
    
    if isinstance(fst, list) and not isinstance(snd, list):
        return comp_pkg_pair([fst, [snd]])
    if not isinstance(fst, list) and isinstance(snd, list):
        return comp_pkg_pair([[fst], snd])

    if fst == snd:
        return 0
    elif fst < snd:
        return 1
    else:
        return -1

def comp_pkg_pair(pkg_pair):
    com_results = [comp_value(fst, snd) for fst,snd in zip(*pkg_pair)]

    try:
        fst_false_com = com_results.index(-1)
    except:
        fst_false_com = -1
    try:
        fst_term_comp = com_results.index(1)
    except:
        fst_term_comp = -1
    
    if fst_term_comp != -1 and ( fst_term_comp < fst_false_com or fst_false_com == -1 ):
        return 1
    elif fst_false_com == -1:
        fst_len = len(pkg_pair[0])
        snd_len = len(pkg_pair[1])
        if fst_len < snd_len:
            return 1
        elif fst_len == snd_len: 
            return 0
        else:
            return -1
    else:
        return -1

fst_part_result = sum( idx +1 for idx,packet_pair in enumerate(packet_pairs) if comp_pkg_pair(packet_pair) == 1) 

print(f'{fst_part_result=}')

all_pkg = [packet_pair[idx] for packet_pair in packet_pairs for idx in range(2)]

divider_pkg_two = [[2]]
all_pkg.append(divider_pkg_two)
divider_pkg_six = [[6]]
all_pkg.append(divider_pkg_six)

all_pkg.sort(key= cmp_to_key(lambda fst, snd: comp_pkg_pair([fst,snd])), reverse=True)

idx_decoder_two = all_pkg.index(divider_pkg_two) +1
idx_decoder_six = all_pkg.index(divider_pkg_six) +1
print(f'snd part result {idx_decoder_two*idx_decoder_six}')
