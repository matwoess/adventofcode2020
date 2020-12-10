from itertools import permutations
from typing import List

import aocd


def part1(sequence: List[int], preamble_len: int = 25) -> int:
    preamble = sequence[:preamble_len]
    index = preamble_len
    for i, num in zip(range(index, len(sequence)), sequence[index:]):
        valid = any(p1 + p2 == num for p1, p2 in permutations(preamble, 2))
        if not valid:
            return num
        del preamble[0]
        preamble.append(num)
    return -1


def subsequences(seq: List[int], min_len: int = 2):
    for i in range(0, len(seq)):
        for j in range(min_len, len(seq) - i + 1):
            yield seq[i:i + j]


def part2(sequence: List[int], number: int = 133015568) -> int:
    to_index = sequence.index(number)
    subseq = sequence[:to_index]
    for seq in subsequences(subseq, min_len=2):
        valid = sum(seq) == number
        if valid:
            # print(min(seq), max(seq))
            return min(seq) + max(seq)
    return -1


if __name__ == '__main__':
    day = 9
    data = aocd.get_data(day=day)
    split_data = list(map(int, data.splitlines()))
    answer1 = part1(split_data)
    print('Answer1:', answer1)
    answer2 = part2(split_data)
    print('Answer2:', answer2)
