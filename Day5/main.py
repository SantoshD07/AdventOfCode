import os
from collections import defaultdict
from pathlib import Path
from functools import cmp_to_key


def read_file():
    rootpath = Path(__file__).parent
    filepath = os.path.join(rootpath, 'input.txt')

    with open(filepath, 'r') as file:
        return file.read()


if __name__ == '__main__':
    data = read_file()
    rules, jobs = data.split('\n\n')

    rules = [tuple(map(int, l.split('|'))) for l in rules.splitlines()]
    jobs = [list(map(int, l.split(','))) for l in jobs.splitlines()]
    print(rules, '\n', jobs)

    part1 = 0
    part2 = 0
    flag = 0

    invalid_map = defaultdict(bool)
    for x, y in rules:
        invalid_map[(y, x)] = True

    def check_job(job):
        for i in range(len(job)):
            for j in range(i + 1, len(job)):
                if invalid_map[(job[i], job[j])]:
                   return False
        return True

    def sort_job(a:int, b:int):
        if invalid_map[(a,b)]:
            return 1
        return -1

    for job in jobs:
        if check_job(job):
            part1 += job[len(job) // 2]
        else:
            fixed_job = sorted(job,key = cmp_to_key(sort_job))
            part2 += fixed_job[len(job) // 2]

    print(part1)
    print(part2)