from typing import Generator

with open("AdventOfCode2022/day6/input.txt", "r") as f:
    data = f.read()

# Generator sliding window
def window(s: str, window_size: int = 4) -> Generator[str, None, None]:
    for i in range(len(s) - window_size + 1):
        yield s[i : i + window_size]


def parse_gen(data: str, window_size: int = 4) -> int | None:
    for s in window(data, window_size):
        if len(set(s)) == window_size:
            return data.index(s) + window_size


# Part 1
print(parse_gen(data))

# Part 2
print(parse_gen(data, 14))


# You could also just use list comprehension and iterate


def parse_list(l: list[str], window_size: int = 4) -> int | None:
    for s in l:
        if len(set(s)) == window_size:
            return data.index(s) + window_size


p1 = [data[i : i + 4] for i in range(len(data) - 2)]
print(parse_list(p1))
p2 = [data[i : i + 14] for i in range(len(data) - 2)]
print(parse_list(p2, 14))
