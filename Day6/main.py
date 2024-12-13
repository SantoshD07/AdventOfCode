import os
from collections import defaultdict
from pathlib import Path


def read_file():
    rootpath = Path(__file__).parent
    filepath = os.path.join(rootpath, 'input.txt')

    with open(filepath, 'r') as file:
        return file.readlines()


lines = read_file()
obstacle_map = defaultdict(set)
patrol_map = set()

for r, row in enumerate(lines):
    for c, val in enumerate(row):
        if val == '^':
            start_r, start_c = r, c
        obstacle_map[val].add((r, c))

print(obstacle_map)


def part1():
    part1 = 1
    maxr = len(lines)
    maxc = len(lines[0])
    r, c = start_r, start_c
    dr, dc = -1, 0

    while True:
        patrol_map.add((r, c))
        if not (0 <= r + dr < maxr and 0 <= c + dc < maxc):
            break
        elif (r + dr, c + dc) in obstacle_map['#']:
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc

    print(len(patrol_map))


if __name__ == '__main__':
    part1()
