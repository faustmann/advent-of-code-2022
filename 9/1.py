
PRINT_TRACE = False

with open('1.txt') as fp:
    moves = [
        {
            "dir": move_splits[0],
            "steps": int(move_splits[1]),
        }
        for move_splits
        in map(lambda line: line.split(' '), (fp.read().splitlines()))
    ]


def sign(x): return x/abs(x) if x != 0 else 0


def next_head_pos(cur_head_pos, direction):
    dir_vector_dict = {
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1),
    }
    dir_vector = dir_vector_dict[direction]
    return (cur_head_pos[0] + dir_vector[0], cur_head_pos[1] + dir_vector[1])


def next_tail_pos(cur_tail_pos, new_head_pos):
    x_diff = new_head_pos[0] - cur_tail_pos[0]
    y_diff = new_head_pos[1] - cur_tail_pos[1]
    if abs(x_diff) <= 1 and abs(y_diff) <= 1:
        return cur_tail_pos
    else:
        return (cur_tail_pos[0]+sign(x_diff), cur_tail_pos[1]+sign(y_diff))


tail_pos = (0, 0)
head_pos = (0, 0)
tail_visited = set([tail_pos])
for move in moves:
    for step in range(move['steps']):
        head_pos = next_head_pos(head_pos, move['dir'])
        tail_pos = next_tail_pos(tail_pos, head_pos)
        tail_visited.add(tail_pos)

        if PRINT_TRACE:
            lines = []
            for l_idx in range(75):
                p_line = ''
                for c_idx in range(75):
                    if (c_idx, l_idx) == head_pos:
                        p_line = p_line + 'H'
                    elif (c_idx, l_idx) == tail_pos:
                        p_line = p_line + 'T'
                    else:
                        p_line = p_line + ('#' if (c_idx, l_idx)
                                           in tail_visited else '.')

                lines.append(p_line)
            print('\n'.join(reversed(lines)))

print(f'fst part result {len(tail_visited)}')

knot_posis = [(0, 0)]*10
tail_visited = set([knot_posis[-1]])
for move in moves:
    for step in range(move['steps']):
        for idx in range(len(knot_posis)):
            if idx == 0:
                knot_posis[idx] = next_head_pos(knot_posis[idx], move['dir'])
            else:
                knot_posis[idx] = next_tail_pos(
                    knot_posis[idx], knot_posis[idx-1])
        tail_visited.add(knot_posis[-1])

print(f'snd part result {len(tail_visited)}')
print(f'fin')
