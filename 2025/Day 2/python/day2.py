from pathlib import Path

data = Path(__file__).resolve().parent.parent.joinpath("input.txt").read_text()

p1 = p2 = 0

def is_invalid_id(num: int) -> bool:
    s = str(num)
    return len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]

def is_invalid_id2(num: int) -> bool:
    s = str(num)
    return s in (s + s)[1:-1]

def find_invalid_ids(ranges_str: str) -> tuple[int, int]:
    p1 = p2 = 0

    for chunk in ranges_str.split(','):
        start, end = map(int, chunk.strip().split('-'))
        for num in range(start, end + 1):
            s = str(num)

            if len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]:
                p1 += num

            if s in (s + s)[1:-1]:
                p2 += num

    return p1, p2

print(find_invalid_ids(data))
