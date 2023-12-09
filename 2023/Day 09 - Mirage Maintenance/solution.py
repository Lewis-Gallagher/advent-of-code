"""
Solution for Advent of Code 2023 day 09 - https://adventofcode.com/2023/day/09
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time


EXAMPLE_INPUT = '''\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
'''

EXAMPLE_OUTPUT_PART1 = 114
EXAMPLE_OUTPUT_PART2 = 0


def _parse_input(data: str) -> List[str]:
    """Parse input text file into usable data structure."""

    return [[int(j) for j in i.split()] for i in data.splitlines()]


def build_list(li: List[int]) -> List[int]:

    new_list = [None] * (len(li) - 1)

    for i in range(len(li) - 1):
        new_list[i] = li[i+1] - li[i]

    return new_list


def part_1_solution(data: List[int]) -> int:
    """Compute solution to puzzle part 1."""

    predicted = []

    for li in data:

        new_list = [li.copy()]
        
        while not all(i == 0 for i in new_list[-1]):
            new = build_list(new_list[-1])
            new_list.append(new)

        for i in reversed(range(0, len(new_list) - 1)):
            val = new_list[i][-1] + new_list[i+1][-1]
            new_list[i].append(val)

        predicted.append(new_list[0][-1])

    return sum(predicted)


def part_2_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 2."""

    predicted = []

    for li in data:

        new_list = [li.copy()]
        
        while not all(i == 0 for i in new_list[-1]):
            new = build_list(new_list[-1])
            new_list.append(new)

        for i in reversed(range(0, len(new_list) - 1)):
            val = new_list[i][0] - new_list[i+1][0]
            new_list[i].insert(0, val)

        predicted.append(val)

    return sum(predicted)


if __name__ == "__main__":
    # Compute puzzle with example data
    example_data = _parse_input(EXAMPLE_INPUT)
    print(example_data)
    # print(part_1_solution(example_data))

    # # Assert the example input results are as expected.
    assert part_1_solution(example_data) == EXAMPLE_OUTPUT_PART1
    print(part_1_solution(example_data))
    # assert part_2_solution(example_data) == EXAMPLE_OUTPUT_PART2

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
