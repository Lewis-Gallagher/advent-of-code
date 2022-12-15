"""
Solution for Advent of Code 2022 day 10 - https://adventofcode.com/2022/day/10
"""

import os
from typing import List, Any
import timeit


EXAMPLE_INPUT = '''\
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop'''


EXAMPLE_OUTPUT_PART1 = 13140


def _parse_input(data: str) -> List[str]:
    """Parse input text file into usable data structure."""

    return [i.split() for i in data.splitlines()]


def part_1_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 1."""
    
    # Count cycles and initialise X signal value.
    X = 1
    signals = []

    for action in data:        
        # addx takes 2 cycles (range(2)) and updates X at the end.
        if action[0] == 'addx':
            for _ in range(2):
                signals.append(X)
            X += int(action[1])

        # noop takes 1 cycle and doesn't alter X so append X as is.
        elif action[0] == 'noop':
            signals.append(X)
        
    # Return i-1 because cycles begin at 1.
    return signals, sum([signals[i-1] * i for i in range(20,len(signals), 40)])


def part_2_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 2."""

    # Get list of signals from part 1.
    sprite_locs = part_1_solution(data)[0]
    # Split signas into list of lists equal to size of screen.
    sprite_locs = [sprite_locs[i:i + 40] for i in range(0, len(sprite_locs), 40)]
    # Make empty screen filled with '.'.
    screen = [[ '.' for _ in range(40)] for j in range(6)]

    for i in range(len(sprite_locs)):
        for j in range(len(sprite_locs[i])):
            # Make sprite range
            sprite_pos = [sprite_locs[i][j]-1, sprite_locs[i][j], sprite_locs[i][j]+1]

            # If the pixel being drawn by the screen is within the sprite range then fill pixel.
            if j in sprite_pos:
                screen[i][j] = '#'

    return screen


if __name__ == "__main__":
    # Compute puzzle with example data
    example_data = _parse_input(EXAMPLE_INPUT)

    # Assert the example input results are as expected.
    assert part_1_solution(example_data)[1] == EXAMPLE_OUTPUT_PART1

    # Read puzzle input.
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
        data = _parse_input(f.read())

    # # Print answers
    print(f'Part 1: { part_1_solution(data=data)[1] }')
    print(f'Part 2: { part_2_solution(data=data) }')
    print(timeit.timeit())