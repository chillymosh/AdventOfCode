from pathlib import Path

path = Path(__file__).parent.parent / "input.txt"
data = [int(x) for x in path.read_text().splitlines()]

p1 = sum(b > a for a, b in zip(data, data[1:]))
print(p1)
p2 = sum(b > a for a, b in zip(data, data[3:]))
print(p2)

# You can use pairwise for 2 elements
from itertools import pairwise
p1 = sum(b > a for a, b in pairwise(data))



