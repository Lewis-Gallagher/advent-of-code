"""
Solution for Advent of Code 2023 day 13 - https://adventofcode.com/2023/day/13
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time
import numpy as np


EXAMPLE_INPUT = '''\
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
'''


EXAMPLE_OUTPUT_PART1 = 405
EXAMPLE_OUTPUT_PART2 = 400


def _parse_input(data: str) -> List[str]:
    """Parse input text file into usable data structure."""

    return np.array([[i for i in line.split()] for line in data.split('\n\n')], dtype='object')


def find_mirror(grid: List[str]) -> int:
    """
    Takes a list of strings and finds the reflection point. Returns the number of rows above the reflection point.
    """

    nrow = len(grid)
    for n, (a, b) in enumerate(zip(grid, grid[1:])):
        
        if a == b:   
            m = n + 1                   # m is the mirror of n. Incidentally, our return value.
            length = min(m, nrow-(m))   # Find the smallest distance before grid boundary.

            # Iterate outwards from the mirror until the closest grid boudnary.
            for i in range(1, length):
                if grid[n-i] == grid[m+i]:
                    continue
                else:
                    break
                
            # If we don't break the loop (all rows match), return.
            else:
                return m
    
    return 0


def mismatches(a: str, b: str) -> int:
    """
    Takes two strings and returns the number of mismatches between them.
    """

    t = 0
    for i, j in zip(a, b):
        if i != j:
            t += 1
    return t


def find_mirror_2(grid: List[str]) -> int:
    """
    Takes a list of strings and finds the reflection point. There must be exactly 1 smudge in the grid.
    """

    nrow = len(grid)
    for n, (a, b) in enumerate(zip(grid, grid[1:])):
        smudges = mismatches(a, b)
        if smudges <= 1:  
            m = n + 1                   # m is the mirror of n. Incidentally, our return value.
            length = min(m, nrow-(m))   # Find the smallest distance before grid boundary.

            # Iterate outwards from the mirror until the closest grid boudnary.
            for i in range(1, length):
                # We must have at most 1 smudge.
                smudges += mismatches(grid[n-i], grid[m+i])
                if smudges <= 1:
                    continue

            # If we don't break the loop (all rows match and must have 1 smudge), return.
            else:
                if smudges == 1:
                    return m
                    
    return 0


def part_1_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 2."""

    # Finds the reflection point in the grid. Also transpose the grid to find reflecting columns.
    total = 0

    for grid in data:
        row = find_mirror(grid)
        total += row * 100
        col = find_mirror(list(zip(*grid)))
        total += col

    return total


def part_2_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 2."""

    # Finds the reflection point in the grid. Also transpose the grid to find reflecting columns.
    total = 0

    for grid in data:
        row = find_mirror_2(grid)
        total += row * 100
        col = find_mirror_2(list(zip(*grid)))
        total += col

    return total


if __name__ == "__main__":
    # Compute puzzle with example data
    example_data = _parse_input(EXAMPLE_INPUT)
    # Assert the example input results are as expected.
    assert part_1_solution(example_data) == EXAMPLE_OUTPUT_PART1
    assert part_2_solution(example_data) == EXAMPLE_OUTPUT_PART2

    # Read puzzle input.
    with open(os.path.join(os.path.dirname(__file__), "input"), "r", encoding="utf-8") as f:
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