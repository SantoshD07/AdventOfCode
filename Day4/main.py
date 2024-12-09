import os
from collections import defaultdict
from pathlib import Path
import re

def part1():
    word_search = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            word_search.append(list(line.strip()))
    n = len(word_search)

    def is_inbounds(i, j):
        return 0 <= i < n and 0 <= j < n

    # part 1
    result = 0
    for i in range(n):
        for j in range(n):
            if word_search[i][j] != 'X':
                continue
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if (di, dj) == (0, 0):
                        continue
                    if is_inbounds(i + 3 * di, j + 3 * dj):
                        if ''.join(word_search[i + k * di][j + k * dj] for k in range(4)) == 'XMAS':
                            result += 1
    print(result)




if __name__ == '__main__':
    part1()