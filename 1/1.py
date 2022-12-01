with open('1.txt') as fp:
    elves_list = list(map(lambda elve:
                          sum([int(cal) for cal in elve.split('\n')]), fp.read().rstrip().split('\n\n')))

print(f'solution for the first part {max(elves_list)}')

print(
    f'solution for the second part {sum(sorted(elves_list, reverse=True)[:3])}')
