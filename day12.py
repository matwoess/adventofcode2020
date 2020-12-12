from typing import List, NamedTuple

import aocd


class Instruction(NamedTuple):
    act: str
    val: int

    @classmethod
    def from_string(cls, init_string: str) -> 'Instruction':
        return Instruction(init_string[0], int(init_string[1:]))


directions = {
    'N': 0 + 1j,
    'S': 0 - 1j,
    'W': -1 + 0j,
    'E': 1 + 0j
}


def part1(instructions: List[Instruction]) -> int:
    curr_position = 0 + 0j
    curr_direction = directions['E']
    for inst in instructions:
        if inst.act == 'F':
            curr_position += curr_direction * inst.val
        elif inst.act == 'L':
            for i in range(inst.val // 90):
                curr_direction *= 1j
        elif inst.act == 'R':
            for i in range(inst.val // 90):
                curr_direction *= -1j
        else:
            curr_position += directions[inst.act] * inst.val

    return int(abs(curr_position.real) + abs(curr_position.imag))


def part2(instructions: List[Instruction]) -> int:
    curr_position = 0 + 0j
    waypoint_offset = 10 + 1j
    for inst in instructions:
        if inst.act == 'F':
            curr_position += waypoint_offset * inst.val
        elif inst.act == 'L':
            for i in range(inst.val // 90):
                waypoint_offset *= 1j
        elif inst.act == 'R':
            for i in range(inst.val // 90):
                waypoint_offset *= -1j
        else:
            waypoint_offset += directions[inst.act] * inst.val

    return int(abs(curr_position.real) + abs(curr_position.imag))


if __name__ == '__main__':
    day = 12
    data = aocd.get_data(day=day)
    all_instructions = [Instruction.from_string(string) for string in data.splitlines()]
    answer1 = part1(all_instructions)
    print('Answer1:', answer1)  # 364
    answer2 = part2(all_instructions)
    print('Answer2:', answer2)  # 39518
