import os
from collections import defaultdict
from pathlib import Path
from itertools import combinations
import sys
from collections import deque

rootpath = Path(__file__).parent
filepath = os.path.join(rootpath, 'input.txt')


num_rows = 71
num_cols = 71
part1_num = 1024

with open(filepath, 'r') as file:
   lines = list(map(str.strip, file.readlines()))

blocks = [tuple(map(int, line.split(",")))[::-1] for line in lines]


def count_steps(num_blocks: int) -> int:
   # state = r, c, dist
   queue = deque([(0, 0, 0)])
   seen = set((0, 0))
   while queue:
      r, c, d = queue.popleft()
      if (r, c) in seen:
         continue
      seen.add((r, c))
      if r == num_rows - 1 and c == num_cols - 1:
         return d
      for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
         nr, nc = r + dr, c + dc
         if (
                 0 <= nr < num_rows
                 and 0 <= nc < num_cols
                 and (nr, nc) not in blocks[:num_blocks]
         ):
            queue.append((nr, nc, d + 1))
   return -1


part1 = count_steps(part1_num)
print(f"Part 1: {part1}")

lo, hi = 0, len(blocks) - 1
while lo < hi:
   mid = (lo + hi) // 2
   if count_steps(mid + 1) != -1:
      lo = mid + 1
   else:
      hi = mid

part2 = ",".join(str(x) for x in blocks[lo][::-1])
print(f"Part 2: {part2}")
