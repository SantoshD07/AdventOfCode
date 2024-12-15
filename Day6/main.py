import os
from collections import defaultdict
from pathlib import Path


# def read_file():
#     rootpath = Path(__file__).parent
#     filepath = os.path.join(rootpath, 'input.txt')
#
#     with open(filepath, 'r') as file:
#         return file.readlines()
#
#
# lines = read_file()
# for line in lines:
#     grid = list(map(list, map(str.strip, line)))
#
# #print(grid)
# obstacle_map = defaultdict(set)
# patrol_map = set()
#
# for r, row in enumerate(lines):
#     for c, val in enumerate(row):
#         if val == '^':
#             start_r, start_c = r, c
#         obstacle_map[val].add((r, c))
#
# #print(obstacle_map)
#
#
# def part1():
#     part1 = 1
#     maxr = len(lines)
#     maxc = len(lines[0])
#     r, c = start_r, start_c
#     dr, dc = -1, 0
#
#     while True:
#         patrol_map.add((r, c))
#         if not (0 <= r + dr < maxr and 0 <= c + dc < maxc):
#             break
#         elif (r + dr, c + dc) in obstacle_map['#']:
#             dc, dr = -dr, dc
#         else:
#             r += dr
#             c += dc
#
#     #print(patrol_map['X'])
#
# maxr, maxc = len(grid), len(grid[0])
#
#
# def loop_check():
#
#     r, c = start_r, start_c
#     dr, dc = -1, 0
#     patrol_map = set()
#
#     while True:
#         if(r,c,dr,dc) in patrol_map:
#             return True
#         patrol_map.add((r, c, dr, dc))
#         if not (0 <= r + dr < maxr and 0 <= c + dc < maxc):
#             return False
#         elif grid[r+dr][c+dc] == "#":
#             dc, dr = -dr, dc
#         else:
#             r += dr
#             c += dc
#
# def part2():
#     part2= 0
#     maxr, maxc = len(grid), len(grid[0])
#     for row_obj in range(maxr):
#         for col_obj in range(maxc):
#             if grid[row_obj][col_obj] != '.':
#                 continue
#             grid[row_obj][col_obj] = '#'
#             if loop_check():
#                 print("hello")
#                 part2 +=1
#             grid[row_obj][col_obj] = '.'
#
#     print(part2)


import sys


def get_start():
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == "^":
                return (r, c)


rootpath = Path(__file__).parent
filepath = os.path.join(rootpath, 'input.txt')

with open(filepath, "r") as f:
    grid = list(map(list, map(str.strip, f.readlines())))

num_rows = len(grid)
num_cols = len(grid[0])

r, c = get_start()
dr, dc = -1, 0
visited = set()

while True:
    visited.add((r, c))
    if not (0 <= r + dr < num_rows and 0 <= c + dc < num_cols):
        break
    if grid[r + dr][c + dc] == "#":
        dc, dr = -dr, dc
    else:
        r += dr
        c += dc

print(f"Part 1: {len(visited)}")


start_r, start_c = get_start()


def check_for_loop():
    r, c = start_r, start_c
    dr, dc = -1, 0
    visited = set()

    while True:
        if (r, c, dr, dc) in visited:
            return True
        visited.add((r, c, dr, dc))
        if not (0 <= r + dr < num_rows and 0 <= c + dc < num_cols):
            return False
        if grid[r + dr][c + dc] == "#":
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc


part2 = 0
for ro in range(num_rows):
    for co in range(num_cols):
        if grid[ro][co] != ".":
            continue
        grid[ro][co] = "#"
        if check_for_loop():
            part2 += 1
        grid[ro][co] = "."

print(f"Part 2: {part2}")


# if __name__ == '__main__':
#     part2()
