import os
from collections import defaultdict
from pathlib import Path
from itertools import combinations

rootpath = Path(__file__).parent
filepath = os.path.join(rootpath, 'input.txt')

with open(filepath, 'r') as file:
   numbers = list(map(int, file.readlines()))

def next_num(x: int) -> int:
    x ^= (x * 64) % 16777216
    x ^= (x // 32) % 16777216
    x ^= (x * 2048) % 16777216
    return x

part1 = 0
seq_totals = defaultdict(int)
for num in numbers:
    seen = set()
    outputs = [(num := next_num(num)) % 10 for _ in range(2000)]
    part1 += num
    diffs = [y - x for x, y in zip(outputs, outputs[1:])]
    for n, *seq in zip(outputs[4:], diffs, diffs[1:], diffs[2:], diffs[3:]):
        seq = tuple(seq)
        if seq in seen: continue
        seen.add(seq)
        seq_totals[seq] += n

print(f'Part 1: {part1}')

part2 = seq_totals[max(seq_totals, key=seq_totals.get)]
print(f'Part 2: {part2}')