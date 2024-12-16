import os
from collections import defaultdict
from pathlib import Path
from itertools import combinations

rootpath = Path(__file__).parent
filepath = os.path.join(rootpath, 'input.txt')

with open(filepath, 'r') as file:
    lines = list(map(str.strip, file.readlines()))

antenna = defaultdict(set)
num_rows = len(lines)
num_cols = len(lines[0])

for r, line in enumerate(lines):
    for c, val in enumerate(line):
        if val != ".":
            antenna[val].add((r, c))

antinodes1 = set()
antinodes2 = set()
for freq in antenna:
    for (r1, c1), (r2, c2) in combinations(antenna[freq], 2):
        antinodes1.add((2 * r1 - r2, 2 * c1 - c2))
        antinodes1.add((2 * r2 - r1, 2 * c2 - c1))
        dr = r2 - r1
        dc = c2 - c1
        r, c = r1, c1
        while 0 <= r < num_rows and 0 <= c < num_cols:
            antinodes2.add((r, c))
            r += dr
            c += dc
        r, c = r1, c1
        while 0 <= r < num_rows and 0 <= c < num_cols:
            antinodes2.add((r, c))
            r -= dr
            c -= dc

part1 = len([1 for r, c in antinodes1 if 0 <= r < num_rows and 0 <= c < num_cols])
print(f"Part 1: {part1}")

part2 = len(antinodes2)
print(f"Part 2: {part2}")
