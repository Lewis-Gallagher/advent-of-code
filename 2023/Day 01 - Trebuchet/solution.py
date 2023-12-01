"""
Solution for Advent of Code 2023 day 01 - https://adventofcode.com/2023/day/01
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time

EXAMPLE_INPUT1 = '''\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
'''

EXAMPLE_INPUT2 = '''\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''

EXAMPLE_OUTPUT_PART1 = 142
EXAMPLE_OUTPUT_PART2 = 281


def _parse_input(data: str) -> List[str]:
    """Parse input text file into usable data structure."""

    return [line for line in data.splitlines()]


def part_1_solution(data: List[str]) -> int:
    """Compute solution to puzzle part 1."""

    sums = []

    for line in data:

        i = 0
        j = len(line)-1
        nums = []
        i_found = False
        j_found = False

        while not i_found:
            if str(line[i]).isnumeric():
                nums.append(line[i])
                i_found = True
            else:
                i+=1

        while not j_found:
            if str(line[j]).isnumeric():
                nums.append(line[j])
                j_found = True
            else:
                j-=1

        s = int(''.join(nums))   
        sums.append(s) 

    return sum(sums)

def part_2_solution(data: List[str]) -> int:
    """Compute solution to puzzle part 2."""

    digit_dict = {
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9
    }

    sums = []

    for line in data:

        i = 0
        j = len(line)
        nums = []
        i_found = False
        j_found = False


        while not i_found and i < len(line):
            for k,v in digit_dict.items():
                if line[i:].startswith(k) or line[i:].startswith(str(v)):
                    nums.append(v)
                    i_found = True
            i+=1

        while not j_found and j > 0:
            for k,v in digit_dict.items():
                if line[:j].endswith(k) or line[:j].endswith(str(v)):
                    nums.append(v)
                    j_found = True
            j-=1


        s = int(''.join([str(i) for i in nums]))
        sums.append(s)

    return sum(sums)


if __name__ == "__main__":
    # Compute puzzle with example data
    example_data1 = _parse_input(EXAMPLE_INPUT1)
    example_data2 = _parse_input(EXAMPLE_INPUT2)

    # # Assert the example input results are as expected.
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