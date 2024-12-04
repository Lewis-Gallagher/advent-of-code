"""
Solution for Advent of Code 2024 day 04 - https://adventofcode.com/2024/day/04
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time


EXAMPLE_INPUT = '''\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
'''

EXAMPLE_OUTPUT_PART1 = 18
EXAMPLE_OUTPUT_PART2 = 9


def _parse_input(data: str) -> List[str]:
    """Parse input text file into usable data structure."""

    return [[i for i in line] for line in data.splitlines()]


def part_1_solution(data: List[str]) -> int:
    """Compute solution to puzzle part 1."""

    word = 'XMAS'
    xmas_count = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    max_length = len(word)-1

    for row in range(len(data)):
        for col in range(len(data[0])):

            # Check for the start of the word
            if data[row][col] == word[0]:
                for row_move, col_move in directions:

                    # Check if the whole XMAS word will be out of bounds before starting
                    if (0 <= row + max_length * row_move < len(data)) and (0 <= col + max_length * col_move < len(data[0])):

                        # M is 1x the directions value, A is 2x the directions value, S is 3x the directions value
                        # E.g. right (0,1): M is (0,1), A is (0,2) and X is (0,3)
                        if data[row + row_move][col + col_move] ==  'M' and \
                            data[row + 2 * row_move][col + 2 * col_move] ==  'A' and \
                            data[row + 3 * row_move][col + 3 * col_move] ==  'S':
                            xmas_count+=1

    return xmas_count


def part_2_solution(data: List[str]) -> int:
    """Compute solution to puzzle part 2."""

    cross_counter = 0
    directions = [(-1, -1), (1, 1), (-1, 1), (1, -1)]

    # X should start 1 row and column inside the matrix to be in bounds
    for row in range(1, len(data)-1):
        for col in range(1, len(data[0])-1):

            # Look for A at the center of the X
            if data[row][col] == 'A':

                # Check both diagonals
                diag1 = [data[row + row_move][col + col_move] for row_move, col_move in directions[:2]]
                diag2 = [data[row + row_move][col + col_move] for row_move, col_move in directions[2:]]

                # Diagonals must be S->M or M->S. Sort lists to ignore orientation
                if sorted(diag1) == ['M','S'] and sorted(diag2) == ['M', 'S']:
                    cross_counter+=1

    return cross_counter


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