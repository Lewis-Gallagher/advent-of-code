"""
Solution for Advent of Code 2022 day 11 - https://adventofcode.com/2022/day/11
Lewis Gallagher - lewis.gallagher@icr.ac.uk
"""

import os
from typing import List, Any
import timeit
from collections import deque
from dataclasses import dataclass
import re
from math import trunc, prod


EXAMPLE_INPUT = '''\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''

EXAMPLE_OUTPUT_PART1 = 10605
EXAMPLE_OUTPUT_PART2 = 0

@dataclass
class Monkey:
    num: int
    current_items: deque
    operation: str
    test: bool
    true_idx: int
    false_idx: int
    inspected_count: int

    def from_data(monkey: List[str]):

        # monkey_dict = dict()
        
        # Find monkey properties.
        monkey_number = re.findall(r"^\s*Monkey (\d)", monkey[0])[0]
        starting_items = re.findall(r"^\s*Starting items: (\d+.*)", monkey[1])
        operation = re.findall(r"^\s*Operation: new = old ([+*] .+)", monkey[2])
        test_if = re.findall(r"^\s*Test: divisible by (\d*)", monkey[3])[0]
        test_true_throw = re.findall(r"^\s*If true: throw to monkey (\d*)", monkey[4])[0]
        test_false_throw = re.findall(r"^\s*If false: throw to monkey (\d*)", monkey[5])[0]

        # Turn starting items into list of ints.
        starting_items = [int(item) for item in ' '.join(starting_items).split(', ')]
        operation = [op for op in ' '.join(operation).split(' ')]

        return Monkey(
            num = int(monkey_number),
            current_items = deque(starting_items),
            operation = operation,
            test = int(test_if),
            true_idx = int(test_true_throw),
            false_idx = int(test_false_throw),
            inspected_count = 0
        )

def inspect_item(list_of_monkeys: List[Monkey], part_2: bool):
    """Accepts a list of monkeys and loops over each of their items. Alter's the item's worry value by an operation and passes the item to another monkey based on the output of a modulo expression. The item is removed from the original monkey's item list and added to the new monkey's item list."""

    for monkey in list_of_monkeys:

        for item in list(monkey.current_items):
            
            # Compute new item value.
            item_new_value = compute_operation(monkey.operation, item, part_2)

            # Throw item to monkey based on result of test.
            if item_new_value % monkey.test == 0:
                list_of_monkeys[monkey.true_idx].current_items.append(item_new_value)
            else:
                list_of_monkeys[monkey.false_idx].current_items.append(item_new_value)

            # Remove item for monkey's item list and increment inspected count.
            monkey.current_items.popleft()
            monkey.inspected_count += 1

    return list_of_monkeys


def compute_operation(operation: List[str], item: int, part_2: bool) -> int:
    """Shows how an item's worry level changes as that monkey inspects an item. Worry levels are multiplied by or added to a number. Operations can be of the following formats:
    new = old * old
    new = old * int
    new = old + old
    new  = old + int"""

    try:
        if operation[0] == '*' and operation[1] == 'old':
             new_item_val =  trunc(int(item**2))

        elif operation[0] == '*' and operation[1].isnumeric():
            new_item_val = trunc(int(item * int(operation[1])))

        elif operation[0] == '+' and operation[1] == 'old':
            new_item_val = trunc(int(item + item))

        elif operation[0] == '+' and operation[1].isnumeric():
            new_item_val = trunc(int(item + int(operation[1])))

    except ValueError:
        print('Operation could not be completed.')

    if part_2 == False:
        return new_item_val / 3
    else:
        return new_item_val

def _parse_input(data: str) -> List[str]:
    """Returns nested list, where each list is a monkey."""

    return [[monkey.strip() for monkey in monkies.split('\n')] for monkies in data.strip().split('\n\n')]


def barrel_of_monkeys(data: List[str]) -> List[Monkey]:
    """Generates a list of Monkeys."""

    monkeys_list = list()
    
    for monkey in data:
        monkeys_list.append(Monkey.from_data(monkey))
        
    return monkeys_list


def part_1_solution(data: List[str]) -> int:
    """Compute solution to puzzle part 1."""

    monkey_list = barrel_of_monkeys(data)

    for _ in range(20):
        monkey_list = inspect_item(monkey_list, part_2=False)
    
    return prod(sorted(monkey.inspected_count for monkey in monkey_list)[-2:])

def part_2_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 2."""

    monkey_list = barrel_of_monkeys(data)

    for _ in range(10000):
        monkey_list = inspect_item(monkey_list, part_2=True)
    
    return prod(sorted(monkey.inspected_count for monkey in monkey_list)[-2:])

    return 0


if __name__ == "__main__":
    # Compute puzzle with example data
    example_data = _parse_input(EXAMPLE_INPUT)

    # Assert the example input results are as expected.
    # assert part_1_solution(example_data) == EXAMPLE_OUTPUT_PART1
    # assert part_2_solution(example_data) == EXAMPLE_OUTPUT_PART2
    # print(part_1_solution(example_data))
    print(part_2_solution(example_data))


    # Read puzzle input.
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
        data = _parse_input(f.read())

    # # Print answers
    print(f'Part 1: { part_1_solution(data=data) }')
    # print(f'Part 2: { part_2_solution(data=data) }')
    print(timeit.timeit())