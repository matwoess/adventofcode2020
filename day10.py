from collections import defaultdict
from typing import List

import aocd


def part1(adapters: List[int]) -> int:
    device_jolts = max(adapters) + 3
    adapters.append(device_jolts)
    prev = 0
    diff1 = diff3 = 0

    for adapter in adapters:
        diff = adapter - prev
        if diff == 1:
            diff1 += 1
        elif diff == 3:
            diff3 += 1
        prev = adapter
    return diff1 * diff3


def part2(adapters: List[int]) -> int:
    adapters.insert(0, 0)
    device_jolts = max(adapters) + 3
    adapters.append(device_jolts)
    # store amount of possible paths till device by list index
    paths_at_index = dict()
    list_len = len(adapters)
    # pre-last index has only one possible variant to reach last element
    paths_at_index[list_len - 2] = 1

    # starting from the end, sum up possible variants to reach the last element
    # re-use previously calculated values in the `paths_at_index` dict
    for index in reversed(range(list_len - 2)):
        curr_adapter = adapters[index]
        sum_paths = 0
        # check next 3 list indices (only next 3 can have a difference <= 3)
        for dist in range(1, 4):
            if (i := index + dist) < list_len and adapters[i] - curr_adapter <= 3:
                sum_paths += paths_at_index[i]
        paths_at_index[index] = sum_paths

    # return all possible paths from list index 0
    return paths_at_index[0]


if __name__ == '__main__':
    day = 10
    data = aocd.get_data(day=day)
    split_data = list(sorted(map(int, data.splitlines())))
    answer1 = part1(split_data)
    print('Answer1:', answer1)
    answer2 = part2(split_data)
    print('Answer2:', answer2)
