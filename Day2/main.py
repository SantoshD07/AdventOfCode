import os
from collections import defaultdict
from pathlib import Path


def read_file():
    rootpath = Path(__file__).parent
    filepath = os.path.join(rootpath, 'input.txt')

    with open(filepath, 'r') as file:
        return file.readlines()


def is_increasing(nums):
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            return False
    return True


def is_decreasing(nums):
    for i in range(1, len(nums)):
        if nums[i] >= nums[i - 1]:
            return False
    return True


def part1():
    inputlines = read_file()
    ctr = 0
    for val in inputlines:
        values = list(map(int, val.split('\n')[0].split(" ")))
        # print(values)
        decrease = is_decreasing(values)
        increase = is_increasing(values)

        if not decrease and not increase:
            continue

        safe = True
        for i in range(1, len(values)):
            distance = abs(values[i] - values[i - 1])
            if distance < 1 or distance > 3:
                safe = False
                break

        if safe == True:
            ctr += 1

    print(ctr)


# Part 2

def is_safe(nums):
    n = len(nums)
    return ((all(1 <= nums[i] - nums[i + 1] <= 3 for i in range(n - 1))) or (
        all(1 <= nums[i + 1] - nums[i] <= 3 for i in range(n - 1))))


def part2():
    inputlines = read_file()
    ctr = 0
    for val in inputlines:
        values = list(map(int, val.split('\n')[0].split(" ")))
        ctr += is_safe(values) or any(is_safe(values[:i] + values[i + 1:]) for i in range(len(values)))
    print(ctr)


if __name__ == '__main__':
    part2()
