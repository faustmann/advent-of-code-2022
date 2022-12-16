
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

line_of_interest = 2000000
line_beacons_or_senor = set(sen_data[dev_idx][0] for sen_data in sensors_data for dev_idx in [0,1] if sen_data[dev_idx][1] == line_of_interest)

sensors_remaining_x_range = list(filter(
    lambda sen_remaining_x_range: sen_remaining_x_range[1] > 0, 
    map(
        lambda sen_dat: (sen_dat[0][0], sen_dat[2] - abs(sen_dat[0][1] - line_of_interest)), 
        sensors_data
    )
))

occupied_x_pos = set(
    sen_rem_x_range[0] + (x_delta*dir) 
        for sen_rem_x_range in sensors_remaining_x_range 
        for x_delta in range(sen_rem_x_range[1]+1) 
        for dir in [-1,1]
)
occupied_x_pos = occupied_x_pos - line_beacons_or_senor

print(f'fst part solution {len(occupied_x_pos)}')
