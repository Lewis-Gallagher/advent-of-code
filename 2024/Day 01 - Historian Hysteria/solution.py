"""
Solution for Advent of Code 2024 day 01 - https://adventofcode.com/2024/day/01
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time


EXAMPLE_INPUT = '''\
3   4
4   3
2   5
1   3
3   9
3   3
'''

EXAMPLE_OUTPUT_PART1 = 11
EXAMPLE_OUTPUT_PART2 = 31


def _parse_input(data: str) -> List[int]:
    """Parse input text file into usable data structure."""

    d = [[int(i) for i in line.split()] for line in data.splitlines()]
    x = [i[0] for i in d]
    y = [i[1] for i in d]

    return x,y


def part_1_solution(list_1: List[int], list_2: List[int]) -> int:
    """Compute solution to puzzle part 1."""

    return sum([abs(i-j) for i,j in zip(sorted(list_1), sorted(list_2))])


def part_2_solution(list_1: List[int], list_2: List[int]) -> int:
    """Compute solution to puzzle part 2."""

    return sum([i * list_2.count(i) for i in list_1])


if __name__ == "__main__":
    # Compute puzzle with example data
    example_x, example_y = _parse_input(EXAMPLE_INPUT)

    # Assert the example input results are as expected.
    assert part_1_solution(example_x, example_y) == EXAMPLE_OUTPUT_PART1
    assert part_2_solution(example_x, example_y) == EXAMPLE_OUTPUT_PART2

    # Read puzzle input.
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
        x,y = _parse_input(f.read())

    # Print answers
    start_time_1 = time.time()
    print(f'\nPart 1: { part_1_solution(x,y) }')
    execution_time_1 = (time.time() - start_time_1)
    print(f'Part 1 execution time: {execution_time_1:.4f}')

    start_time_2 = time.time()
    print(f'\nPart 2: { part_2_solution(x,y) }')
    execution_time_2 = (time.time() - start_time_2)
    print(f'Part 2 execution time: {execution_time_2:.4f}')