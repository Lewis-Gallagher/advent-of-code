"""
Solution for Advent of Code 2022 day 12 - https://adventofcode.com/2022/day/12
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time


EXAMPLE_INPUT = '''\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''

EXAMPLE_OUTPUT_PART1 = 0
EXAMPLE_OUTPUT_PART2 = 0


def _parse_input(data: str) -> List[str]:
    """Parse input text file into usable data structure."""

    return [[i for i in row] for row in data.splitlines()]


def part_1_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 1."""

    return 0


def part_2_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 2."""
    return 0


if __name__ == "__main__":
    # Compute puzzle with example data
    example_data = _parse_input(EXAMPLE_INPUT)
    print(example_data)
    # Assert the example input results are as expected.
    # assert part_1_solution(example_data) == EXAMPLE_OUTPUT_PART1
    # assert part_2_solution(example_data) == EXAMPLE_OUTPUT_PART2

    # Read puzzle input.
    # with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
    #     data = _parse_input(f.read())

    # # Print answers
    # start_time_1 = time.time()
    # print(f'Part 1: { part_1_solution(data) }')
    # execution_time_1 = (time.time() - start_time_1)
    # print('Part 1 execution time: ' + str(execution_time_1))

    # start_time_2 = time.time()
    # print(f'Part 2: { part_2_solution(data) }')
    # execution_time_2 = (time.time() - start_time_2)
    # print('Part 2 execution time: ' + str(execution_time_2))