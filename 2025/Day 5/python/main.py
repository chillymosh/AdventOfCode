from pathlib import Path

RANGES: list[tuple[int, int]] = []
INTS: list[int] = []

with open(Path(__file__).parent.parent / "input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        if "-" in line:
            start, end = map(int, line.split("-"))
            RANGES.append((start, end))
        else:
            INTS.append(int(line))

p1 = sum(any(start <= v <= end for start, end in RANGES) for v in INTS)
print(p1)
        
merged: list[list[int]] = []

for start, end in sorted(RANGES):
    if merged and start <= merged[-1][1] + 1:
        merged[-1][1] = max(merged[-1][1], end)
    else:
        merged.append([start, end])

p2 = sum(b - a + 1 for a, b in merged)
print(p2)
