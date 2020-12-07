from typing import Iterator

import aocd
import re


def extractor(lines) -> Iterator[tuple[int, int, str, str]]:
    pattern = r'(\d+)-(\d+)\s(\w):\s(\w+)'
    for row in lines:
        match = re.match(pattern, row)
        if not match:
            # yield -1, -1, '', ''
            continue
        groups = match.groups()
        a, b, ch, pw = int(groups[0]), int(groups[1]), groups[2], groups[3]
        yield a, b, ch, pw


def part1(lines: list) -> int:
    return sum([(a <= pw.count(ch) <= b) for a, b, ch, pw in extractor(lines)])


def part2(lines: list) -> int:
    return sum([(pw[a - 1] == ch) != (pw[b - 1] == ch) for a, b, ch, pw in extractor(lines)])


if __name__ == '__main__':
    day = 2
    data = aocd.get_data(day=day)
    split_data = data.splitlines()
    answer1 = part1(split_data)
    print('Answer1:', answer1)
    answer2 = part2(split_data)
    print('Answer2:', answer2)
