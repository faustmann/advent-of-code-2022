
with open('1.txt') as fp:
    rock_paths = list(map(lambda line: list(map(lambda coord_str: tuple(map(int,coord_str.split(','))), line.split(' -> '))), fp.read().splitlines()))


min_x = min(pos[0] for path in rock_paths for pos in path)
max_x = max(pos[0] for path in rock_paths for pos in path)
min_y = 0
max_y = max(pos[1] for path in rock_paths for pos in path)

cave = [['.' for y in range(max_x-min_x+1)] for x in range(max_y-min_y+1)]

def cave_pos_to_array_pos(c_pos):
    return c_pos[0]-min_x, c_pos[1]-min_y

def stuf_at(c_pos):
    x, y = cave_pos_to_array_pos(c_pos)
    return cave[y][x]

for rock_path in rock_paths:
    for idx in range(1, len(rock_path)):
        prev_keypoint = rock_path[idx-1]
        cur_keypoint = rock_path[idx]
        x_step = 1 if prev_keypoint[0] <= cur_keypoint[0] else -1
        y_step = 1 if prev_keypoint[1] <= cur_keypoint[1] else -1
        rock_points = [(c_x, c_y) for c_x in range(prev_keypoint[0], cur_keypoint[0] +x_step, x_step) for c_y in range(prev_keypoint[1], cur_keypoint[1] +y_step, y_step)]
        for r_pos in rock_points:
            a_x, a_y = cave_pos_to_array_pos(r_pos)
            cave[a_y][a_x] = '#'

def get_stone_end_a_pos(drop_a_pos):
    y_fundament_base = next((y for y in range(drop_a_pos[1], len(cave)) if cave[y][drop_a_pos[0]] != '.'), None)
    if y_fundament_base is None:
        return None
    fundament_base = (drop_a_pos[0], y_fundament_base)
    fundament = [cave[fundament_base[1]][fundament_base[0] + delta_x] for delta_x in [-1,1]]

    if all(fund_elem != '.' for fund_elem in fundament):
        return fundament_base[0], fundament_base[1]-1

    if cave[fundament_base[1]][fundament_base[0] -1] == '.':
        return get_stone_end_a_pos((fundament_base[0]-1, fundament_base[1] ))
    elif cave[fundament_base[1]][fundament_base[0] +1] == '.':
        return get_stone_end_a_pos((fundament_base[0]+1, fundament_base[1] ))

sand_a_source = cave_pos_to_array_pos((500,0))

num_sands = 0
while True:
    end_pos = get_stone_end_a_pos(sand_a_source)
    if end_pos is None:
        break
    num_sands += 1
    cave[end_pos[1]][end_pos[0]] = 'o'

print(f'fst part sol: {num_sands=}')