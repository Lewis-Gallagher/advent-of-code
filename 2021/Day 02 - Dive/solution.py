"""
Solution for Advent of Code 2021 day 02 - https://adventofcode.com/2021/day/02
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time


EXAMPLE_INPUT = '''\
forward 5
down 5
forward 8
up 3
down 8
forward 2
'''

EXAMPLE_OUTPUT_PART1 = 150
EXAMPLE_OUTPUT_PART2 = 900


def _parse_input(data: str) -> List[str]:
    """Parse input text file into usable data structure."""

    data = data.splitlines()

    return data


def part_1_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 1.
    
    forward X increases the horizontal position by X units.
    down X increases the depth by X units.
    up X decreases the depth by X units."""

    depth = 0
    horizontal = 0

    for i in data:
        cmd, x = i.split()
        x = int(x)       

        if cmd == 'down':
            depth += x
        elif cmd == 'up':
            depth -= x
        elif cmd == 'forward':
            horizontal += x

    return depth*horizontal


def part_2_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 2.
    
    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X."""
    
    aim = 0
    depth = 0
    horizontal = 0

    for i in data:
        cmd, x = i.split()
        x = int(x)  

        if cmd == 'down':
            aim += x
        elif cmd == 'up':
            aim -= x
        elif cmd == 'forward':
            horizontal += x
            depth += aim*x
        
    return depth*horizontal


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