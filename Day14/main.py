import os
import sys
from collections import defaultdict
from pathlib import Path
from itertools import combinations
import re
import math
import matplotlib.pyplot as plt

rootpath = Path(__file__).parent
filepath = os.path.join(rootpath, 'input.txt')

with open(filepath, 'r') as file:
    lines = list(map(str.strip, file.readlines()))

width = 101
height = 103


def safety_score(robots):
    quad = [0] * 4
    for xf, yf in robots:
        midw, midh = width // 2, height // 2
        if xf < midw:
            if yf < midh:
                quad[0] += 1
            if yf > midh:
                quad[1] += 1
        elif xf > midw:
            if yf < midh:
                quad[2] += 1
            if yf > midh:
                quad[3] += 1

    return math.prod(quad)


robots = []
for line in lines:
    x, y, dx, dy = tuple(map(int, re.findall(r'-?\d+', line)))
    robots.append((x, y, dx, dy))

part1_robots = []
for x, y, dx, dy in robots:
    xf = (x + (dx * 100)) % width
    yf = (y + (dy * 100)) % height

    part1_robots.append((xf, yf))

part1 = safety_score(part1_robots)
print(part1)

t = []
ss = []
for i in range(7847):
    snap_shot = []
    for x, y, dx, dy in robots:
        xf = (x + (dx * i)) % width
        yf = (y + (dy * i)) % height
        snap_shot.append((xf, yf))
    t.append(i)
    ss.append(safety_score(snap_shot))

for y in range(height):
    for x in range(width):
        if (x, y) in snap_shot:
            print("#", end="")
        else:
            print(".", end="")
    print()

# plt.plot(t, ss)
# plt.show()
