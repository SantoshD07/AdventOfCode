import os
from collections import defaultdict
from pathlib import Path


def read_file(filepath: str):
    with open(filepath, 'r') as file:
        return file.readlines()


if __name__ == '__main__':
    rootpath = Path(__file__).parent
    filepath = os.path.join(rootpath, 'input.txt')
    inputlines = read_file(filepath)

    l1, l2 = [], []
    l1_hash, l2_hash = defaultdict(int), defaultdict(int)

    for val in inputlines:
        l1_val, l2_val = val.split("   ")
        l1_hash[int(l1_val)] = l1_hash[int(l1_val)] + 1
        l2_hash[int(l2_val)] = l2_hash[int(l2_val)] + 1

        l1.append(int(l1_val))
        l2.append(int(l2_val))

    l1.sort()
    l2.sort()
    result = 0

    for i in range(len(inputlines)):
        result = result + abs(l1[i] - l2[i])  # Day1, Part 1 solution
        result = result + l2_hash[l1[i]] * l1[i]  # Day1, Part 2 solution

    print(result)
    print(l2_hash)
