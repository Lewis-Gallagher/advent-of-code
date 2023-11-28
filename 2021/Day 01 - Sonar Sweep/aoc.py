"""
Solution for Advent of Code 2021 day 1 - https://adventofcode.com/2021/day/1
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time


EXAMPLE_INPUT = '''\
199
200
208
210
200
207
240
269
260
263
'''

EXAMPLE_OUTPUT_PART1 = 7
EXAMPLE_OUTPUT_PART2 = 5


def _parse_input(data: str) -> List[str]:
    """Parse input text file into usable data structure."""

    return [int(i) for i in data.splitlines()]


def compare_depths(data: List[int], window_size: int) -> int:
    """
    Takes a sequence of integers and compares readings based on sums of window size. Window size can be 0 for single readings.
    Should take O(n) time as the function iterates over the input list once.
    """

    upcount = 0
    prev_sum = 0

    # Get sums of window sizes.
    for i in range(len(data) - window_size + 1):
        w_sum = sum(data[i:i+window_size])

        # Cant compare the first reading.
        if i != 0: 
            # If deeper, iterate.
            if w_sum > prev_sum:
                upcount += 1

        prev_sum = w_sum

    return upcount


def part_1_solution(data: List[int]) -> int:
    """Compute solution to puzzle part 1."""

    return compare_depths(data, 1)
    

def part_2_solution(data: List[int]) -> Any:
    """Compute solution to puzzle part 2."""

    return compare_depths(data, 3)


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
    print(f'Part 2 execution time: {execution_time_1:.4f}')