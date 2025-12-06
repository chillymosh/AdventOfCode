from pathlib import Path
from math import prod

data = Path(__file__).parent.parent.joinpath("input.txt").read_text().splitlines()

block = list[tuple[str, ...]]

w = max(map(len, data))
blocks: list[block] = []
cur: list[tuple[str, ...]] = []

for col in zip(*[line.ljust(w) for line in data]):
    if all(c == " " for c in col):
        if cur: 
            blocks.append(cur)
            cur = []
    else:
        cur.append(col)
if cur:
    blocks.append(cur)

def calculate(nums: list[int], op: str) -> int:
    return sum(nums) if op == "+" else prod(nums)

def part1(blocks: list[list[tuple[str, ...]]]) -> int:
    total = 0
    for block in blocks:
        rows = list(zip(*block))
        op = "+" if "+" in rows[-1] else "*"
        nums = [int("".join(r).strip()) for r in rows[:-1]]
        total += calculate(nums, op)
    return total

def part2(blocks: list[list[tuple[str, ...]]]) -> int:
    total = 0
    for block in blocks:
        rows = list(zip(*block))
        op = "+" if "+" in rows[-1] else "*"
        nums = [
            int("".join(d for d in col if d != " "))
            for col in reversed(list(zip(*rows[:-1])))
            if any(d != " " for d in col)
        ]
        total += calculate(nums, op)
    return total

print(part1(blocks))
print(part2(blocks))
