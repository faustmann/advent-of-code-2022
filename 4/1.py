
with open('1.txt') as fp:
    assignments = [tuple(map(lambda a: list(map(int, a.split(
        '-'))), ass)) for ass in map(lambda ass_line: ass_line.split(','), fp.read().splitlines())]


def fully_contained(assignment_pair):
    fst, snd = assignment_pair
    start_diff = fst[0] - snd[0]
    start_contained = (start_diff) / (abs(start_diff)
                                      ) if start_diff != 0 else 0
    end_diff = snd[1] - fst[1]
    end_contained = (end_diff) / (abs(end_diff)) if end_diff != 0 else 0
    result = 1 if start_contained == end_contained or start_contained == 0 or end_contained == 0 else 0
    return result


fst_result = sum(fully_contained(ass) for ass in assignments)
print(f'first part result {fst_result=}')


def overlap(assignment_pair):
    fst, snd = assignment_pair
    fst_overlap_diff = fst[1] - snd[0]
    fst_overlap = (fst_overlap_diff) // (abs(fst_overlap_diff)
                                         ) if fst_overlap_diff != 0 else 0
    snd_overlap_diff = snd[1] - fst[0]
    snd_overlap = (snd_overlap_diff) // (abs(snd_overlap_diff)
                                         ) if snd_overlap_diff != 0 else 0

    return min(1, fst_overlap + snd_overlap + (1 if fst_overlap == 0 or snd_overlap == 0 else 0))


snd_result = sum(overlap(ass) for ass in assignments)
print(f'second part result {snd_result=}')
