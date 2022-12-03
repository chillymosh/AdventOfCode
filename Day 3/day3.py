with open("AdventOfCode2022/day3/input.txt", "r") as f:
    data = [line.strip() for line in f]

# No Imports

def split_half(r: str) -> tuple[str, str]:
    half = len(r) // 2
    return r[:half], r[half:]


def calc_score(l: str) -> int:
    return ord(l) - 38 if l.isupper() else ord(l) - 96

# Part 1
p1_total = 0
for line in data:
    c1, c2 = split_half(line)
    common = set(c1).intersection(c2)
    for letter in common:
        p1_total += calc_score(letter)
print(p1_total)

# Part 2
batched = [data[i : i + 3] for i in range(0, len(data), 3)]

p2_total = 0
for r in batched:
    common = set(r[0]).intersection(r[1]).intersection(r[2])
    for letter in common:
        p2_total += calc_score(letter)
print(p2_total)


# Using Imports

from string import ascii_letters
from more_itertools import chunked

scores = {c: i + 1 for i, c in enumerate(ascii_letters)}
print(sum(scores[(set(l[: len(l) // 2]) & set(l[len(l) // 2 :])).pop()] for l in data))
print(sum(scores[(set(l1) & set(l2) & set(l3)).pop()] for l1, l2, l3 in chunked(data, 3)))
