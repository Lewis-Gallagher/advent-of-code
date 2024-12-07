"""
Solution for Advent of Code 2024 day 06 - https://adventofcode.com/2024/day/06
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time
from copy import deepcopy

EXAMPLE_INPUT = '''\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
'''

EXAMPLE_OUTPUT_PART1 = 41
EXAMPLE_OUTPUT_PART2 = 0


def _parse_input(data: str) -> List[str]:
    """Parse input text file into usable data structure."""

    return [[i for i in line] for line in data.splitlines()]


def rotate_pointer(pointer: str) -> str:
    
    # Lazy if block but w/e
    if pointer == '>':
        pointer = 'v'
    elif pointer == 'v':
        pointer = '<'
    elif pointer == '<':
        pointer = '^'
    elif pointer == '^':
        pointer = '>'
        
    return pointer


def part_1_solution(grid: List[str]) -> Any:
    """Compute solution to puzzle part 1."""

    start = [[(ix,iy), i] for ix, row in enumerate(grid) for iy, i in enumerate(row) if i in '<>^v'][0]
    r, c = start[0][0],  start[0][1]
    pointer = start[1]

    move_dict = {
        '>':(0,1),
        'v':(1,0),
        '<':(0,-1),
        '^':(-1,0)
    }

    while True:

        # Mark visited cell
        grid[r][c] = 'X'
        # Get directions based on current pointer state
        r_move, c_move = move_dict[pointer]
        
        # Check next move is in bounds
        if (0 <= r + r_move < len(grid)) and (0 <= c + c_move < len(grid[0])):
            # if blocked rorate pointer and move on
            if grid[r+r_move][c+c_move] == '#':
                pointer = rotate_pointer(pointer)
                continue

            # Otherwise move pointer
            r += r_move
            c += c_move

        else:
            return sum(i.count('X') for i in grid)
        

def part_2_solution(grid: List[str]) -> Any:
    """Compute solution to puzzle part 2."""

    # Add Xs to guard path
    part_1_solution(grid)
    # Find loops by checking if we visit an obstacle (or the new obstacle) more than once
    


    return 0


if __name__ == "__main__":
    # Compute puzzle with example data
    example_data = _parse_input(EXAMPLE_INPUT)
    # Assert the example input results are as expected.
    assert part_1_solution(deepcopy(example_data)) == EXAMPLE_OUTPUT_PART1
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
