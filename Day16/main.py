import os
from collections import defaultdict
from pathlib import Path
from itertools import combinations
import sys
import heapq


rootpath = Path(__file__).parent
filepath = os.path.join(rootpath, 'input.txt')

with open(filepath, 'r') as file:
   grid = list(map(str.strip, file.readlines()))


for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == "S":
            start = (r, c)
            break
    else:
        continue
    break

# state = cost, r, c, dr, dc
queue = [(0, *start, 0, 1, [start])]
seen = {(*start, 0, 1)}
part1 = None
best_cost = float("inf")
points = set()

while queue:
    cost, r, c, dr, dc, path = heapq.heappop(queue)
    seen.add((r, c, dr, dc))
    if grid[r][c] == "E":
        if not part1:
            part1 = cost
        if cost <= best_cost:
            best_cost = cost
            for point in path:
                points.add(point)
        else:
            break
    if grid[r + dr][c + dc] != "#" and (r + dr, c + dc, dr, dc) not in seen:
        heapq.heappush(
            queue, (cost + 1, r + dr, c + dc, dr, dc, path + [(r + dr, c + dc)])
        )
    for ndr, ndc in [(-dc, dr), (dc, -dr)]:
        if (r, c, ndr, ndc) not in seen and grid[r + ndr][c + ndc] != "#":
            heapq.heappush(queue, (cost + 1000, r, c, ndr, ndc, list(path)))

print(f"Part 1: {part1}")
part2 = len(points)
print(f"Part 2: {part2}")
