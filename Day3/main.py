import os
from collections import defaultdict
from pathlib import Path
import re

def read_file():
    rootpath = Path(__file__).parent
    filepath = os.path.join(rootpath, 'input.txt')

    with open(filepath, 'r') as file:
        return file.read()

def part1():
    input = read_file()
    l = re.findall(r"mul\([^,a-z]+,[^)a-z]+\)", str(input))
    print(l)
    print(len(l))

    sum = 0
    for val in l:
        print(val)
        a,b = val.split("(")[1].split(")")[0].split(",")
        try:
            if not int(a) or not int(b):
                print("Sike", val)
                continue
        except:
            print("Sike", val)
            continue

        print(a,b)
        sum = sum + int(a)*int(b)

    print(sum)

def part2():
    part1 = 0
    part2 = 0
    enabled = True
    for inst in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data):
        match inst:
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _:
                x, y = map(int, inst[4:-1].split(","))
                part1 += x * y
                if enabled:
                    part2 += x * y

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")



