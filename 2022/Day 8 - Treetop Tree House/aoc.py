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


def part_1_solution(data: List[str]) -> int:
    """Compute solution to puzzle part 1."""
    
    def is_visible(tree: int, data: List[int]) -> bool:
        """Check if the tree is visible from the right, left, top or bottom respectively."""
        if tree > max(data[i+1][0:j+1]) or \
            tree > max(data[i+1][j+2:]) or \
            tree > max([row[j+1] for row in data[:i+1]]) or \
            tree > max([row[j+1] for row in data[i+2:]]):
            return True
    
    # All tree edges are visible. Get sum of shape.
    visible = len(data) * 2 + len(data[0]) * 2 - 4

    # Get inner trees only.
    data_inner = [row[1:-1] for row in data[1:-1]]

    for i in range(len(data_inner)):
        for j in range(len(data_inner[i])):
            if is_visible(data_inner[i][j], data):
                visible += 1

    return visible


# def part_2_solution(data: List[str]) -> int:
#     """Compute solution to puzzle part 2."""

#     for i in range(len(data)):
#         for j in range(len(data[i])):
#             if is_visible(data[i][j]):
                


#     return scenic_score


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