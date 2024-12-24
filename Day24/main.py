import os
from collections import defaultdict
from pathlib import Path
from itertools import combinations
import re
from dataclasses import dataclass


rootpath = Path(__file__).parent
filepath = os.path.join(rootpath, 'input.txt')

with open(filepath, 'r') as file:
   data = file.read()

@dataclass
class Connection:
    in1: str
    in2: str
    op: str
    out: str


operations = {
    "OR": lambda x1, x2: x1 | x2,
    "AND": lambda x1, x2: x1 & x2,
    "XOR": lambda x1, x2: x1 ^ x2,
}

def run_wire(w: str):
    if w in init:
        return init[w]
    conn = wire_map[w]
    return operations[conn.op](run_wire(conn.in1), run_wire(conn.in2))



init_pairs = re.findall(r"(.{3}): ([01])", data)
init = {k: int(v) for k, v in init_pairs}
map_str = data.split("\n\n")[1].splitlines()

wire_map = {}
for line in map_str:
    in1, op, in2, _, out = line.strip().split(' ')
    wire_map[out] = Connection(in1, in2, op, out)

result = [run_wire(w) for w in sorted([w for w in wire_map if w.startswith("z")], reverse=True)]

part1 = int(''.join(map(str, result)), 2)
print(f'Part 1: {part1}')
