from collections import namedtuple
import random

Part_Sol = namedtuple('Part_Sol', 'flow path')
Path_Elem = namedtuple('Path_Elem', 'valve opened')
Part_Soli = namedtuple('Part_Sol', 'flow pos opened')

def extract_valve_data(line):
    line_split = line.split(' ')
    id =  line_split[1]
    flow = int( line_split[4].split('=')[-1][:-1] )
    neighbours = [neigh[:2] for neigh in line_split[9:]]

    return {
        "id": id,
        "flow": flow,
        "neighbours": neighbours,
    }

with open('1.txt') as fp:
    valve_dat = {valve_dat['id']: valve_dat for valve_dat in [ extract_valve_data(line_split) for line_split in fp.read().splitlines() ]}

sorted_flows = sorted(valve_dat.values(), key=lambda v: v['flow'], reverse=True)

part_solution = Part_Sol(0,[Path_Elem('AA', False)])
def greedy_solution(part_sol, time):
    flow = part_sol.flow
    path = part_sol.path
    
    cur_pos = path[-1]
    if not cur_pos.opened and valve_dat[cur_pos.valve]['flow'] != 0:
        flow = flow + valve_dat[cur_pos.valve]['flow'] * (30-time)
        path = path[:-1] + [Path_Elem(cur_pos.valve, True)]
        return Part_Sol(flow, path)
    else:
        neighbours = [valve for valve in valve_dat[cur_pos.valve]['neighbours'] if not valve in [path_pos.valve for path_pos in path]]
        if not neighbours:
            path.append(Path_Elem(random.choice(valve_dat[cur_pos.valve]['neighbours']), True))
        else:
            max_valve = max(neighbours, key=lambda id: valve_dat[id]['flow'])
            path.append(Path_Elem(max_valve, False))
        return part_sol

for time_point in range(30):
    part_solution = greedy_solution(part_solution,time_point)
greedy_flow = part_solution.flow

def extend_part_sol(part_sol, time_point):
    new_part_sol = []

    flow = part_sol.flow
    cur_pos = part_sol.pos
    
    if not cur_pos in part_sol.opened and valve_dat[cur_pos]['flow'] != 0:
        new_flow = flow + valve_dat[cur_pos]['flow'] * (30-(time_point+1))
        opened = part_sol.opened.union(set([cur_pos]))
        new_part_sol.append( Part_Soli(new_flow, cur_pos, opened) )
    
    neighbours = [valve for valve in valve_dat[cur_pos]['neighbours']]
    for neighbour in neighbours:
        still_pos_flows = list(f['flow'] for f in sorted_flows if not f['id'] in part_sol.opened)
        if max(greedy_flow, part_solutions[0].flow) <= flow + sum((30-t) * f for f,t in zip(still_pos_flows, range(time_point+2,30,2))):
            new_part_sol.append(Part_Soli(flow, neighbour, part_sol.opened))
    return new_part_sol

part_solutions = [Part_Soli(0, 'AA', set())]
for time_point in range(30):
    new_part_solutions = []
    for part_solution in part_solutions:
        new_part_solutions.extend(extend_part_sol(part_solution, time_point))
    new_part_solutions.sort(key=lambda sol: sol.flow, reverse=True)

    part_solutions = []
    for new_part_solution in new_part_solutions:
        if not any(
            part_sol.pos == new_part_solution.pos 
            and (part_sol.opened == new_part_solution.opened or part_sol.opened.issubset(new_part_solution.opened))
         for part_sol in part_solutions):
            part_solutions.append(new_part_solution)
    print(f'{time_point=}, {len(part_solutions)} unfiltered {len(new_part_solutions)}')
    
print(f'fst part sol {part_solutions[0].flow}')
