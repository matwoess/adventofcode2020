from functools import reduce

import aocd


def part1(groups: list[str]) -> int:
    inter_group_sets = [set(group.replace('\n', '')) for group in groups]
    return sum([len(group_set) for group_set in inter_group_sets])


def part2(groups: list[str]) -> int:
    total = 0
    for group in groups:
        group_sets = [set(s) for s in group.splitlines()]
        unanimous_set = reduce(lambda a, b: a & b, group_sets)
        total += len(unanimous_set)
    return total


if __name__ == '__main__':
    day = 6
    data = aocd.get_data(day=day)
    split_data = data.split('\n\n')
    answer1 = part1(split_data)
    print('Answer1:', answer1)
    # aocd.submit(answer1, part='a', day=day)
    answer2 = part2(split_data)
    print('Answer2:', answer2)
    # aocd.submit(answer1, part='a', day=day)
