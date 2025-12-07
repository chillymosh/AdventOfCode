from pathlib import Path
from collections import defaultdict

data = Path(__file__).parent.parent.joinpath("input.txt").read_text().splitlines()

def solve(grid: list[str], part: int = 1) -> int:
    height, width = len(grid), len(grid[0])
    start_col = grid[0].index("S")
    beams = {start_col: 1}
    p1 = p2 = 0

    for r in range(1, height):
        new_beams: dict[int, int] = defaultdict(int)

        for c, ways in beams.items():
            if not (0 <= c < width):
                if part == 2:
                    p2 += ways
                continue

            if grid[r][c] != "^":
                new_beams[c] += ways
                continue

            if part == 1:
                p1 += 1

            for nc in (c - 1, c + 1):
                if 0 <= nc < width:
                    new_beams[nc] += ways
                elif part == 2:
                    p2 += ways

        beams = new_beams

    return p1 if part == 1 else p2 + sum(beams.values())

print(solve(data))
print(solve(data, 2))
