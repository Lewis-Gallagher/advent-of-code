"""
Solution for Advent of Code 2021 day 03 - https://adventofcode.com/2021/day/03
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time
from collections import Counter
import numpy as np


EXAMPLE_INPUT = '''\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
'''

EXAMPLE_OUTPUT_PART1 = 198
EXAMPLE_OUTPUT_PART2 = 230


def _parse_input(data: str) -> List[str]:
    """Parse input text file into usable data structure."""

    data = [[int(x) for x in i] for i in data.splitlines()]

    return data


def part_1_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 1."""

    data = np.transpose(data)

    gamma = []
    epsilon = []

    for i in range(len(data)):
        c = Counter(data[i]).most_common(2)

        g = c[0][0]
        e = c[-1][0]
        gamma.append(g)
        epsilon.append(e)
    
    gamma = int(''.join(map(str, gamma)),2)
    epsilon = int(''.join(map(str, epsilon)),2)

    return gamma*epsilon


def part_2_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 2."""

    data_o2 = data
    data_co2 = data

    # transpose data
    data_t = np.transpose(data)

    for pos in range(len(data_t)):

        # Count values at each position as matrice are updated
        o2_counter = Counter([x[pos] for x in data_o2])
        co2_counter = Counter([x[pos] for x in data_co2])

        # Update matrices
        if o2_counter[0] > o2_counter[1]:
            data_o2 = [x for x in data_o2 if x[pos] == 0]
        else:
            data_o2 = [x for x in data_o2 if x[pos] == 1]
        
        if co2_counter[0] > co2_counter[1]:
            data_co2 = [x for x in data_co2 if x[pos] == 1]
        else:
            data_co2 = [x for x in data_co2 if x[pos] == 0]

        if data_o2:
            o2 = int(''.join(map(str, data_o2[0])), 2)
        if data_co2:
            co2 = int(''.join(map(str, data_co2[0])), 2)


    return o2*co2


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
