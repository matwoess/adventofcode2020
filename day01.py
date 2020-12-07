import aocd


def part1(exp: list[int]) -> int:
    for e1 in exp:
        for e2 in exp:
            if e1 + e2 == 2020:
                return e1 * e2


def part2(exp: list[int]) -> int:
    thresh = 2020 - min(exp)
    for e1 in exp:
        for e2 in exp:
            if (e := e1 + e2) > thresh:
                continue
            for e3 in exp:
                if e + e3 == 2020:
                    return e1 * e2 * e3


if __name__ == '__main__':
    day = 1
    data = aocd.get_data(day=day)
    split_data = [int(line) for line in data.splitlines()]
    answer1 = part1(split_data)
    print('Answer1:', answer1)
    answer2 = part2(split_data)
    print('Answer2:', answer2)
