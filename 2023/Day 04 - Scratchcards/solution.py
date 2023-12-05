"""
Solution for Advent of Code 2023 day 04 - https://adventofcode.com/2023/day/04
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time

EXAMPLE_INPUT = '''\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''

EXAMPLE_OUTPUT_PART1 = 13
EXAMPLE_OUTPUT_PART2 = 30


def _parse_input(data):
    """Parse input text file into usable data structure."""

    d = [i.split(":")[1].strip() for i in data.splitlines()]

    x = [[list(map(int, k.split())) for k in j.split("| ")] for j in d]

    return x


def part_1_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 1."""

    total = 0

    for x,y in data:

        # If a number is in the winning list, tally it.
        m = sum([i in x for i in y])
        
        # Double the score. -1 because 2**0 gives 1. 2**2 gives 2, 2**3 gives 4 etc.
        if m > 0:
            total += 2 ** (m-1)
    
    return total


def part_2_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 2."""

    # Dict containing copies of each card
    copies = {}

    # All cards start with 1 copy.
    for i in range(len(data)):
        copies[i] = 1

    # Enumerate over cards.
    for card, (x,y) in enumerate(data):

        # If a number is in the winning list, tally it.
        m = sum([i in x for i in y])

        # Loop through the next `m` cards.
        for next in range(card+1, card+m+1):

            # Add the number of instances of this card to the next.
            copies[next] += copies[card]
        
    return sum(copies.values())


if __name__ == "__main__":
    # Compute puzzle with example data
    example_data = _parse_input(EXAMPLE_INPUT)

    # Assert the example input results are as expected.
    assert part_1_solution(example_data) == EXAMPLE_OUTPUT_PART1
    assert part_2_solution(example_data) == EXAMPLE_OUTPUT_PART2

    # Read puzzle input.
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
        data = _parse_input(f.read())

    # Print answers
    start_time_1 = time.time()
    print(f'\nPart 1: { part_1_solution(data) }')
    execution_time_1 = (time.time() - start_time_1)
    print(f'Part 1 execution time: {execution_time_1:.4f}')

    start_time_2 = time.time()
    print(f'\nPart 2: { part_2_solution(data) }')
    execution_time_2 = (time.time() - start_time_2)
    print(f'Part 2 execution time: {execution_time_2:.4f}')