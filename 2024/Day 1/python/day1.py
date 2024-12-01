from pathlib import Path
from collections import Counter

with open(Path(__file__).parent.parent / "input.txt") as f:
    left, right = zip(*(map(int, line.split()) for line in f))

p1 = sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))
print(p1)

p2 = sum(l * right.count(l) for l in left)
print(p2)

# Optimised part 2
r_counter = Counter(right)
p2 = sum(l * r_counter[l] for l in left)
print(p2)
