"""
Solution for Advent of Code 2022 day 9 - https://adventofcode.com/2022/day/9
"""


import os
from typing import List, Any
import timeit


PART_1_EXAMPLE_INPUT = '''\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''

PART_2_EXAMPLE_INPUT = '''\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''


PART_1_EXAMPLE_OUTPUT = 13
PART_2_EXAMPLE_OUTPUT = 36


def _parse_input(data: str) -> List[tuple]:
    """Parse input text file into usable data structure."""
    data = [tuple(i.split()) for i in data.splitlines()]

    return data


def are_adjacent(head: List[int], tail: List[int]) -> bool:
    """Returns true if head xy position is adjacent to tail xy position"""

    xdist = abs(head[0] - tail[0])
    ydist = abs(head[1] - tail[1])
    if (xdist == 0 or xdist == 1) and (ydist == 1 or ydist == 0):
        return True


def move_head(move: List[int], head: List[int]) -> List[int]:
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


def distance(head: List[int], tail: List[int]) -> int:
    """Returns the x-axis distance and y-axis distance of two points."""

    xdist = head[0] - tail[0]
    ydist = head[1] - tail[1]

    return xdist, ydist

def move_tail(tail: List[int], xdist: int, ydist: int) -> List[int]:
    """Updates tail position based on distance to head position."""

    # If tail xdist or ydist is 2 away from head, reduce to 1 as we don't want them to overlap.
    if xdist == 2:
        xdist = 1
    elif xdist == -2:
        xdist = -1

    if ydist == 2:
        ydist = 1
    elif ydist == -2:
        ydist = -1

    # Update tail values.
    tail[0] += xdist
    tail[1] += ydist

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
            
            # Check if tail is still adjacent. Adjacent distances are 0 (same), 1(hori/vert) or 2(diag).
            xdist, ydist = distance(head, tail)

            # If distance is greater than 1 then move tail behind head.
            if abs(xdist) >= 2 or abs(ydist) >= 2:
                move_tail(tail, xdist, ydist)

            # Append tail coordinates to list of visited coordinates.
            visited.append(list(tail))

    # Return the length of a Set of coordinates to get unique values.
    return len(set(tuple(coord) for coord in visited))


def part_2_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 2."""

    rope = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
    visited = []

    # Iterate over moves.
    for move, count in data:

        # Move head postion one at a time.
        for _ in range(int(count)):
            rope[0] = move_head(move, rope[0])

            # Treat each pair of rope segements as a head and a tail.  
            for i in range(1, len(rope)):
                xdist, ydist = distance(rope[i-1], rope[i])

                # Check if they're adjacent and if not, move the tail segment.
                if abs(xdist) >= 2 or abs(ydist) >= 2:
                    rope[i] = move_tail(rope[i], xdist, ydist)

            # Append last index of rope coordinates to list of visited coordinates.
            visited.append(list(rope[-1]))

    # Return the length of a Set of coordinates to get unique values.
    return len(set(tuple(coord) for coord in visited))


if __name__ == "__main__":
    # Compute puzzle with example data
    example_data_part_1 = _parse_input(PART_1_EXAMPLE_INPUT)
    example_data_part_2 = _parse_input(PART_2_EXAMPLE_INPUT)

    # Assert the example input results are as expected.
    assert part_1_solution(example_data_part_1) == PART_1_EXAMPLE_OUTPUT
    assert part_2_solution(example_data_part_2) == PART_2_EXAMPLE_OUTPUT

    # Read puzzle input.
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
        data = _parse_input(f.read())

    # Print answers
    print(f'Part 1: { part_1_solution(data=data) }')
    print(f'Part 2: { part_2_solution(data=data) }')
    print(timeit.timeit())