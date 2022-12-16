
def extract_sen_data(line):
    line_split = line.split(' ')
    sen_x = int( line_split[2][:-1].split('=')[-1] )
    sen_y = int( line_split[3][:-1].split('=')[-1] )
    beacon_x = int( line_split[8][:-1].split('=')[-1] )
    beacon_y = int( line_split[9].split('=')[-1] )

    man_dist = abs(sen_x-beacon_x) + abs(sen_y-beacon_y)

    return (sen_x, sen_y), (beacon_x, beacon_y), man_dist

with open('1.txt') as fp:
    sensors_data = [extract_sen_data(line_split) for line_split in fp.read().splitlines()]

coord_range = 4000000
for line_of_interest in range(coord_range +1):
    line_beacons_or_senor = set(sen_data[dev_idx][0] for sen_data in sensors_data for dev_idx in [0,1] if sen_data[dev_idx][1] == line_of_interest)

    sensors_remaining_x_range = list(filter(
        lambda sen_remaining_x_range: sen_remaining_x_range[1] > 0, 
        map(
            lambda sen_dat: (sen_dat[0][0], sen_dat[2] - abs(sen_dat[0][1] - line_of_interest)), 
            sensors_data
        )
    ))

    x_intervals = list(
        [sen_rem_x_range[0] - sen_rem_x_range[1], sen_rem_x_range[0] + sen_rem_x_range[1] ]
            for sen_rem_x_range in sensors_remaining_x_range 
            for dir in [-1,1]
    )

    x_intervals.sort(key=lambda interval: interval[0])
    merged = [x_intervals[0]]
    for current in x_intervals:
        previous = merged[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)

    if not any(interval[0] <= 0 and coord_range <= interval[1] for interval in merged):
        print('check me')
    
    if line_of_interest % 10000 == 0:
        print(f'{line_of_interest=}/{coord_range}')
