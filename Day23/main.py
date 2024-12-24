import os
from collections import defaultdict
from pathlib import Path
from itertools import combinations

rootpath = Path(__file__).parent
filepath = os.path.join(rootpath, 'input.txt')

with open(filepath, 'r') as file:
   pairs = [l.strip().split('-') for l in file.readlines()]

conns = defaultdict(set)
for a, b in pairs:
   conns[a].add(b)
   conns[b].add(a)

triples = set()
for conn in conns:
   for neighbor in conns[conn]:
      for nn in conns[neighbor]:
         if conn in conns[nn]:
            triples.add(tuple(sorted([conn, neighbor, nn])))

part1 = len([t for t in triples if any(x.startswith("t") for x in t)])
print(f'Part 1: {part1}')

passwords = set()


def build_set(conn: str, group: set[str]) -> None:
   password = ','.join(sorted(group))
   if password in passwords: return
   passwords.add(password)
   for neighbor in conns[conn]:
      if neighbor in group: continue
      if any(neighbor not in conns[node] for node in group): continue
      build_set(neighbor, {*group, neighbor})


groups = set()
for conn in conns:
   build_set(conn, {conn})
part2 = max(passwords, key=len)
print(f'Part 2: {part2}')