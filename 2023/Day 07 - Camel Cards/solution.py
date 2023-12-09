"""
Solution for Advent of Code 2023 day 07 - https://adventofcode.com/2023/day/07
Author: Lewis Gallagher
"""

import os
from typing import List, Any
import time
from collections import Counter, defaultdict


EXAMPLE_INPUT = '''\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
'''

EXAMPLE_OUTPUT_PART1 = 6440
EXAMPLE_OUTPUT_PART2 = 5905


def _parse_input(data: str) -> List[str]:
    """Parse input text file into usable data structure."""

    return [[hand for hand in line.split()] for line in data.splitlines()]


def get_hand_type(hand: str) -> bool:
    '''
    Takes a hand of cards and counts the number of items. Score the hand based on the counter.
    '''

    counts = [val for _, val in Counter(hand).most_common()]

    if counts == [5]:
        return 7    # Five of a kind

    if counts == [4,1]:
        return 6    # Four of a kind

    if counts == [3,2]:
        return 5    # Full house
    
    if counts == [3,1,1]:
        return 4    # Three of a kind

    if counts == [2,2,1]:
        return 3    # Two pair
    
    if counts == [2,1,1,1]:
        return 2    # One pair
    
    if counts == [1,1,1,1,1]:
        return 1    # High card
    

def replacements(hand: str) -> List[str]:
    '''
    Takes a hand of cards and recursively calculates all permutations where J can equal 123456789TQKA.
    '''

    if hand == '':
        return ['']
    
    return [
        i + r 
        for i in ('123456789TQKA' if hand[0] == 'J' else hand[0]) 
        for r in replacements(hand[1:])
        ]


def classify(hand: str) -> int:
    '''
    Takes a hand of cards and finds the maximum hand type for that card by mapping the get_hand_type function over each output of the recursive replacement function.
    '''

    return max(map(get_hand_type, replacements(hand)))


def part_1_solution(data: List[str]) -> int:
    """Compute solution to puzzle part 1."""

    card_map = {'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}
    hands = {hand[0]: hand[1] for hand in data}

    winnings = list()
    results = defaultdict(list)

    # Calculate the values and type of hand for each hand.
    for hand, bet in hands.items():
        x = [card_map.get(val) for val in hand]
        type = get_hand_type(x)
        results[hand].append(x)
        results[hand].append(type)
        
    # Resolve the ties by ordering by hand type, then card values.
    results = dict(sorted(results.items(), key=lambda v: (v[1][1], v[1][0])))

    # Multiply rank by bet.
    for rank, (k,v) in enumerate(results.items(), start = 1):
        win = int(hands[k])*rank
        winnings.append(win)

    return sum(winnings)


def part_2_solution(data: List[str]) -> Any:
    """Compute solution to puzzle part 2."""

    # In part 2 joker is the weakest card.
    card_map = {'A':13, 'K':12, 'Q':11, 'J':0, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}
    hands = {hand[0]: hand[1] for hand in data}

    winnings = list()
    results = defaultdict(list)

    # Calculate the values and type of hand for each hand.
    for hand, bet in hands.items():
        x = [card_map.get(val) for val in hand]
        type = classify(hand)
        results[hand].append(x)
        results[hand].append(type)
        
    # Resolve the ties by ordering by hand type, then card values.
    results = dict(sorted(results.items(), key=lambda v: (v[1][1], v[1][0])))

    # Multiply rank by bet.
    for rank, (k,v) in enumerate(results.items(), start = 1):
        win = int(hands[k])*rank
        winnings.append(win)

    return sum(winnings)


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