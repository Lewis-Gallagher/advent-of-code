"""
Solution for Advent of Code 2023 day 08 - https://adventofcode.com/2023/day/08
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time
import re


EXAMPLE_INPUT = '''\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
'''

EXAMPLE_OUTPUT_PART1 = 6
EXAMPLE_OUTPUT_PART2 = 0


def _parse_input(data: str) -> List[str]:
    """Parse input text file into usable data structure."""

    # instructions, *letters assigns the first line of the split to instructions and everything else to letters.
    instructions, *letters = data.split('\n\n')

    d = dict()

    # Not very graceful but reads into a dict.
    for line in letters:
        for l in line.splitlines():
            m = re.findall('(\w{3})', l)
            d[m[0]] = [m[1], m[2]]

    return instructions, d


def part_1_solution(instructions: str, letters: dict[str]) -> int:
    """Compute solution to puzzle part 1."""

    # Count steps.
    steps = 0

    # Start at AAA.
    curr = {k:v for k, v in letters.items() if k == 'AAA'}

    while list(curr.keys())[0] != 'ZZZ':

        # For each letter perform the opperation.
        for l in instructions:
                        
            # Go left or right and update the current position.
            if l == 'L':
                curr = {k:v for k, v in letters.items() if k == list(curr.values())[0][0]}
            else:
                curr = {k:v for k, v in letters.items() if k == list(curr.values())[0][1]}

            steps += 1

    return steps


def part_2_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 2."""
    return 0


if __name__ == "__main__":
    # Compute puzzle with example data
    example_intstructions, example_letters = _parse_input(EXAMPLE_INPUT)
    
    # # Assert the example input results are as expected.
    assert part_1_solution(example_intstructions, example_letters) == EXAMPLE_OUTPUT_PART1
    # assert part_2_solution(example_data) == EXAMPLE_OUTPUT_PART2

    # Read puzzle input.
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
        intsructions, letters = _parse_input(f.read())

    # Print answers
    start_time_1 = time.time()
    print(f'\nPart 1: { part_1_solution(intsructions, letters) }')
    execution_time_1 = (time.time() - start_time_1)
    print(f'Part 1 execution time: {execution_time_1:.4f}')

    # start_time_2 = time.time()
    # print(f'\nPart 2: { part_2_solution(data) }')
    # execution_time_2 = (time.time() - start_time_2)
    # print(f'Part 2 execution time: {execution_time_2:.4f}')
