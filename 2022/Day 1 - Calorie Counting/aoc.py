"""
Solution for Advent of Code 2022 day 1 - https://adventofcode.com/2022/day/1
"""
import os
from typing import List, Any
import timeit

EXAMPLE_INPUT = '''\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000\
'''
EXAMPLE_OUTPUT_PART1 = 24000
EXAMPLE_OUTPUT_PART2 = 45000


def _parse_input(data: List[str]) -> List[str]:
    """Parse input text file into usable data structure."""
    return [[int(e) for e in elf.splitlines()] for elf in data.split("\n\n")]

def part_1_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 1."""
    return sorted([sum(elf) for elf in data])[-1]

def part_2_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 2."""
    return sum(sorted([sum(elf) for elf in data])[-3:])

if __name__ == "__main__":
    # Compute puzzle with example data.
    example_data = _parse_input(EXAMPLE_INPUT)

    # Assert the example input results are as expected.
    assert part_1_solution(example_data) == EXAMPLE_OUTPUT_PART1
    assert part_2_solution(example_data) == EXAMPLE_OUTPUT_PART2

    # Read puzzle input.
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
        data = _parse_input(f.read())

    # Print answers.
    print(f'Part 1: { part_1_solution(data=data) }')
    print(f'Part 2: { part_2_solution(data=data) }')
    print(timeit.timeit())