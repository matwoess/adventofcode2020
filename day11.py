import aocd
import numpy as np


def print_occupancy(seats, floor):
    arr = np.where(seats == 1, '#', 'L')
    arr[floor] = '.'
    for row in arr:
        print(''.join(row))
    print()


def get_next_state(occupied: np.ndarray, floor: np.ndarray) -> np.ndarray:
    neighbors = np.zeros(shape=occupied.shape, dtype=np.int)
    neighbors[1:] += occupied[:-1]  # propagate down
    neighbors[:-1] += occupied[1:]  # propagate up
    neighbors[:, 1:] += occupied[:, :-1]  # propagate right
    neighbors[:, :-1] += occupied[:, 1:]  # propagate left
    neighbors[1:, 1:] += occupied[:-1, :-1]  # propagate down-right
    neighbors[1:, :-1] += occupied[:-1, 1:]  # propagate down-left
    neighbors[:-1, :-1] += occupied[1:, 1:]  # propagate up-left
    neighbors[:-1, 1:] += occupied[1:, :-1]  # propagate up-right

    new_state = occupied == 1
    new_occupied = neighbors == 0
    new_free = neighbors >= 4
    new_state &= ~new_free
    new_state |= new_occupied
    new_state &= ~floor
    return np.where(new_state, 1, 0)


def part1(state: np.ndarray) -> int:
    floor = state == '.'
    occupied = np.where(state == '#', 1, 0)
    # print_occupancy(seats, floor)
    prev = np.empty(shape=occupied.shape)
    while np.any(occupied != prev):
        prev = occupied
        occupied = get_next_state(occupied, floor)
        # print_occupancy(seats, floor)
    return sum(occupied.ravel())


def get_next_state_line_of_sight(occupied: np.ndarray, seats: np.ndarray, floor: np.ndarray) -> np.ndarray:
    shape = occupied.shape
    neighbors = np.zeros(shape=shape, dtype=np.int)
    max_len = max(shape)
    all_directions = {(1, 0), (-1, 0), (0, -1), (0, 1),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)}

    def check_direction(r, c, dw, rw):
        for i in range(1, max_len):
            x = r + i * dw
            y = c + i * rw
            if not (0 <= x < shape[0] and 0 <= y < shape[1]):
                return 0
            if occupied[x, y] == 1:
                return 1
            if seats[x, y]:
                return 0
        return 0

    for row in range(shape[0]):
        for col in range(shape[1]):
            if floor[row, col]:
                continue
            visible_neighbors = 0
            for downward, rightward in all_directions:
                visible_neighbors += check_direction(row, col, downward, rightward)
            neighbors[row, col] = visible_neighbors

    new_state = occupied == 1
    new_occupied = neighbors == 0
    new_free = neighbors >= 5
    new_state &= ~new_free
    new_state |= new_occupied
    new_state &= ~floor
    return np.where(new_state, 1, 0)


def part2(state: np.ndarray) -> int:
    floor = state == '.'
    seats = state == 'L'
    occupied = np.where(state == '#', 1, 0)
    # print_occupancy(seats, floor)
    prev = np.empty(shape=occupied.shape)
    while np.any(occupied != prev):
        prev = occupied
        occupied = get_next_state_line_of_sight(occupied, seats, floor)
        # print_occupancy(occupied, floor)
    return sum(occupied.ravel())


if __name__ == '__main__':
    day = 11
    data = aocd.get_data(day=day)
    split_data = data.splitlines()
    initial_layout = np.array([list(line) for line in split_data])
    answer1 = part1(initial_layout)
    print('Answer1:', answer1)  # 2152
    answer2 = part2(initial_layout)
    print('Answer2:', answer2)  # 1937
