"""
Solution for Advent of Code 2024 day 05 - https://adventofcode.com/2024/day/05
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time
from copy import deepcopy


EXAMPLE_INPUT = '''\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''

EXAMPLE_OUTPUT_PART1 = 143
EXAMPLE_OUTPUT_PART2 = 123


def _parse_input(data: str) -> tuple[List[int], List[int]]:
    """Parse input text file into usable data structure."""

    sections = [line.split('\n') for line in data.split('\n\n')]
    orders = [list(map(int, i.split('|'))) for i in sections[0]]
    updates = [list(map(int, i.split(','))) for i in sections[1]]

    return orders, updates

def is_ordered(order_list: List[int], update: List[int]) -> bool:

    for order in order_list:

        # Check if ordering instructions are relevant
        if not all(i in update for i in order): continue

        # Check for correct ordering
        if not update.index(order[0]) < update.index(order[1]):
            return False
        
    return True

def fix_order(order_list: List[int], update: List[int]) -> List[int]:

    # print(update)
    for order in order_list:
        # Check instructions have relevant numbers and needs to be reordered
        if not all(i in update for i in order): continue
        if update.index(order[0]) < update.index(order[1]): continue
        
        update.insert(0, update.pop(update.index(order[0])))
        print(update, order)

    return update


def part_1_solution(order_list: List[int], update_list: List[int]) -> int:
    """Compute solution to puzzle part 1."""

    middle_vals = list()
    correct = list()

    for update in deepcopy(update_list):        
        if is_ordered(order_list, update):
            correct.append(update)

    middle_vals = [i[len(i) // 2] for i in correct]

    return sum(middle_vals)


#### Incorrect - To complete ###

# def part_2_solution(order_list: List[int], update_list: List[int]) -> int:
#     """Compute solution to puzzle part 2."""

#     middle_vals = list()
#     incorrect = list()
#     corrected = list()

#     for update in deepcopy(update_list):
#         if not is_ordered(order_list, update):
    
#             new = fix_order(order_list, update)
#             corrected.append(new)
#             # print(update, new)

#             middle_vals.append(update[len(update) // 2])

#     # print(corrected)
#     return sum(middle_vals)


if __name__ == "__main__":
    # Compute puzzle with example data
    example_orders, example_updates = _parse_input(EXAMPLE_INPUT)
    print(part_1_solution(example_orders, example_updates))
    print(part_2_solution(example_orders, example_updates))

    # Assert the example input results are as expected.
    assert part_1_solution(example_orders, example_updates) == EXAMPLE_OUTPUT_PART1
    assert part_2_solution(example_orders, example_updates) == EXAMPLE_OUTPUT_PART2

    # Read puzzle input.
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
        orders, updates = _parse_input(f.read())

    # Print answers
    start_time_1 = time.time()
    print(f'\nPart 1: { part_1_solution(orders, updates) }')
    execution_time_1 = (time.time() - start_time_1)
    print(f'Part 1 execution time: {execution_time_1:.4f}')

    start_time_2 = time.time()
    print(f'\nPart 2: { part_2_solution(orders, updates) }')
    execution_time_2 = (time.time() - start_time_2)
    print(f'Part 2 execution time: {execution_time_2:.4f}')