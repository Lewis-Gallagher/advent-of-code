"""
Solution for Advent of Code 2023 day 05 - https://adventofcode.com/2023/day/05
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time


EXAMPLE_INPUT = '''\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48    

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''

EXAMPLE_OUTPUT_PART1 = 35
EXAMPLE_OUTPUT_PART2 = 0


def _parse_input(data: str) -> tuple[List[int], List[int]]:
    """Parse input text file into usable data structure."""
    
    seeds, *maps = data.split('\n\n')
    seeds = list(map(int, seeds.split(':')[1].split()))
    maps = [[list(map(int, j.split())) for j in i.splitlines()[1:]] for i in maps]

    return seeds, maps

def part_1_solution(source: List[int], maps: List[int]) -> Any:
    """Compute solution to puzzle part 1."""

    for m in maps:

        dest = []   # New list for each new category.

        for num in source:
            for d, s, r in m:
                # Check if source in range. Apply the offset to the source, which equals the difference between the destination and source values.
                if num in range(s, s+r):
                    dest_val = num + (d - s)
                    dest.append(dest_val) 
                    break

            # If the source isn't in the range, the destination value won't change.
            else:
                dest.append(num)
        
        # The desintation vals from this category become source vals for the next category map
        source = dest

    return min(dest)


def part_2_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 2."""
    return 0


if __name__ == "__main__":
    # Compute puzzle with example data
    example_seeds, example_maps = _parse_input(EXAMPLE_INPUT)

    # Assert the example input results are as expected.
    assert part_1_solution(example_seeds, example_maps) == EXAMPLE_OUTPUT_PART1
    # assert part_2_solution(example_data) == EXAMPLE_OUTPUT_PART2

    # Read puzzle input.
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
        seeds, maps = _parse_input(f.read())

    # Print answers
    start_time_1 = time.time()
    print(f'\nPart 1: { part_1_solution(seeds, maps) }')
    execution_time_1 = (time.time() - start_time_1)
    print(f'Part 1 execution time: {execution_time_1:.4f}')

    # start_time_2 = time.time()
    # print(f'\nPart 2: { part_2_solution(data) }')
    # execution_time_2 = (time.time() - start_time_2)
    # print(f'Part 2 execution time: {execution_time_2:.4f}')
