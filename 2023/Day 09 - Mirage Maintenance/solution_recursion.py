from typing import List, Any
import os

def _parse_input(data: str) -> List[str]:
    """Parse input text file into usable data structure."""

    return [[int(j) for j in i.split()] for i in data.splitlines()]


def extrapolate_part1(array):
    '''
    Takes an array of integers and calculates the differences between all elements. Applies the function recursively on the new array and returns the next integer in the array.
    '''

    if all(i == 0 for i in array):
        return 0
    
    # zip(ar, ar[1:]) will generate all pairs in an array e.g. (1,2) (2,3) (3,4) (4,5) etc.
    deltas = [y - x for x, y in zip(array, array[1:])]
    diff = extrapolate_part1(deltas)
    return array[-1] + diff


def extrapolate_part2(array):
    if all(i == 0 for i in array):
        return 0
    
    deltas = [y - x for x, y in zip(array, array[1:])]
    diff = extrapolate_part2(deltas)
    return array[0] - diff


# Run

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="utf-8") as f:
    data = _parse_input(f.read())    

total1 = 0
total2 = 0

for line in data:
    total1 += extrapolate_part1(line)

print(f'Part 1: {total1}')

for line in data:
    total2 += extrapolate_part2(line)

print(f'Part 2: {total2}')