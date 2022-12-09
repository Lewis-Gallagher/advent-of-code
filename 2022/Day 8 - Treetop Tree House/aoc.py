"""
Solution for Advent of Code 2022 day 8 - https://adventofcode.com/2022/day/8
"""

import os
from typing import List
import numpy as np
import timeit


EXAMPLE_INPUT = '''\
30373
25512
65332
33549
35390'''

EXAMPLE_OUTPUT_PART1 = 21
EXAMPLE_OUTPUT_PART2 = 8


def _parse_input(data: str) -> List[int]:
    """Parse input text file into list of lists."""
    data = [[int(d) for d in row] for row in data.splitlines()]

    return data


def is_visible(i: int, j: int, data: List[int]) -> bool:
    """Takes (x,y) coordinates as input and checks if the tree at that location is visible from the left, right, top or bottom respectively."""

    tree = data[i][j]

    if tree > max(data[i][:j]) or \
        tree > max(data[i][j+1:]) or \
        tree > max([row[j] for row in data[:i]]) or \
        tree > max([row[j] for row in data[i+1:]]):
        return True


def get_visible_distance(tree: int, neighbours: List[int]) -> int:
    """Increment dist if neighbours are smaller than current tree"""
    dist = 0
    for neighbour in neighbours:
        if neighbour >= tree:
            dist += 1
            return dist
        else:
            dist += 1
    return dist


def part_1_solution(data: List[str]) -> int:
    """Compute solution to puzzle part 1."""
    
    # All tree edges are visible. Get sum of edges.
    visible = len(data) * 2 + len(data[0]) * 2 - 4

    # Iterate through inner rows and columns.
    for i in range(1, len(data)-1):
        for j in range(1, len(data[i])-1):
            if is_visible(i, j, data):
                visible += 1

    return visible


def part_2_solution(data: List[str]) -> int:
    """For each tree get it's neighbouring trees and find the distance it can see."""   
    scenic_scores = []

    # Begin iterating over trees and get tree neighbours.
    for i in range(len(data)):
        for j in range(len(data[i])):
            tree = data[i][j]
            left_neighbours = data[i][:j]
            right_neighbours = data[i][j+1:]
            up_neighbours = [row[j] for row in data[:i]]
            down_neighbours = [row[j] for row in data[i+1:]]

            # Reverse left and up neighbours because it needs to iterate over neighbours as if beginning at the nearest neighbour
            left, right, up, down = [
                get_visible_distance(tree, left_neighbours[::-1]),
                get_visible_distance(tree, right_neighbours),
                get_visible_distance(tree, up_neighbours[::-1]),
                get_visible_distance(tree, down_neighbours)
            ]

            # Multiply visible distances together to get the scenic score and return the maximum score.
            # I think there's some numpy.prod magic I can do here instead...
            scenic_score = 1
            for dist in [left, right, up, down]:
                scenic_score = scenic_score * dist
            scenic_scores.append(scenic_score)

    return max(scenic_scores)


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
    print(f'Part 1: { part_1_solution(data=data) }')
    print(f'Part 2: { part_2_solution(data=data) }')
    print(timeit.timeit())