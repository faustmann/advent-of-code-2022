from functools import reduce

CALC_FST_PART = False

with open('1.txt') as fp:
    monkey_str_list = fp.read().split('\n\n')


def create_calc(fst, op, snd):
    if calc_parts[1] == '*':
        return lambda old: (int(fst) if fst.isnumeric(
        ) else old) * (int(snd) if snd.isnumeric() else old)
    else:
        return lambda old: (int(fst) if fst.isnumeric(
        ) else old) + (int(snd) if snd.isnumeric() else old)


monkeys = []
for monkey_str in monkey_str_list:
    monkey = {'inspected_items': 0}
    monkeys.append(monkey)
    for line_idx, monkey_line in enumerate(monkey_str.split('\n')):
        if line_idx == 1:
            monkey['items'] = [
                int(item) for item in monkey_line.split(': ')[-1].split(', ')]
        if line_idx == 2:
            calc_parts = monkey_line.split(' = ')[-1].split(' ')
            monkey['calc'] = create_calc(*calc_parts)
        if line_idx == 3:
            monkey['div_test_number'] = int(monkey_line.split(' ')[-1])
        if line_idx == 4:
            monkey['test_true_monkey'] = int(monkey_line.split(' ')[-1])
        if line_idx == 5:
            monkey['test_false_monkey'] = int(monkey_line.split(' ')[-1])

if CALC_FST_PART:
    for round_num in range(20):
        for monkey in monkeys:
            monkey['inspected_items'] += len(monkey['items'])
            while len(monkey['items']) != 0:
                item = monkey['items'].pop(0)
                item = monkey['calc'](item) // 3
                if item % monkey['div_test_number'] == 0:
                    itemToMonkey = monkey['test_true_monkey']
                else:
                    itemToMonkey = monkey['test_false_monkey']
                monkeys[itemToMonkey]['items'].append(item)

    sorted_monkeys = sorted(
        monkeys, key=lambda monkey: monkey['inspected_items'], reverse=True)

    print(
        f"fst past result {sorted_monkeys[0]['inspected_items'] * sorted_monkeys[1]['inspected_items']}")
else:
    for round_num in range(10000):
        print(f'round {round_num}')
        for monkey in monkeys:
            monkey['inspected_items'] += len(monkey['items'])
            while len(monkey['items']) != 0:
                item = monkey['items'].pop(0)
                item = monkey['calc'](item)
                if item % monkey['div_test_number'] == 0:
                    itemToMonkey = monkey['test_true_monkey']
                else:
                    itemToMonkey = monkey['test_false_monkey']
                monkeys[itemToMonkey]['items'].append(item)

    sorted_monkeys = sorted(
        monkeys, key=lambda monkey: monkey['inspected_items'], reverse=True)

    print(
        f"snd past result {sorted_monkeys[0]['inspected_items'] * sorted_monkeys[1]['inspected_items']}")

print('fin')
