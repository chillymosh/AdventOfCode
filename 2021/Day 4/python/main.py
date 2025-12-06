import itertools
from pathlib import Path

data = (Path(__file__).parent.parent / "input.txt").read_text()

sections = data.strip().split("\n\n")
draws = list(map(int, sections[0].split(",")))
boards_raw = sections[1:]
boards: list[list[list[int]]] = []
won: set[int] = set()
p1 = p2 = None

for block in boards_raw:
    board = [list(map(int, line.split())) for line in block.splitlines()]
    boards.append(board)

lookup: dict[int, list[tuple[int, int, int]]] = {}

for b, board in enumerate(boards):
    for r, c in itertools.product(range(5), range(5)):
        lookup.setdefault(board[r][c], []).append((b, r, c))

marks = [[[False]*5 for _ in range(5)] for _ in boards]
row_count = [[0]*5 for _ in boards]
col_count = [[0]*5 for _ in boards]
remaining = [sum(sum(row) for row in board) for board in boards]

for number in draws:
    if number not in lookup:
        continue

    for b, r, c in lookup[number]:
        if marks[b][r][c]:
            continue 

        marks[b][r][c] = True
        row_count[b][r] += 1
        col_count[b][c] += 1
        remaining[b] -= boards[b][r][c]


        if (row_count[b][r] == 5 or col_count[b][c] == 5) and b not in won:
            won.add(b)
            score = remaining[b] * number
        
            if p1 is None:
                p1 = score  
            p2 = score     

print(p1, p2)