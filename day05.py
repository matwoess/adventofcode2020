from typing import NamedTuple

import aocd


class Seat(NamedTuple):
    row: int
    col: int

    def get_id(self):
        return self.row * 8 + self.col

    @classmethod
    def from_string(cls, partition_string: str) -> 'Seat':
        row_splits = partition_string[0:7]
        range_from = 0
        range_to = 128
        for s in row_splits:
            range_len = range_to - range_from
            if s == 'F':
                range_to -= range_len // 2
            elif s == 'B':
                range_from += range_len // 2
            else:
                raise ValueError('invalid partition character for rows')
        assert range_from == range_to - 1
        row = range_from
        column_splits = partition_string[7:10]
        range_from = 0
        range_to = 8
        for s in column_splits:
            range_len = range_to - range_from
            if s == 'L':
                range_to -= range_len // 2
            elif s == 'R':
                range_from += range_len // 2
            else:
                raise ValueError('invalid partition character for columns')
        assert range_from == range_to - 1
        col = range_from
        return Seat(row, col)


def part1(seats: list[Seat]) -> int:
    return max([s.get_id() for s in seats])


def part2(seats: list[Seat]) -> int:
    min_row = min([s.row for s in seats])
    max_row = max([s.row for s in seats])
    all_seats = {Seat(r, c) for c in range(8) for r in range(min_row + 1, max_row)}  # exclude first and last row
    my_seat = all_seats - set(seats)
    assert len(my_seat) == 1
    return list(my_seat)[0].get_id()


if __name__ == '__main__':
    day = 5
    data = aocd.get_data(day=day)
    split_data = data.splitlines()
    assigned_seats = [Seat.from_string(partition_string) for partition_string in split_data]
    answer1 = part1(assigned_seats)
    print('Answer1:', answer1)
    # aocd.submit(answer1, part='a', day=day)
    answer2 = part2(assigned_seats)
    print('Answer2:', answer2)
    # aocd.submit(answer1, part='a', day=day)
