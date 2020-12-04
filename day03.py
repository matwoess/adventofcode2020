from typing import Iterator, NamedTuple

import aocd
import numpy as np
import math


class Slope(NamedTuple):
    right: int
    down: int


def ride(trees: np.ndarray, slope: Slope) -> Iterator[bool]:
    right = down = 0
    height, width = trees.shape
    while down < height - 1:
        down += slope.down
        right += slope.right
        right = right % width  # repeat pattern
        yield trees[down, right]
    return False  # out of bounds, no tree


def part1(trees: np.ndarray, slope=Slope(right=3, down=1)) -> int:
    return sum(tile for tile in ride(trees, slope))


def part2(trees: np.ndarray) -> int:
    slopes = [Slope(1, 1), Slope(3, 1), Slope(5, 1), Slope(7, 1), Slope(1, 2)]
    return math.prod([part1(trees, slope) for slope in slopes])


if __name__ == '__main__':
    day = 3
    data = aocd.get_data(day=day)
    split_data = data.splitlines()
    char_array = np.array([list(line) for line in split_data])
    tree_array = char_array == '#'
    answer1 = part1(tree_array)
    print('Answer1:', answer1)
    # aocd.submit(answer1, part='a', day=day)
    answer2 = part2(tree_array)
    print('Answer2:', answer2)
    # aocd.submit(answer2, part='b', day=day)
