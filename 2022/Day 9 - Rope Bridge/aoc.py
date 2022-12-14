"""
Solution for Advent of Code 2022 day 9 - https://adventofcode.com/2022/day/9
"""


import os
from typing import List, Any
import timeit


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


def are_adjacent(head: List[int], tail: List[int]) -> None:
    """Returns true if head xy position is adjacent to tail xy position"""

    xdist = abs(head[0] - tail[0])
    ydist = abs(head[1] - tail[1])
    if (xdist == 0 or xdist == 1) and (ydist == 1 or ydist == 0):
        return True


def move_head(move: int, head: int) -> List[int]:
    """Updates head position by 1 depending on direction."""

    if move == 'R':
        head[0] += 1
    elif move == 'L':
        head[0] -= 1
    elif move == 'U':
        head[1] += 1
    elif move == 'D':
        head[1] -= 1

    return head


def move_tail(move: str, head: int, tail: int) -> List[int]:
    """Updates tail position relative to head position."""

    if move == 'U':
        tail[0] += head[0] - tail[0]
        tail[1] += head[1] - tail[1] -1

    elif move == 'D':
        tail[0] += head[0] - tail[0]
        tail[1] += head[1] - tail[1] +1

    elif move == 'R':
        tail[0] += head[0] - tail[0] -1
        tail[1] += head[1] - tail[1]

    elif move == 'L':
        tail[0] += head[0] - tail[0] +1
        tail[1] += head[1] - tail[1]

    return tail


def part_1_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 1."""
    
    head = [0,0]
    tail = [0,0]
    visited = []

    # Iterate over moves.
    for move, count in data:
        # Move head one count at a time.
        for _ in range(int(count)):
            head = move_head(move, head)
            
            # Check if tail is still adjacent.
            if not are_adjacent(head, tail):
                tail = move_tail(move, head, tail)

            # Append tail coordinates to list of visited coordinates.
            visited.append(list(tail))
            
    # Return the length of a Set of coordinates to get unique values.
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

    # Print answers
    print(f'Part 1: { part_1_solution(data=data) }')
    # print(f'Part 2: { part_2_solution(data=data) }')
    print(timeit.timeit())