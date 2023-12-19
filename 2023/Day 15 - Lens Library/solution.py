"""
Solution for Advent of Code 2023 day 15 - https://adventofcode.com/2023/day/15
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time
import re

EXAMPLE_INPUT = '''\
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
'''

EXAMPLE_OUTPUT_PART1 = 1320
EXAMPLE_OUTPUT_PART2 = 145


def _parse_input(data: str) -> List[str]:
    """Parse input text file into usable data structure."""

    return [i.strip() for i in data.split(',')]


def hash(s: str) -> int:
    """Takes a string of ASCII characters and returns the total hash value of the string."""

    h = 0
    for ch in s:
        h += ord(ch) 
        h *= 17
        h %= 256

    return h


def fill_boxes(strings: List[str]) -> dict[int, List[Any]]:
        
    boxes = {i:[] for i in range(0,256)}

    for s in strings:
        # label - symbol - focal length
        m = re.match("([a-zA-Z]+)([-=])([0-9]?)", s)
        label = m.group(1)
        focal = m.group(3)

        h = hash(label)

        if m.group(2) == '-':

            # Remove if the lens is in the box.
            for n, vals in enumerate(boxes[h]):
                if vals[0] == label:
                    boxes[h].pop(n)
                    break
            
        elif m.group(2) == '=':
            
            # Add to the box If the box is empty.
            if len(boxes[h]) == 0:
                boxes[h].append([label, int(focal)])
                
            # The box isn't empty - check if the box contains a lens with that label.
            else:
                for vals in boxes[h]:
                    # Found. Update the focal length.
                    if vals[0] == label:
                        vals[1] = int(focal)
                        break
                
                # Not found. The lens isn't in the box, so append it.
                else:
                    boxes[h].append([label, int(focal)])

    return boxes
    

def part_1_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 1."""

    total = 0
    for s in data:
        total += hash(s)
    
    return total


def part_2_solution(strings: List[str]) -> int:
    """Compute solution to puzzle part 2."""

    boxes = fill_boxes(strings)

    total = 0

    # We only want to iterate over unique labels.
    labels = set()
    for s in strings:
        labels.add(re.match("([a-zA-Z]+)", s).group())

    # Assign power to each lens.
    for lab in labels:
        power1 = 0
        power2 = 0
        power3 = 0

        for b in boxes:
            for n, val in enumerate(boxes[b], start = 1):
                if lab in val:
                    power1 = 1+b
                    power2 = n
                    power3 = val[1]
        
        total += power1*power2*power3
        
    return total

if __name__ == "__main__":
    # Compute puzzle with example data
    example_data = _parse_input(EXAMPLE_INPUT)

    # Assert the example input results are as expected.
    assert part_1_solution(example_data) == EXAMPLE_OUTPUT_PART1
    assert part_2_solution(example_data) == EXAMPLE_OUTPUT_PART2

    # Read puzzle input.
    with open(os.path.join(os.path.dirname(__file__), "input"), "r", encoding="utf-8") as f:
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