import os
from collections import defaultdict
from pathlib import Path
from itertools import combinations
from collections import deque

rootpath = Path(__file__).parent
filepath = os.path.join(rootpath, 'input.txt')

with open(filepath, 'r') as file:
    grid = list(map(str.strip, file.readlines()))

num_rows = len(grid)
num_cols = len(grid[0])

regions = []
seen = set()

for r in range(num_rows):
    for c in range(num_cols):
        if (r, c) in seen:
            continue
        region = set()
        queue = deque([(r, c)])
        while queue:
            rr, cc = queue.popleft()
            region.add((rr, cc))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = rr + dr, cc + dc
                if (nr, nc) not in seen and 0 <= nr < num_rows and 0 <= nc < num_cols and grid[nr][nc] == grid[rr][cc]:
                    queue.append((rr + dr, cc + dc))
                    seen.add((nr, nc))
        regions.append(region)

def perimeter(region: set[tuple[int]]):
    total = 0
    for r, c in region:
        num_neighbors = len([1 for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)) if (dr+r, dc+c) in region])
        total += 4 - num_neighbors
    return total


def sides(region: set[tuple[int]]) -> int:
    up, down, left, right = (set() for _ in range(4))
    for r, c in region:
        if (r - 1, c) not in region:
            up.add((r, c))
        if (r + 1, c) not in region:
            down.add((r, c))
        if (r, c - 1) not in region:
            left.add((r, c))
        if (r, c + 1) not in region:
            right.add((r, c))

    count = 0
    for r, c in up:
        if (r, c) in left:
            count += 1
        if (r, c) in right:
            count += 1
        if (r - 1, c - 1) in right and (r, c) not in left:
            count += 1
        if (r - 1, c + 1) in left and (r, c) not in right:
            count += 1

    for r, c in down:
        if (r, c) in left:
            count += 1
        if (r, c) in right:
            count += 1
        if (r + 1, c - 1) in right and (r, c) not in left:
            count += 1
        if (r + 1, c + 1) in left and (r, c) not in right:
            count += 1

    return count



part1 = sum(len(r) * perimeter(r) for r in regions)
print(part1)

part2 = sum(len(r) * sides(r) for r in regions)
print(part2)
