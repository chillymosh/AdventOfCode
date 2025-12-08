from pathlib import Path
from collections import Counter

data = [
    tuple(map(int, line.split(",")))
    for line in Path(__file__).parent.parent.joinpath("input.txt").read_text().split()
]
n = len(data)
edges = [
    ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2, i, j)
    for i, (x1, y1, z1) in enumerate(data)
    for j in range(i + 1, n)
    for x2, y2, z2 in [data[j]]
]
edges.sort()

class DSU:
    __slots__ = ("parent", "size", "components")

    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True

dsu1, dsu2 = DSU(n), DSU(n)

for d, a, b in edges[:1000]:
    dsu1.union(a, b)

sizes = sorted(Counter(dsu1.find(i) for i in range(n)).values(), reverse=True)
p1, p2 = sizes[0] * sizes[1] * sizes[2], 0
for d, a, b in edges:
    if dsu2.union(a, b) and dsu2.components == 1:
        p2 = data[a][0] * data[b][0]
        break

print(p1)
print(p2)
