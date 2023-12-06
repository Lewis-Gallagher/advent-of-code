"""
Solution for Advent of Code 2023 day 06 - https://adventofcode.com/2023/day/06
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time
import numpy as np

EXAMPLE_INPUT = '''\
Time:      7  15   30
Distance:  9  40  200
'''

EXAMPLE_OUTPUT_PART1 = 288
EXAMPLE_OUTPUT_PART2 = 71503


def _parse_input1(data: str) -> List[str]:
    """Parse input text file into usable data structure."""

    x,y = [list(map(int, i.split(":")[1].strip().split())) for i in data.splitlines()]

    z = [[i,j] for i, j in zip(x,y)]

    return z


def _parse_input2(data: str) -> List[str]:
    """Parse input text file into usable data structure."""

    x,y = [int(i.split(":")[1].replace(' ', '')) for i in data.splitlines()]

    return x,y


def part_1_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 1."""

    winning = list()

    for t, d in data:

        counter = 0
        possible = 0

        for i in range(1, t):
            time_left = t - i
            possible = i*time_left

            if possible > d:
                counter += 1

        winning.append(counter)

    return np.prod(winning)


def part_2_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 2."""

    t = data[0]
    d = data[1]
    counter = 0
    possible = 0

    for i in range(1, t):
        time_left = t - i
        possible = i*time_left

        if possible > d:
            counter += 1

    return counter


if __name__ == "__main__":
    # Compute puzzle with example data
    example_data1 = _parse_input1(EXAMPLE_INPUT)
    example_data2 = _parse_input2(EXAMPLE_INPUT)

    # Assert the example input results are as expected.
    assert part_1_solution(example_data1) == EXAMPLE_OUTPUT_PART1
    assert part_2_solution(example_data2) == EXAMPLE_OUTPUT_PART2

    # Read puzzle input for part1.
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
        data1 = _parse_input1(f.read())

    # Print answers
    start_time_1 = time.time()
    print(f'\nPart 1: { part_1_solution(data1) }')
    execution_time_1 = (time.time() - start_time_1)
    print(f'Part 1 execution time: {execution_time_1:.4f}')

    # Read puzzle input for part2.
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
        data2 = _parse_input2(f.read())

    start_time_2 = time.time()
    print(f'\nPart 2: { part_2_solution(data2) }')
    execution_time_2 = (time.time() - start_time_2)
    print(f'Part 2 execution time: {execution_time_2:.4f}')