import math

with open("input.txt", "r") as f:
    data = [line.strip() for line in f]


def full_number(x: int, y: int, schematic: list[list[str]], searched: list[tuple[int, int, int]]) -> int:
    y_min, y_max = y, y
    while y_min >= 1 and schematic[x][y_min - 1].isdigit():
        y_min -= 1
    while y_max < len(schematic[x]) and schematic[x][y_max].isdigit():
        y_max += 1

    if (x, y_min, y_max) not in searched:
        searched.append((x, y_min, y_max))
        return int("".join(schematic[x][y_min:y_max]))
    return 0


def adjacent_numbers(i: int, j: int, schematic: list[list[str]], searched: list[tuple[int, int, int]]) -> list[int]:
    numbers: list[int] = []
    for dx, dy in ((-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, 0), (1, -1), (1, 1)):
        x, y = i + dx, j + dy
        if 0 <= x < len(schematic) and 0 <= y < len(schematic[x]) and schematic[x][y].isdigit():
            number = full_number(x, y, schematic, searched)
            if number != 0:
                numbers.append(number)
    return numbers


def find_parts(schematic: list[list[str]]) -> list[tuple[str, list[int]]]:
    searched = []
    parts: list[tuple[str, list[int]]] = []
    for i in range(len(schematic)):
        parts.extend(
            (schematic[i][j], adjacent_numbers(i, j, schematic, searched))
            for j in range(len(schematic[i]))
            if not schematic[i][j].isdigit() and schematic[i][j] != "."
        )
    return parts


def p1(parts: list[tuple[str, list[int]]]) -> int:
    return sum(sum(part[1]) for part in parts)


def p2(parts: list[tuple[str, list[int]]]) -> int:
    return sum(math.prod(part[1]) for part in parts if len(part[1]) == 2)

schematic = [list(line) for line in data]
parts = find_parts(schematic)

print(p1(parts))
print(p2(parts))



# I did stumble across someone else's which is kinda neat


print(sum(int(l[j:k])
    for i,l in enumerate(data) 
    for j in range(len(l)-1)
    for k in range(j,j+4)
    if(1-l[j-1:k].isdigit())*l[j:k].isdigit()*(k>=len(l)or 1-l[k].isdigit())*
      any(c not in"1234567890.\n"for x in data[max(0,i-1):i+2]for c in x[max(0,j-1):k+1])
))


print(sum(len(q:=[int(m[x:k])
      for m in data[max(0,i-1):i+2]
      for x in range(max(0,j-3),j+2) 
      for k in range(max(x,j),x+4)
      if((k>=len(m))or 1-m[k].isdigit())*m[x:k].isdigit()*((x<1)or 1-m[x-1].isdigit())
     ])==2 and q[0]*q[1]
    for i,l in enumerate(data)
    for j in range(len(l)-1)
    if l[j] == "*"
))

# Another from a friend group

import re
from collections import defaultdict


def p1_a():
    ans = 0
    for i, line in enumerate(data):
        for m in re.finditer(r"\d+", line):
            idxs = [(i, m.start() - 1), (i, m.end())]
            idxs += [(i - 1, j) for j in range(m.start() - 1, m.end() + 1)]
            idxs += [(i + 1, j) for j in range(m.start() - 1, m.end() + 1)]
            count = sum(0 <= a < len(data) and 0 <= b < len(data[a]) and data[a][b] != "." for a, b in idxs)
            if count > 0:
                ans += int(m.group())
    return ans


def p2_a():
    adj = defaultdict(list)
    for i, line in enumerate(data):
        for m in re.finditer(r"\d+", line):
            idxs = [(i, m.start() - 1), (i, m.end())]
            idxs += [(i - 1, j) for j in range(m.start() - 1, m.end() + 1)]
            idxs += [(i + 1, j) for j in range(m.start() - 1, m.end() + 1)]
            for a, b in idxs:
                if 0 <= a < len(data) and 0 <= b < len(data[a]) and data[a][b] != ".":
                    adj[a, b].append(m.group())
    return sum(int(x[0]) * int(x[1]) for x in adj.values() if len(x) == 2)

print(p1_a())
print(p2_a())