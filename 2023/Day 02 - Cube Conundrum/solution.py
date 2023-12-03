"""
Solution for Advent of Code 2023 day 02 - https://adventofcode.com/2023/day/02
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time
import re
import numpy as np


EXAMPLE_INPUT = '''\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''

EXAMPLE_OUTPUT_PART1 = 8
EXAMPLE_OUTPUT_PART2 = 2286


def _parse_input(data: str) -> List[str]:
    """Parse input text file into usable data structure."""

    return [line for line in data.splitlines()]


def part_1_solution(data: List[str]) -> int:
    """Compute solution to puzzle part 1."""

    lookup = {'red':12, 'green':13, 'blue':14}
    possible_games = set()

    for game in data:

        # Seperate game and cubes.
        num, cubes = game.split(': ')

        num = int(num.split(' ')[-1])
        possible_games.add(num)

        # Seperate hands of cubes.
        hands = cubes.split('; ')

        # Get tupples of counts and colours.
        for h in hands:
            count_cols = re.findall(r"(\d+)\s(\w+)", h)

            # Check if the colour count exceeds the maximum.
            for c in count_cols:
                if int(c[0]) > lookup.get(c[1]):
                    possible_games.discard(num)

    return sum(possible_games)


def part_2_solution(data: List[str]) -> int:
    """Compute solution to puzzle part 2."""

    powers = []

    for game in data:

        # Initialise dict with required cube numbers.
        need_cubes = {'red':0, 'blue':0, 'green':0}

        # Seperate game and cubes.
        num, cubes = game.split(': ')
        num = int(num.split(' ')[-1])

        # Seperate hands of cubes.
        hands = cubes.split('; ')

        # Get tupples of counts and colours.
        for h in hands:
            count_cols = re.findall(r"(\d+)\s(\w+)", h)

            # For each pair update the need_cubes dict if the value is larger.
            for c in count_cols:
                if int(c[0]) > need_cubes.get(c[1]):
                    need_cubes[c[1]] = int(c[0])

        # Product of a list containing zeros will be zero. Filter them.
        to_power = [i for i in list(need_cubes.values()) if i != 0]
        powers.append(np.prod(to_power))

    return sum(powers)


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