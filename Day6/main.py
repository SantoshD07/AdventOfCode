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
patrol_map = defaultdict(set)

for r, row in enumerate(lines):
    for c, val in enumerate(row):
        if val == '^':
            start_r, start_c = r, c
        obstacle_map[val].add((r, c))

print(obstacle_map)


def part1():
    part1 = 1
    maxr = len(lines)
    maxc = len(lines[0]) - 1
    r, c = start_r, start_c
    print(start_r+1, start_c+1)
    dr, dc = -1, 0

    while (r <maxr and c <maxc and r>0 and c>0):
        r, c = r + dr, c + dc

        if (r,c) not in obstacle_map['#']:
            if (r,c) not in patrol_map['X']:
                patrol_map['X'].add((r,c))
            print(r+1, c+1)
        else:
            print("Change direction", r, c)
            r, c = r - dr, c-dc
            if (dr, dc) == (-1, 0):
                dr, dc = 0, 1
            elif (dr, dc) == (0, 1):
                dr, dc = 1, 0
            elif (dr, dc) == (1, 0):
                dr, dc = 0, -1
            elif (dr, dc) == (0, -1):
                dr, dc = -1, 0


    print(part1+len(patrol_map['X']))


if __name__ == '__main__':
    part1()
