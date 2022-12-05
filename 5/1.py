
part_one = False
with open("1.txt") as fp:
    lines = fp.read()

stacks, moves = lines.split('\n\n')
moves = [{"num_moves": int(line_parts[1]),
            "from": int(line_parts[-3]) -1,
            "to": int(line_parts[-1]) -1
            } 
            for line_parts 
            in map(lambda line: line.split(' '), moves.split('\n'))
            ]

stacks_lines = list(reversed(stacks.splitlines()[:-1]))
num_stacks = int(stacks.splitlines()[-1].split(' ')[-2])

stacks_list = [[] for idx in range(num_stacks)]
for stack_num in range(num_stacks):
    for stacks_line in stacks_lines:
        sign = stacks_line[1+4*stack_num]
        if sign != ' ':
            stacks_list[stack_num].append(sign)

for move in moves:
    if part_one:
        for move_num in range(move['num_moves']):
            stacks_list[move['to']].append(stacks_list[move['from']].pop())
    else:
        slice = stacks_list[move['from']][-move['num_moves']:]
        del stacks_list[move['from']][-move['num_moves']:]
        stacks_list[move['to']].extend(slice)

print(f'result {"".join([stack[-1] for stack in stacks_list])}')
