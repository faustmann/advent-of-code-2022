import sys
import heapq
from collections import namedtuple


Point = namedtuple("Point", "x y")


with open('1.txt') as fp:
    grid = list(map(list, fp.read().splitlines()))

x_len = len(grid)
y_len = len(grid[0])
start_positions = [Point(x,y) for x in range(x_len) for y in range(y_len ) if grid[x][y] == 'S' or grid[x][y] == 'a']
end_pos = Point(*next((x,y) for x in range(x_len) for y in range(y_len) if grid[x][y] == 'E'))

route_lengths = []
for idx, start_pos in enumerate(start_positions):
    print(f'try start pos idx {idx}/{len(start_positions)}')
    openlist = []
    heapq.heappush(openlist, (0, start_pos))
    min_cost_map = [[(sys.maxsize, None) for y in range(y_len)] for x in range(x_len)]
    min_cost_map[start_pos.x][start_pos.y] = (0, None)


    def heuristic_manhattan_dist(pos):
        x, y = pos
        return (end_pos.x - x) + (end_pos.y - y)

    def get_height(pos):
        x, y = pos
        raw_height_char = grid[x][y]
        if raw_height_char == 'S':
            raw_height_char = 'a'
        if raw_height_char == 'E':
            raw_height_char = 'z'
        
        return ord(raw_height_char) - ord('a')

    def expand_pos(cur_pos):
        x, y = cur_pos
        two_d_offsets = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

        for x_off, y_off in two_d_offsets:
            new_pos = Point(x + x_off, y + y_off)
            if 0 <= new_pos.x < x_len and 0 <= new_pos.y < y_len:
                if get_height(new_pos) - get_height(cur_pos) > 1 or new_pos == start_pos:
                    continue

                new_part_cost = min_cost_map[x][y][0] + 1

                new_pos_elem_in_openlist = next(
                    (elem for elem in openlist if elem[1] == new_pos), None
                )

                if new_pos_elem_in_openlist != None or \
                    new_part_cost >= min_cost_map[new_pos.x][new_pos.y][0]:
                    continue

                min_cost_map[new_pos.x][new_pos.y] = (new_part_cost, cur_pos)

                if new_pos == end_pos:
                    return False

                heapq.heappush(
                    openlist, (new_part_cost + heuristic_manhattan_dist(new_pos), new_pos)
                )

        return True


    while len(openlist) > 0:
        _, current_pos = heapq.heappop(openlist)
        if not expand_pos(current_pos):
            route_lengths.append(min_cost_map[end_pos.x][end_pos.y][0])
            break

print(f"min route cost {min(route_lengths)}")
