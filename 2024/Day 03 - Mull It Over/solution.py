"""
Solution for Advent of Code 2024 day 03 - https://adventofcode.com/2024/day/03
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time
import re


EXAMPLE_INPUT1 = '''\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''

EXAMPLE_INPUT2 = '''\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''

EXAMPLE_OUTPUT_PART1 = 161
EXAMPLE_OUTPUT_PART2 = 48


def _parse_input(data: str) -> str:
    """Parse input text file into usable data structure."""

    return data


def part_1_solution(data: str) -> int:
    """Compute solution to puzzle part 1."""

    vals = list()
    matches = re.findall(r'mul(\(\d{1,3},\d{1,3}\))', data)
    
    for mul in matches:
        x,y = [int(i) for i in mul.strip('()').split(',')]
        vals.append(x*y)

    return sum(vals)


def part_2_solution(data: str) -> int:

    total = 0
    do = True

    for match in re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", data):
        if match == "do()":
            do = True
        elif match == "don't()":
            do = False
        elif do:
            x, y = list(map(int, match[4:-1].split(',')))
            total += x * y

    return total

# def part_2_solution(data: List[str]) -> Any:
#     """Compute solution to puzzle part 2."""

#     vals = list()

#     # split by valid mul functions
#     split_list = re.split(r'(mul\(\d{1,3},\d{1,3}\))', data)

#     # Mul is enabled by default
#     do = True

#     for s in split_list:
        
#         # Check if do/don't is present before the mul
#         do_dont = re.findall(r"do\(\)|don't\(\)", s)
#         if do_dont:
#             if do_dont[-1] == "do()":
#                 do = True
#             elif do_dont[-1] == "don't()":
#                 do = False

#         if do:
#             matches = re.findall(r'mul(\(\d{1,3},\d{1,3}\))', s)
            
#             for mul in matches:
#                 x,y = [int(i) for i in mul.strip('()').split(',')]
#                 vals.append(x*y)

#     return sum(vals)
                

if __name__ == "__main__":
    # Compute puzzle with example data
    example_data1 = _parse_input(EXAMPLE_INPUT1)
    example_data2 = _parse_input(EXAMPLE_INPUT2)

    # Assert the example input results are as expected.
    assert part_1_solution(example_data1) == EXAMPLE_OUTPUT_PART1
    assert part_2_solution(example_data2) == EXAMPLE_OUTPUT_PART2

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
