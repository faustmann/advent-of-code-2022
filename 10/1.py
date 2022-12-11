from functools import reduce

with open('1.txt') as fp:
    commands = []
    for command_split in map(lambda line: line.split(' '), (fp.read().splitlines())):
        command = {}
        command['instruction'] = command_split[0]
        if len(command_split) == 2:
            commands.append({'instuction': 'proc_addx'})
            command['summand'] = int(command_split[1])

        commands.append(command)

executed_com_res = reduce(lambda acc, elem: acc + [
    {**elem, **{'sum': acc[-1]['sum'] + elem.get('summand', 0)}}], commands, [{'sum': 1}])

fst_part_result = sum(idx * executed_com_res[idx-1]['sum']
                      for idx in range(20, len(executed_com_res), 40))
print(f'{fst_part_result=}')

snd_part_result = ''
for idx, cur_exec_command in enumerate(executed_com_res):
    cursor_pos_x = idx % 40
    if cursor_pos_x == 0:
        snd_part_result += '\n'

    if abs(cursor_pos_x - cur_exec_command['sum']) <= 1:
        snd_part_result += '#'
    else:
        snd_part_result += '.'


print(snd_part_result)
print('fin')

