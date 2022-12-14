"""
Solution for Advent of Code 2022 day 9 - https://adventofcode.com/2022/day/9
"""


import os
from typing import List, Any
import timeit
import numpy as np
from itertools import groupby
from operator import itemgetter


EXAMPLE_INPUT = '''\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''


EXAMPLE_OUTPUT_PART1 = 13
EXAMPLE_OUTPUT_PART2 = 0


def _parse_input(data: str) -> List[tuple]:
    """Parse input text file into usable data structure."""
    data = [tuple(i.split()) for i in data.splitlines()]

    return data


def adjacent(a: List[int], b: List[int]) -> bool:
    """Returns true of a and b are adjacent"""
    # Vertically adjacent
    if a[0] == b[0] and abs(a[1] - b[1]) == 1:
        return True

    # Horizontally adjacent
    elif a[1] == b[1] and abs(a[0] - b[0]) == 1:
        return True

    # Diagonally adjacent (Thanks Niki!)
    elif abs(a[0] - b[0]) == 1 and abs(a[1] - b[1]) == 1:
        return True

    # A and B in the same position
    elif abs(a[0] - b[0]) == 0 and abs(a[1] - b[1]) == 0:
        return True

    else:
        return False 


def part_1_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 1."""
    
    head = [0,0]
    tail = [0,0]
    visited = []
    for m, n in data:
        if m == "R":
            # Move head one space at a time
            for _ in range(int(n)):
                head[0] += 1
                # If head not touching tail - otherwise tail stays still
                if not adjacent(head, tail):
                    # If head is on a different y value
                    if head[1] != tail[1]:
                        # Move tail x to head pos minus 1 (when going right) and align y (diagonal move)
                        tail[0] = head[0] - 1
                        tail[1] = head[1]
                    # On same y, move tail to one behind head on x
                    else:
                        tail[0] = head[0] - 1
                visited.append(list(tail))

        elif m == "L":
            for _ in range(int(n)):
                head[0] -= 1
                # If head not touching tail - otherwise tail stays still
                if not adjacent(head, tail):
                    # If head is on a different y value
                    if head[1] != tail[1]:
                        # Move tail x to head pos minus 1 (when going right) and align y (diagonal move)
                        tail[0] = head[0] + 1
                        tail[1] = head[1]
                    # On same y, move tail to one behind head on x
                    else:
                        tail[0] = head[0] + 1
                visited.append(list(tail))

        elif m == "U":
            for _ in range(int(n)):
                head[1] += 1
                # If head not touching tail - otherwise tail stays still
                if not adjacent(head, tail):
                    # If head is on a different y value
                    if head[1] != tail[1]:
                        # Move tail x to head pos minus 1 (when going right) and align y (diagonal move)
                        tail[1] = head[1] - 1
                        tail[0] = head[0]
                    # On same y, move tail to one behind head on x
                    else:
                        tail[1] = head[1] - 1
                visited.append(list(tail))

        elif m == "D":
            for _ in range(int(n)):
                head[1] -= 1
                # If head not touching tail - otherwise tail stays still
                if not adjacent(head, tail):
                    # If head is on a different y value
                    if head[1] != tail[1]:
                        # Move tail x to head pos minus 1 (when going right) and align y (diagonal move)
                        tail[1] = head[1] + 1
                        tail[0] = head[0]
                    # On same y, move tail to one behind head on x
                    else:
                        tail[1] = head[1] + 1
                visited.append(list(tail))

    return len(set(tuple(coord) for coord in visited))


def part_2_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 2."""
    return 0


if __name__ == "__main__":
    # Compute puzzle with example data
    example_data = _parse_input(EXAMPLE_INPUT)
    # Assert the example input results are as expected.
    assert part_1_solution(example_data) == EXAMPLE_OUTPUT_PART1
    # assert part_2_solution(example_data) == EXAMPLE_OUTPUT_PART2

    # Read puzzle input.
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
        data = _parse_input(f.read())

    # # Print answers
    print(f'Part 1: { part_1_solution(data=data) }')
    # print(f'Part 2: { part_2_solution(data=data) }')
    print(timeit.timeit())