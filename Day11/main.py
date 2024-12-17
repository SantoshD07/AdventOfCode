import os
from collections import defaultdict
from pathlib import Path
from itertools import combinations
from functools import cache

rootpath = Path(__file__).parent
filepath = os.path.join(rootpath, 'input.txt')

with open(filepath, 'r') as file:
    stones = list(map(int, file.read().strip().split(" ")))

"""
- If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
- If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
- If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
"""

# for _ in range(25):
#     new_stones = []
#     for stone in stones:
#         if stone == 0:
#             new_stones.append(1)
#         elif len(str(stone)) % 2 == 0:
#             new_stones.append(int(str(stone)[len(str(stone)) // 2:]))
#             new_stones.append(int(str(stone)[:len(str(stone)) // 2]))
#         else:
#             new_stones.append(stone * 2024)
#
#     stones = new_stones
#
# print(len(stones))


""" Bruh Part-2 75 blinks takes forever, len(list) reaching 12M so optimizing the above"""

@cache
def count_stones(val, blinks):
   if blinks == 0:
       return 1

   if val == 0:
       return count_stones(1, blinks-1)

   str_val = str(val)
   len_str_val = len(str_val)
   if len_str_val % 2 ==0:
       return count_stones(int(str_val[:len_str_val//2]), blinks - 1) + count_stones(int(str_val[len_str_val//2:]), blinks - 1)

   return count_stones(val*2024, blinks-1)

part2 = sum(count_stones(val, 75) for val in stones)
print(part2)