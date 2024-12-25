import os
from collections import defaultdict
from pathlib import Path
from itertools import combinations

rootpath = Path(__file__).parent
filepath = os.path.join(rootpath, 'input.txt')

with open(filepath, 'r') as file:
   lines = list(x.strip() for x in file.readlines() if x.strip() != '')

locks, keys = [], []
for i in range(len(lines) // 7):
    if lines[7*i] == '#####':
        # lock
        lock = [0, 0, 0, 0, 0]
        for j in range(1, 7):
            for k, char in enumerate(lines[7*i + j]):
                if char == '#':
                    lock[k] += 1
        locks.append(tuple(lock))
    else:
        # key
        key = [5, 5, 5, 5, 5]
        for j in range(1, 7):
            for k, char in enumerate(lines[7 * i + j]):
                if char == '.':
                    key[k] -= 1
        keys.append(tuple(key))

pairs = 0
for l in locks:
    for k in keys:
        if all(l[i] + k[i] <= 5 for i in range(5)):
            pairs += 1
print(pairs)