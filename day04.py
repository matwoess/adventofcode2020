import aocd
from typing import List
import re


class Passport:
    required_keys: list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # , 'cid']
    kv_pattern: str = r'(\w+):([#\w]+)'
    conditions = {
        'byr': lambda byr: 1920 <= int(byr) <= 2002,
        'iyr': lambda iyr: 2010 <= int(iyr) <= 2020,
        'eyr': lambda eyr: 2020 <= int(eyr) <= 2030,
        'hgt': lambda hgt: Passport.height_valid(hgt),
        'hcl': lambda hcl: re.match(r'#[0-9a-f]{6}$', hcl),
        'ecl': lambda ecl: re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', ecl),
        'pid': lambda pid: re.match(r'\d{9}$', pid),
        'cid': lambda cid: True,
    }

    @classmethod
    def height_valid(cls, height: str) -> bool:
        if m := re.match(r'^(\d{3})cm$', height):
            return 150 <= int(m.group(1)) <= 193
        elif m := re.match(r'^(\d{2})in$', height):
            return 59 <= int(m.group(1)) <= 76
        else:
            return False

    def __init__(self, string: str):
        kv_pairs = re.findall(Passport.kv_pattern, string)
        self.values = {k: v for k, v in kv_pairs}

    def has_all_ish_keys(self) -> bool:
        return all(k in self.values.keys() for k in Passport.required_keys)

    def all_values_valid(self) -> bool:
        for key, value in self.values.items():
            if not Passport.conditions[key](value):
                return False
        return True


def part1(passports: List[Passport]) -> int:
    return sum(p.has_all_ish_keys() for p in passports)


def part2(passports: List[Passport]) -> int:
    complete_passports = [p for p in passports if p.has_all_ish_keys()]
    return sum(p.all_values_valid() for p in complete_passports)


if __name__ == '__main__':
    day = 4
    data = aocd.get_data(day=day)
    split_data = data.split('\n\n')
    all_passports = [Passport(d) for d in split_data]
    answer1 = part1(all_passports)
    print('Answer1:', answer1)
    answer2 = part2(all_passports)
    print('Answer2:', answer2)
