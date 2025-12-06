from pathlib import Path
from math import prod

data = Path(__file__).parent.parent.joinpath("input.txt").read_text().splitlines()

block = list[tuple[str, ...]]

w = max(map(len, data))
grid = [line.ljust(w) for line in data]
blocks: list[block] = []
cur: list[tuple[str, ...]] = []

for col in zip(*grid):
    if all(c == " " for c in col):
        if cur: 
            blocks.append(cur)
            cur = []
    else:
        cur.append(col)
if cur:
    blocks.append(cur)

def part1(blocks: list[block]) -> int:
    total = 0
    for block in blocks:
        rows = list(zip(*block))
        op = "+" if "+" in rows[-1] else "*"
        nums = [int("".join(r).strip()) for r in rows[:-1]]
        total += sum(nums) if op == "+" else prod(nums)
    return total


def part2(blocks: list[block]) -> int:
    total = 0
    for block in blocks:
        rows = list(zip(*block))
        op = "+" if "+" in rows[-1] else "*"
        cols = list(zip(*rows[:-1]))
        nums: list[int] = []
        
        for col in reversed(cols): 
            s = "".join(d for d in col if d != " ")
            if s:
                nums.append(int(s))

        total += sum(nums) if op == "+" else prod(nums) 
    return total

print(part1(blocks))
print(part2(blocks))
