"""
Solution for Advent of Code 2024 day 02 - https://adventofcode.com/2024/day/02
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time


EXAMPLE_INPUT = '''\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

EXAMPLE_OUTPUT_PART1 = 2
EXAMPLE_OUTPUT_PART2 = 4


def _parse_input(data: str) -> List[int]:
    """Parse input text file into usable data structure."""

    return [[int(level) for level in reports.split()] for reports in data.splitlines()]


def is_safe(record: List[int]) -> bool:
    """First checks record is sorted, then checks each value is between 1-3 different from the next."""

    if record == sorted(record, reverse=True) or record == sorted(record, reverse=False):
        if all([1 <= abs(record[i] - record[i+1]) <= 3 for i in range(len(record)-1)]):
            return record
    return


def fix_record(record: List[int]) -> bool:
    """Iterates through the record taking out one element at a time and checking if that makes it valid."""

    for index in range(len(record)):
        new_record = [record[i] for i in range(len(record)) if i != index]
        if is_safe(new_record):
            return True
        
    return None


def part_1_solution(data: List[int]) -> int:

    safe_counter = 0
    for record in data:
        if is_safe(record):
            safe_counter += 1
    return safe_counter


def part_2_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 2."""

    safe_counter = 0
    for record in data:
        if is_safe(record):
            safe_counter += 1
        else:
            if fix_record(record):
                safe_counter += 1

    return safe_counter


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