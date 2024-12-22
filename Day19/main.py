import os
from collections import defaultdict
from pathlib import Path
from itertools import combinations
import sys
from functools import cache

rootpath = Path(__file__).parent
filepath = os.path.join(rootpath, 'input.txt')

with open(filepath, 'r') as file:
   options = file.readline().strip().split(", ")
   file.readline()
   targets = file.read().strip().split("\n")


@cache
def count_combinations(target: str) -> int:
    if target == "":
        return 1
    count = 0
    for option in options:
        if target.startswith(option):
            count += count_combinations(target[len(option) :])
    return count



combinations = [count_combinations(t) for t in targets]
part1 = len([c for c in combinations if c != 0])
print(f"Part 1: {part1}")

part2 = sum(combinations)
print(f"Part 2: {part2}")
