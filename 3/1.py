
with open('1.txt') as fp:
    rucksacks = fp.read().splitlines()


def score_item(item): return ord(item) - \
    96 if item.islower() else ord(item) - 64 + 26


def rate_items_both_compartments(rucksack):
    com_length = len(rucksack) // 2
    items_both_compartments = set(rucksack[:com_length]).intersection(
        set(rucksack[com_length:]))
    return sum(score_item(item) for item in items_both_compartments)


part_one_result = sum(rate_items_both_compartments(rucksack)
                      for rucksack in rucksacks)

print(part_one_result)


part_two_result = sum(score_item(list(set(rucksacks[idx]) & set(
    rucksacks[idx+1]) & set(rucksacks[idx+2]))[0]) for idx in range(0, len(rucksacks), 3))

print(part_two_result)
