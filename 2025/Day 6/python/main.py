from pathlib import Path
from math import prod

data = Path(__file__).parent.parent.joinpath("input.txt").read_text().splitlines()

block = list[tuple[str, ...]]

w = max(map(len, data))
blocks: list[block] = []
cur: block = []

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

def solve(blocks: list[block], part: int = 1) -> int:
    total = 0
    for block in blocks:
        rows = list(zip(*block))
        op = "+" if "+" in rows[-1] else "*"
        if part == 1:
            nums = [int("".join(r).strip()) for r in rows[:-1]]
        else:
            nums = [
            int("".join(d for d in col if d != " "))
            for col in reversed(list(zip(*rows[:-1])))
            if any(d != " " for d in col)
        ]
        total += calculate(nums, op)
    return total


print(solve(blocks))
print(solve(blocks, 2))
