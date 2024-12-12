import os
from collections import defaultdict
from pathlib import Path

rootpath = Path(__file__).parent
filepath = os.path.join(rootpath, 'input.txt')

with open(filepath, 'r') as file:
    lines = list(map(str.strip, file.readlines()))


def check_possibility(target, nums, part2=False) -> bool:
    if len(nums) == 1:
        return target == nums[0]

    num = nums.pop()
    if target % num == 0:
        if check_possibility(target // num, nums[:], part2=part2):
            return True

    if target - num >= 0:
        if check_possibility(target - num, nums[:], part2=part2):
            return True

    if not part2:
        return False

    str_target = str(target)
    str_num = str(num)
    if str_target.endswith(str_num) and len(str_target) > len(str_num):
        new_target = int(str_target[:-len(str_num)])
        if check_possibility(new_target, nums[:], part2=part2):
            return True


part1 = 0
part2 = 0
for line in lines:
    target = int(line.split(':')[0])
    nums = list(map(int, line.split(': ')[1].split(' ')))

    if check_possibility(target, nums[:]):
        part1 += target
    if check_possibility(target, nums[:], part2=True):
        part2 += target

print("Part1", part1)
print("Part2", part2)
