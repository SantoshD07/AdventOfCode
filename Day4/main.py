import os
from collections import defaultdict
from pathlib import Path


def read_file():
    rootpath = Path(__file__).parent
    filepath = os.path.join(rootpath, 'input.txt')

    with open(filepath, 'r') as file:
        return file.readlines()


lines = read_file()
char_map = defaultdict(set)

for r, row in enumerate(lines):
    for c, val in enumerate(row):
        char_map[val].add((r, c))


def part1():
    part1 = 0
    for r, c in char_map["X"]:
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
            for i, char in enumerate("MAS", 1):
                if (r + (dr * i), c + (dc * i)) not in char_map[char]:
                    break
            else:
                part1 += 1

    print(part1)


def part2():
    part2 = 0
    upleft = lambda r, c: (r - 1, c - 1)
    upright = lambda r, c: (r - 1, c + 1)
    downleft = lambda r, c: (r + 1, c - 1)
    downright = lambda r, c: (r + 1, c + 1)

    for r, c in char_map["A"]:
        if upleft(r, c) in char_map["M"]:
            if upright(r, c) in char_map["M"] and downleft(r, c) in char_map["S"] and downright(r, c) in char_map["S"]:
                part2 += 1
            elif downleft(r, c) in char_map["M"] and upright(r, c) in char_map["S"] and downright(r, c) in char_map["S"]:
                part2 += 1
        elif downright(r, c) in char_map["M"]:
            if upright(r, c) in char_map["M"] and downleft(r, c) in char_map["S"] and upleft(r, c) in char_map["S"]:
                part2 +=1
            elif downleft(r, c) in char_map["M"] and upright(r, c) in char_map["S"] and upleft(r, c) in char_map["S"]:
                part2 +=1

    print(part2)


if __name__ == '__main__':
    part2()
