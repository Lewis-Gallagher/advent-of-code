"""
Solution for Advent of Code 2022 day 2 - https://adventofcode.com/2022/day/2
"""

import os
from typing import List, Any
import time


EXAMPLE_INPUT = '''\
A Y
B X
C Z'''

EXAMPLE_OUTPUT_PART1 = 15
EXAMPLE_OUTPUT_PART2 = 12




def _parse_input(data: List[str]) -> List[str]:
    """Parse input text file into usable data structure."""

    game = [[i for i in round.split()] for round in data.splitlines()]
    return game


def part_1_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 1."""
    
    # Create dict for my moves.
    scores = {'X':1, 'Y':2, 'Z':3}

    # All possible outcomes (0=loss, 3=draw, 6=win).
    outcomes = {
        'A':{'X':3, 'Y':6, 'Z':0}, # Rock
        'B':{'X':0, 'Y':3, 'Z':6}, # Paper
        'C':{'X':6, 'Y':0, 'Z':3}, # Scissors
        }

    return sum([scores[play[1]] + outcomes[play[0]][play[1]] for play in data])


def part_2_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 2.
    Now the second column tells us what outcome we need, not what to play. X=loss, Y=draw, Z=win.
    """

    # Create dict for my moves (same as part 1).   
    scores = {'X':1, 'Y':2, 'Z':3}

    # Dict for instructions (lose/draw/win)
    instructions = {'X':0, 'Y':3, 'Z':6}

    # All possible outcomes now that X=win, Y=draw, Z=win (0=loss, 3=draw, 6=win).
    outcomes = {
        'A':{0:'Z', 3:'X', 6:'Y'}, # Rock
        'B':{0:'X', 3:'Y', 6:'Z'}, # Paper
        'C':{0:'Y', 3:'Z', 6:'X'}, # Scissors
        }

    return sum([instructions.get(play[1]) + scores[outcomes[play[0]][instructions.get(play[1])]] for play in data])


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
    # Print answers
    start_time_1 = time.time()
    print(f'\nPart 1: { part_1_solution(data) }')
    execution_time_1 = (time.time() - start_time_1)
    print(f'Part 1 execution time: {execution_time_1:.4f}')

    start_time_2 = time.time()
    print(f'\nPart 2: { part_2_solution(data) }')
    execution_time_2 = (time.time() - start_time_2)
    print(f'Part 2 execution time: {execution_time_1:.4f}')