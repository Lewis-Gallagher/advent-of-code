"""
Solution for Advent of Code 2022 day 11 - https://adventofcode.com/2022/day/11
Author - Lewis Gallagher
"""

from __future__ import annotations
import os
from typing import List, Dict
import time
from collections import deque
import re
import math
from copy import deepcopy


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
EXAMPLE_OUTPUT_PART2 = 2713310158


class Monkey:
    """
    The Monkey class possesses many attributes.
    current_items represents the all the items a monkey has and their worry levles.
    operation represents how the worry level of each item should change upon inspection.
    """
    def __init__(self, monkey_num: int, current_items: List[int], operation: str, divisor: int, true_idx: int, false_idx: int) -> None:
        self.monkey_num = monkey_num # E.g. 0
        self.current_items = current_items # E.g. [11,65,75]
        self.operation = operation # E.g. ['*', '8']
        self.divisor = divisor # E.g. 23
        self.true_idx = true_idx # E.g. 1
        self.false_idx = false_idx # E.g. 2
        self.inspected_count = 0 # Start at zero
    
    def __repr__(self) -> str:
        return f"Monkey:(id={self.monkey_num}, items={self.current_items}, inspect_count={self.inspected_count})"


    def inspect_item(self, releif=True, lcm=None) -> int:
        """Inspects the next item in a Monkey's item list. 
        Inspecting causes our worry level to go up, before it is divided by three and rounded down. 
        Then we test who to throw to, by dividing by a divisor."""

        # Find if the operation is multiplication or addition and compute operation accordingly:
        # new = old * int
        # new = old + int
        # new = old * old
        # new = old + old

        try:
            if self.operation[0] == '*' and self.operation[1] == 'old':
                self.current_items[0] = self.current_items[0]**2

            elif self.operation[0] == '*' and self.operation[1].isnumeric():
                self.current_items[0] = self.current_items[0] * int(self.operation[1])

            elif self.operation[0] == '+' and self.operation[1] == 'old':
                self.current_items[0] = self.current_items[0] + self.current_items[0]

            elif self.operation[0] == '+' and self.operation[1].isnumeric():
                self.current_items[0] = self.current_items[0] + int(self.operation[1])

        except ValueError:
            print('Operation could not be completed.')

        # Reduce our worry level using releif or lcm.
        if releif:
            self.current_items[0] = self.current_items[0] // 3
        if lcm:
            self.current_items[0] %= lcm

        # Increment inspected counter.
        self.inspected_count += 1
 
        # Return an int representing which monkey to throw to.
        if self.current_items[0] % self.divisor == 0:
            return self.true_idx    
        else:
            return self.false_idx


    def add_item(self, item: int):
        """Receives an item and appends it to end of monkey's item list."""
        self.current_items.append(item)


    def give_item(self, other: Monkey) -> int:
        """Adds current item to the item list of a monkey while removing from the list of the current monkey."""
        other.add_item(self.current_items.popleft())        


def get_lcm(monkey_dict: Dict[int, Monkey]):
    """Copmutes lowest common multiple of all divisors. Because all divisors are prime numbers this equals the product of them all."""
    return math.lcm(*[monkey.divisor for monkey in monkey_dict.values()])


def _parse_input(data: str) -> List[str]:
    """
    Reads the input data into a list of lists, where each sublist represents a monkey.
    Then regex out all the relevant numbers and create a Monkey class object.
    Append Monkey object to a dictionairy of Monkeys where the keys are the monkey_num.
    """

    monkey_dict = dict()

    monkey_list = [[monkey.strip() for monkey in monkies.split('\n')] for monkies in data.strip().split('\n\n')]

    for monkey in monkey_list:
        monkey_number = re.findall(r"^\s*Monkey (\d)", monkey[0])[0]
        starting_items = re.findall(r"^\s*Starting items: (\d+.*)", monkey[1])
        operation = re.findall(r"^\s*Operation: new = old ([+*] .+)", monkey[2])
        divisor = re.findall(r"^\s*Test: divisible by (\d*)", monkey[3])[0]
        test_true_throw = re.findall(r"^\s*If true: throw to monkey (\d*)", monkey[4])[0]
        test_false_throw = re.findall(r"^\s*If false: throw to monkey (\d*)", monkey[5])[0]

        # Turn starting items into list of ints.
        starting_items = [int(item) for item in ' '.join(starting_items).split(', ')]
        operation = [op for op in ' '.join(operation).split(' ')]

        monkey =  Monkey(
            monkey_num = int(monkey_number),
            current_items = deque(starting_items),
            operation = operation,
            divisor = int(divisor),
            true_idx = int(test_true_throw),
            false_idx = int(test_false_throw)
        )

        monkey_dict[monkey_number] = monkey

    return monkey_dict


def part_1_solution(monkey_dict: Dict[int, Monkey]) -> int:
    """Compute solution to puzzle part 1."""

    # 20 rounds of play.
    rounds_to_play = 20

    for _ in range(1, rounds_to_play+1):
        for monkey in monkey_dict.values(): # Iterator through monkeys in order.
            while monkey.current_items: # Monkey inspects and throws until it has no more items.
                to_monkey = list(monkey_dict.values())[monkey.inspect_item()] # Find which monkey to throw to.
                monkey.give_item(to_monkey) # Throw to the chosen monkey.

    # Return monkey business. i.e. the total of two highest inspection_counts multiplied together.
    return math.prod(sorted(monkey.inspected_count for monkey in monkey_dict.values())[-2:])


def part_2_solution(monkey_dict: Dict[int, Monkey]) -> int:
    """Compute solution to puzzle part 2."""

    # 10000 rounds of play.
    rounds_to_play = 10000
    
    for _ in range(1, rounds_to_play+1):
        for monkey in monkey_dict.values(): # Iterator through monkeys in order.
            while monkey.current_items: # Monkey inspects and throws until it has no more items.
                to_monkey = list(monkey_dict.values())[monkey.inspect_item(releif=False, lcm=get_lcm(monkey_dict))] # Find which monkey to throw to using lcm mod.
                monkey.give_item(to_monkey) # Throw to the chosen monkey.

    # Return monkey business. i.e. the total of two highest inspection_counts multiplied together.
    return math.prod(sorted(monkey.inspected_count for monkey in monkey_dict.values())[-2:])


if __name__ == "__main__":
    # Compute puzzle with example data.
    example_data = _parse_input(EXAMPLE_INPUT)

    # Assert the example input results are as expected.
    assert part_1_solution(deepcopy(example_data)) == EXAMPLE_OUTPUT_PART1
    assert part_2_solution(deepcopy(example_data)) == EXAMPLE_OUTPUT_PART2

    # Read puzzle input.
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
        data = _parse_input(f.read())

    # Print answers.
    start_time_1 = time.time()
    print(f'Part 1: { part_1_solution(deepcopy(data)) }')
    execution_time_1 = (time.time() - start_time_1)
    print('Part 1 execution time: ' + str(execution_time_1))

    start_time_2 = time.time()
    print(f'Part 2: { part_2_solution(deepcopy(data)) }')
    execution_time_2 = (time.time() - start_time_2)
    print('Part 2 execution time: ' + str(execution_time_2))