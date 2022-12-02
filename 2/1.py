
with open('1.txt') as fp:
    rounds = list(map(lambda round: round.rstrip().split(' '), fp.readlines()))

score_my_move = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

win_counter_action = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}

lose_counter_action = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
}


def score_round(round):
    if win_counter_action[round[0]] == round[1]:
        return 6

    if ord(round[0]) - ord(round[1]) == -23:
        return 3

    return 0


part_one_result = sum(score_my_move[round[1]] + score_round(round)
                      for round
                      in rounds
                      )

print(f'first part {part_one_result=}')


def score_strategy(round):
    map_strategy = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }

    strat_points = map_strategy[round[1]]
    my_move_points = 0
    if strat_points == 0:
        my_move_points = score_my_move[lose_counter_action[round[0]]]

    if strat_points == 3:
        my_move_points = score_my_move[chr(ord(round[0]) + 23)]

    if strat_points == 6:
        my_move_points = score_my_move[win_counter_action[round[0]]]

    return strat_points + my_move_points


part_two_result = sum(score_strategy(round)
                      for round
                      in rounds
                      )

print(f'second part {part_two_result=}')
