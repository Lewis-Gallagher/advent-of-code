"""
Solution for Advent of Code 2023 day 16 - https://adventofcode.com/2023/day/16
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time
import numpy as np
from collections import deque


EXAMPLE_INPUT = '''\
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
'''

EXAMPLE_OUTPUT_PART1 = 46
EXAMPLE_OUTPUT_PART2 = 0


def _parse_input(data: str) -> List[str]:
    """Parse input text file into usable data structure."""

    return np.array([line for line in data.splitlines()])

# {(mirror type, arrival direction), destination direction}
MIRROR_MAP = {
    ('\\', (0, -1)):    (1, 1),     # \ From North to East
    ('\\', (0, 1)):     (-1, -1),   # \ From South to West
    ('\\', (1, 0)):     (-1, -1),   # \ From East to North
    ('\\', (-1, 0)):    (1, 1),     # \ From West to South
    ('/',  (0, -1)):    (-1, 1),    # / From North to West
    ('/',  (0, 1)):     (1, -1),    # / From South to East
    ('/',  (1, 0)):     (-1, 1),    # / From East South
    ('/',  (-1, 0)):    (1, -1)     # / From West North
}

DIR_MAP = {
    'E': (0, 1),
    'W': (0, -1),
    'N': (-1, 0),
    'S': (1, 0)
}


def beam_travel(grid: List[str]):
    total = 0                       # Counter for energised cells.
    nrow = len(grid)                # Rows.
    ncol = len(grid[0])             # Columns.
    start = ((0,-1), DIR_MAP['E'])  # Start to the left of the grid traveling East.
    queue = deque(start)            # Initialise a queue.
    visited = set(start)            # Track visited cells.

    # Begin a BFS.
    # `queue` is a (position, direction) pair - we know that if we visit a coordinate in a direction we've already seen, to do nothing. It is possible to revisit a coordinate, but in a different direction.

    # If next position in queue is '.', continue in the same direction 1
    # If next position in queue is '-|' ask if we are approaching from a pointy end, if so continue in same direction 1. Otherwise split the beam.
    # If next position in queue is a mirror '/\' then go diagonally,

    while queue:
        # Get new position and direction.
        pos, drn = queue.pop()
        r, c = pos
        dr, dc = drn

        # Check if we've been here before in this direction.
        if (pos, drn) in visited:
            continue

        # Get new row and column position by position + directional movment.
        r += dr
        c += dc

        # Check for out of bounds.
        if (0 < r <= ncol) or (0 < c <= nrow):
            continue

        # Get next cells character.
        ch = grid[r][c]
        
        # Continue in the same direction. i.e. `.` or `|-` from the pointy ends.
        if ch == '.' or (ch == '|' and dr == 0) or (ch == '-' and dc == 0):
            queue.appendleft(pos, drn)
        
        # / Mirror. 
        # East <-> North, (0,1) <-> (-1,0)
        # West <-> South, (0,-1) <-> (1,0)
        # I.e. row = -dcol and col = -drow

        elif ch == '/':
            queue.appendleft((r, c), (-dc, -dr))

        elif ch == '//':
            
            


def part_1_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 1."""

    return 0


def part_2_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 2."""
    return 0


if __name__ == "__main__":
    # Compute puzzle with example data
    example_data = _parse_input(EXAMPLE_INPUT)
    print(example_data)
    # # Assert the example input results are as expected.
    # assert part_1_solution(example_data) == EXAMPLE_OUTPUT_PART1
    # assert part_2_solution(example_data) == EXAMPLE_OUTPUT_PART2

    # # Read puzzle input.
    # with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
    #     data = _parse_input(f.read())

    # # Print answers
    # start_time_1 = time.time()
    # print(f'\nPart 1: { part_1_solution(data) }')
    # execution_time_1 = (time.time() - start_time_1)
    # print(f'Part 1 execution time: {execution_time_1:.4f}')

    # start_time_2 = time.time()
    # print(f'\nPart 2: { part_2_solution(data) }')
    # execution_time_2 = (time.time() - start_time_2)
    # print(f'Part 2 execution time: {execution_time_2:.4f}')
