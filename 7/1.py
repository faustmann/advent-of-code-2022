with open('1.txt') as fp:
    log = fp.read()

commands = [{'command': command_part[0].strip().split(' '), 'output': list(map(lambda output_line: output_line.split(' '), command_part[1:]))}
            for command_part in map(lambda command_part: command_part.strip().split('\n'), log.split('$')[1:])]

'''
node struct for path tree
{
    'parent': ...,
    'name': 'xxx',
    'size': xxx,
    'children': [...],
}
'''
root_elem = {
    'parent': None,
    'name': '/',
    'children': []
}


def process_ls_output(output, path_elem):
    result = []
    for output_line in output:
        if output_line[0] == 'dir':
            elem = {
                'parent': path_elem,
                'name': output_line[1],
                'children': [],
            }
        else:
            elem = {
                'parent': path_elem,
                'name': output_line[1],
                'size': int(output_line[0]),
            }
        result.append(elem)
    return result


def process_command(command_obj, path_elem):
    command = command_obj["command"]
    if command[0] == 'cd':
        if command[1] == '/':
            return root_elem
        elif command[1] == '..':
            return path_elem['parent']
        else:
            return next(elem for elem in path_elem['children'] if elem['name'] == command[1] and not 'size' in elem)
    elif command[0] == 'ls':
        path_elem['children'] = process_ls_output(
            command_obj["output"], path_elem)
        return path_elem


cur_path = None
for command in commands:
    cur_path = process_command(command, cur_path)

dir_size_list = []


def calc_size(cur_node):
    global dir_size_list
    if 'size' in cur_node:
        return cur_node['size']
    else:
        dir_size = sum(calc_size(node) for node in cur_node['children'])
        dir_size_list.append(dir_size)
        return dir_size


calc_size(root_elem)

print(
    f'sum small dir size {sum(size for size in dir_size_list if size < 100000)}')


free_space = 70000000 - calc_size(root_elem) - 30000000

if free_space < 0:
    del_me_size = next(size for size in sorted(
        dir_size_list) if size > abs(free_space))
    print(f'{del_me_size=}')

print('fin')
