import itertools
from pathlib import Path
from collections import deque

with open(Path(__file__).parent.parent / "input.txt") as f:
    data = [list(line.strip()) for line in f]


DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]


def total_removable_rolls(grid: list[list[str]]) -> int:
    rows, cols = len(grid), len(grid[0])

    neigh = [[0] * cols for _ in range(rows)]
    for r, c in itertools.product(range(rows), range(cols)):
        if grid[r][c] != "@":
            continue
        neigh[r][c] = sum(
            0 <= r + dr < rows
            and 0 <= c + dc < cols
            and grid[r + dr][c + dc] == "@"
            for dr, dc in DIRECTIONS
        )

    q = deque(
        (r, c)
        for r, c in itertools.product(range(rows), range(cols))
        if grid[r][c] == "@" and neigh[r][c] < 4
    )

    removed = 0

    while q:
        r, c = q.popleft()
        if grid[r][c] != "@":
            continue

        grid[r][c] = "."
        removed += 1

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if grid[nr][nc] != "@":
                continue

            neigh[nr][nc] -= 1

            if neigh[nr][nc] == 3:
                q.append((nr, nc))

    return removed


def count_accessible(grid: list[list[str]]) -> int:
    rows, cols = len(grid), len(grid[0])
    return sum(
        grid[r][c] == "@"
        and sum(
            0 <= r + dr < rows
            and 0 <= c + dc < cols
            and grid[r + dr][c + dc] == "@"
            for dr, dc in DIRECTIONS
        )
        < 4
        for r, c in itertools.product(range(rows), range(cols))
    )


p1 = count_accessible([row[:] for row in data])
p2 = total_removable_rolls([row[:] for row in data])

print(p1)
print(p2)