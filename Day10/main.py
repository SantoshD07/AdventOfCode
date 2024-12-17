import os
from collections import defaultdict
from pathlib import Path
from itertools import combinations
from collections import deque

rootpath = Path(__file__).parent
filepath = os.path.join(rootpath, 'input.txt')

with open(filepath, 'r') as file:
    grid = [list(map(int, line.strip())) for line in file.readlines()]

cols = len(grid[0])
rows = len(grid)

zeros = [(r, c) for r, row in enumerate(grid) for c, val in enumerate(row) if val == 0]

print(grid)
def count_trails(r, c):
    queue = deque([(r, c)])
    temp = set()
    count = 0
    while queue:
        print(queue)
        r, c = queue.popleft()
        if grid[r][c] == 9:
            temp.add((r, c))
            count +=1
            continue
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[r][c] + 1 == grid[nr][nc]:
                queue.append((nr,nc))

    return temp, count

part1, part2 = 0,0
for start in zeros:
    trails, paths = count_trails(*start)
    part1 += trails
    part2 += paths

print(part1, part2)