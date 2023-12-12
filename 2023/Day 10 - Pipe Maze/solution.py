"""
Solution for Advent of Code 2023 day 10 - https://adventofcode.com/2023/day/10
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time
import numpy as np
from collections import deque


EXAMPLE_INPUT = '''\
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
'''

EXAMPLE_OUTPUT_PART1 = 8
EXAMPLE_OUTPUT_PART2 = 0


def _parse_input(data: str) -> List[List[str]]:
    """Parse input text file into usable data structure."""

    return np.array([[i for i in line] for line in data.splitlines()])


def floodfill(grid: List[List[str]], i:int, j:int) -> int:

    steps = 0
    nrow = len(grid)
    ncol = len(grid[0])

    queue = deque()
    queue.append((i,j))
    seen = [(i, j)]

    while queue:
        i,j = queue.pop()

        # Can we go up? Can selected cell go up (S|JL) and can the next cell receive an upward move? (|7F)?
        if i > 0 and grid[i][j] in 'S|JL' and grid[i-1][j] in '|7F' and (i-1, j) not in seen:
            seen.append((i-1, j))
            queue.appendleft((i-1, j))

        # Can we go down? Can selected cell go down (S|7F) and can the next cell receive an downward move? (|JL)?
        if i <= nrow and grid[i][j] in 'S|7F' and grid[i+1][j] in '|JL)' and (i+1, j) not in seen:
            seen.append((i+1, j))
            queue.appendleft((i+1, j))
        
        # Can we go left? Can selected cell go left (S-7J) and can the next cell receive an left move? (-FL)?
        if j > 0 and grid[i][j] in 'S-7J' and grid[i][j-1] in '-FL' and (i, j-1) not in seen:
            seen.append((i, j-1))
            queue.appendleft((i, j-1))

        # Can we go right? Can selected cell go right (S-FL) and can the next cell receive an right move? (-7J)?
        if j <= ncol and grid[i][j] in 'S-FL' and grid[i][j+1] in '-7J' and (i, j+1) not in seen:
            seen.append((i, j+1))
            queue.appendleft((i, j+1))

        steps += 1

    return steps//2


def part_1_solution(data: List[List[str]]) -> None:
    """Compute solution to puzzle part 1."""

    start = np.where(data == 'S')
    sr = start[0][0]
    sc = start[1][0]

    return floodfill(data, sr, sc)


def part_2_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 2."""
    return 0


if __name__ == "__main__":
    # Compute puzzle with example data
    example_data = _parse_input(EXAMPLE_INPUT)

    start = np.where(example_data == 'S')
    sr = start[0][0]
    sc = start[1][0]

    print(part_1_solution(example_data))

    # # Assert the example input results are as expected.
    assert part_1_solution(example_data) == EXAMPLE_OUTPUT_PART1
    # assert part_2_solution(example_data) == EXAMPLE_OUTPUT_PART2

    # Read puzzle input.
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
        data = _parse_input(f.read())

    # Print answers
    start_time_1 = time.time()
    print(f'\nPart 1: { part_1_solution(data) }')
    execution_time_1 = (time.time() - start_time_1)
    print(f'Part 1 execution time: {execution_time_1:.4f}')

    # start_time_2 = time.time()
    # print(f'\nPart 2: { part_2_solution(data) }')
    # execution_time_2 = (time.time() - start_time_2)
    # print(f'Part 2 execution time: {execution_time_2:.4f}')
