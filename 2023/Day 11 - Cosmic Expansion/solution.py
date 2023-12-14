"""
Solution for Advent of Code 2023 day 11 - https://adventofcode.com/2023/day/11
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time
import numpy as np
from itertools import combinations


EXAMPLE_INPUT = '''\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
'''

EXAMPLE_OUTPUT_PART1 = 374
EXAMPLE_OUTPUT_PART2 = 82000210


def _parse_input(data: str) -> List[str]:
    """Parse input text file into usable data structure."""

    return np.array([[i for i in line] for line in data.splitlines()])


def manhattan_distance(cord_a: List[tuple[int]], cord_b: List[tuple[int]]) -> int:
    '''Calculates manhattan/taxicab distance between two xy coordinates.'''

    return (abs(cord_a[0] - cord_b[0])) + (abs(cord_a[1] - cord_b[1]))


def part_1_solution(grid: List[str]) -> int:
    """
    Compute solution to puzzle part 1.
    Instead of expanding the grid upfront, we just determine where the empty rows and columns are and if our path crosses one of these rows/columns, we add to the distance travelled.
    """

    dist = 0
    g_list = list()
    unique_combs = list()

    # Get locations of galaxies.
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                g_list.append((i,j))

    # Make a list of all unique combinations of galaxies.
    for n, i in enumerate(combinations(g_list, 2)):
        unique_combs.append(i)

    # Find empty rows and columns.
    empty_rows = list(map(int, np.where(np.all(grid == '.', axis = 1))[0]))
    empty_cols = list(map(int, np.where(np.all(grid == '.', axis = 0))[0]))

    # For each pair - calculate the manhattan distance including empty rows and columns crossed.    
    for n, c in enumerate(unique_combs, start = 1):

        coordA = c[0]
        coordB = c[1]

        crossed_empty_rows = sum([i in range(min((coordA[0], coordB[0])), max((coordA[0], coordB[0]))) for i in empty_rows])
        crossed_empty_cols = sum([i in range(min((coordA[1], coordB[1])), max((coordA[1], coordB[1]))) for i in empty_cols])

        d = manhattan_distance(coordA, coordB) + crossed_empty_cols + crossed_empty_rows
        dist += d

    return dist


def part_2_solution(grid: List[str]) -> int:
    """
    Compute solution to puzzle part 2.
    Identical to part one, however the galaxies are 1 million times larger, so we multiply the number of empty rows/columns we cross by 999,999.
    """

    dist = 0
    g_list = list()
    unique_combs = list()

    # Get locations of galaxies.
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                g_list.append((i,j))

    # Make a list of all unique combinations of galaxies.
    for n, i in enumerate(combinations(g_list, 2)):
        unique_combs.append(i)

    # Find empty rows and columns.
    empty_rows = list(map(int, np.where(np.all(grid == '.', axis = 1))[0]))
    empty_cols = list(map(int, np.where(np.all(grid == '.', axis = 0))[0]))

    # For each pair - calculate the manhattan distance including empty rows and columns crossed.    
    for n, c in enumerate(unique_combs, start = 1):

        coordA = c[0]
        coordB = c[1]

        crossed_empty_rows = sum([i in range(min((coordA[0], coordB[0])), max((coordA[0], coordB[0]))) for i in empty_rows])
        crossed_empty_cols = sum([i in range(min((coordA[1], coordB[1])), max((coordA[1], coordB[1]))) for i in empty_cols])

        d = manhattan_distance(coordA, coordB) + (crossed_empty_cols*999999) + (crossed_empty_rows*999999)
        dist += d

    return dist


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