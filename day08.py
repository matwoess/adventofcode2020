import re
from typing import NamedTuple

import aocd


class Instruction(NamedTuple):
    inst: str
    arg: int

    @classmethod
    def from_string(cls, string: str) -> 'Instruction':
        pattern = r'(jmp|acc|nop) (\+\d+|-\d+)'
        match = re.match(pattern, string)
        return Instruction(match.group(1), int(match.group(2)))


def part1(instructions: list[Instruction]) -> int:
    executed = set()
    accumulator = pc = 0
    while pc not in executed:
        executed.add(pc)
        instruction = instructions[pc]
        if instruction.inst == 'jmp':
            pc += instruction.arg
        else:  # to_execute.inst in ['nop', 'acc']:
            if instruction.inst == 'acc':
                accumulator += instruction.arg
            pc += 1
    return accumulator


def part2(instructions: list[Instruction]) -> int:
    executed = set()
    accumulator = 0
    pc = 0
    code_len = len(instructions)
    for index, inst in enumerate(instructions):
        if inst.inst == 'acc':
            continue
        backup = inst
        if inst.inst == 'jmp':
            instructions[index] = Instruction('nop', inst.arg)
        elif inst.inst == 'nop':
            instructions[index] = Instruction('jmp', inst.arg)
        while pc not in executed and pc < code_len:
            executed.add(pc)
            instruction = instructions[pc]
            if instruction.inst == 'jmp':
                pc += instruction.arg
            else:  # to_execute.inst in ['nop', 'acc']:
                if instruction.inst == 'acc':
                    accumulator += instruction.arg
                pc += 1
        if pc >= code_len:
            return accumulator
        else:
            # reset values
            executed = set()
            accumulator = 0
            pc = 0
            # change instruction back for next iteration
            instructions[index] = backup
    return -1


if __name__ == '__main__':
    day = 8
    data = aocd.get_data(day=day)
    split_data = data.splitlines()
    all_instructions = [Instruction.from_string(s) for s in split_data]
    answer1 = part1(all_instructions)
    print('Answer1:', answer1)
    answer2 = part2(all_instructions)
    print('Answer2:', answer2)
