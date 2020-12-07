import re

import aocd


class Bag:
    bag_pattern = r'^(\w+ \w+) bags contain (.*)'
    content_pattern = r'(?:(\d+) (\w+ \w+) bags?(?:, )?)'

    def __init__(self, bag_specification):
        match = re.match(Bag.bag_pattern, bag_specification)
        self.bag_name = match.group(1)
        content_string = match.group(2)
        self.contents = {name: int(count) for count, name in re.findall(Bag.content_pattern, content_string)}


def part1(bags: list[Bag]) -> int:
    all_bags_map = {b.bag_name: b for b in bags}

    def contains_shiny_gold(bag: Bag) -> bool:
        if not bag.contents:
            return False
        if 'shiny gold' in bag.contents:
            return True
        return any(contains_shiny_gold(all_bags_map[k]) for k in bag.contents.keys())

    return sum(contains_shiny_gold(b) for b in bags)


def part2(bags: list[Bag]) -> int:
    all_bags_map = {b.bag_name: b for b in bags}

    def count_contents(bag: Bag) -> int:
        if not bag.contents:
            return 0
        current_content = sum(bag.contents.values())
        child_contents = 0
        for c, n in bag.contents.items():
            sub_bag = all_bags_map[c]
            child_contents += n * count_contents(sub_bag)
        return current_content + child_contents

    return count_contents(all_bags_map['shiny gold'])


if __name__ == '__main__':
    day = 7
    data = aocd.get_data(day=day)
    split_data = data.splitlines()
    all_bags = [Bag(spec) for spec in split_data]
    answer1 = part1(all_bags)
    print('Answer1:', answer1)
    answer2 = part2(all_bags)
    print('Answer2:', answer2)
