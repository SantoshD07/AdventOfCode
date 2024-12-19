import os
from collections import defaultdict
from pathlib import Path
from itertools import combinations

rootpath = Path(__file__).parent
filepath = os.path.join(rootpath, 'input.txt')

with open(filepath, 'r') as file:
   grid_str, moves = file.read().split("\n\n")
grid = [list(row) for row in grid_str.split("\n")]

moves = moves.replace("\n", "")

for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == "@":
            break
    else:
        continue
    break

move_map = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
for move in moves:
    dr, dc = move_map[move]
    rr, cc = r + dr, c + dc
    do_move = True
    while True:
        if grid[rr][cc] == "#":
            do_move = False
            break
        if grid[rr][cc] == ".":
            break
        if grid[rr][cc] == "O":
            rr, cc = rr + dr, cc + dc
        else:
            assert False

    if not do_move:
        continue
    grid[r][c] = "."
    r, c = r + dr, c + dc
    if grid[r][c] == "O":
        grid[rr][cc] = "O"
    grid[r][c] = "@"

part1 = sum(
    r * 100 + c for r, row in enumerate(grid) for c, val in enumerate(row) if val == "O"
)
print(f"Part 1: {part1}")

grid_map = {"#": "##", "O": "[]", ".": "..", "@": "@."}

with open(filepath, 'r') as file:
    grid_str, moves = file.read().split("\n\n")

grid = []
for row in grid_str.splitlines():
    new_row = []
    for val in row:
        new_row.extend(grid_map[val])
    grid.append(new_row)
moves = moves.replace("\n", "")

for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == "@":
            break
    else:
        continue
    break

move_map = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
for move in moves:
    dr, dc = move_map[move]
    do_move = True
    to_move = [(r, c)]
    i = 0
    while i < len(to_move):
        rr, cc = to_move[i]
        i += 1
        nr, nc = rr + dr, cc + dc
        if (nr, nc) in to_move:
            continue
        if grid[nr][nc] == "#":
            do_move = False
            break
        if grid[nr][nc] == ".":
            continue
        if grid[nr][nc] == "[":
            to_move.extend([(nr, nc), (nr, nc + 1)])
        elif grid[nr][nc] == "]":
            to_move.extend([(nr, nc), (nr, nc - 1)])
        else:
            assert False

    if not do_move:
        continue
    grid_copy = [list(row) for row in grid]
    r, c = r + dr, c + dc
    for rr, cc in to_move:
        grid[rr][cc] = "."
    for rr, cc in to_move:
        grid[rr + dr][cc + dc] = grid_copy[rr][cc]

part2 = sum(
    r * 100 + c for r, row in enumerate(grid) for c, val in enumerate(row) if val == "["
)
print(f"Part 2: {part2}")
