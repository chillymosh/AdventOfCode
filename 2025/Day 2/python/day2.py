from pathlib import Path

data = Path(__file__).resolve().parent.parent.joinpath("input.txt").read_text()

p1 = p2 = 0

for chunk in data.split(','):
    start, end = map(int, chunk.strip().split('-'))
    for num in range(start, end + 1):
        s = str(num)

        if len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]:
            p1 += num

        if s in (s + s)[1:-1]:
            p2 += num

print(p1, p2)
