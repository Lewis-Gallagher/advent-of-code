"""
Solution for Advent of Code 2022 day 8 - https://adventofcode.com/2022/day/8
"""

import os
from typing import List
import numpy as np
import timeit


EXAMPLE_INPUT = '''\
30373
25512
65332
33549
35390'''

EXAMPLE_OUTPUT_PART1 = 21
EXAMPLE_OUTPUT_PART2 = 8


def _parse_input(data: str) -> List[int]:
    """Parse input text file into list of lists."""
    data = [[int(d) for d in row] for row in data.splitlines()]

    return data


def is_visible(i: int, j: int, data: List[int]) -> bool:
    """Takes (x,y) coordinates as input and checks if the tree at that location is visible from the left, right, top or bottom respectively."""

    if data[i][j] > max(data[i][:j]) or \
        data[i][j] > max(data[i][j+1:]) or \
        data[i][j] > max([row[j] for row in data[:i]]) or \
        data[i][j] > max([row[j] for row in data[i+1:]]):
        return True


def part_1_solution(data: List[str]) -> int:
    """Compute solution to puzzle part 1."""
    
    # All tree edges are visible. Get sum of shape.
    visible = len(data) * 2 + len(data[0]) * 2 - 4

    # Iterate through rows and columns.
    for i in range(1, len(data)-1):
        for j in range(1, len(data[i])-1):
            if is_visible(i, j, data):
                visible += 1

    return visible


def part_2_solution(data: List[str]) -> int:
    """Compute solution to puzzle part 2."""

    return 0


if __name__ == "__main__":
    # Compute puzzle with example data
    example_data = _parse_input(EXAMPLE_INPUT)

    # Assert the example input results are as expected.
    assert part_1_solution(example_data) == EXAMPLE_OUTPUT_PART1
    # assert part_2_solution(example_data) == EXAMPLE_OUTPUT_PART2

    # Read puzzle input.
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
        data = _parse_input(f.read())

    # Print answers
    print(f'Part 1: { part_1_solution(data=data) }')
    # print(f'Part 2: { part_2_solution(data=data) }')
    print(timeit.timeit())