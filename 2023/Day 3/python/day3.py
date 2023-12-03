import math
import itertools

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
    for dx, dy in itertools.product(range(-1, 2), range(-1, 2)):
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
    return sum(math.prod(part[1]) for part in parts if part[0] == "*" and len(part[1]) == 2)

schematic = [list(line) for line in data]
parts = find_parts(schematic)

print(p1(parts))
print(p2(parts))



# I did stumble across someone else's which is kinda neat

# import sys
# import re


# def flatten_list(xss):
#     return [x for xs in xss for x in xs]

# def is_symbol(xy):
#     return xy in diagram and not diagram[xy].isdigit() and diagram[xy] != '.' 

# def adjecents8(xy):
#     (x, y) = xy
#     return [(x+1, y), (x-1, y), (x, y+1), 
#             (x, y-1), (x+1, y+1), 
#             (x-1, y-1), (x-1, y+1), (x+1, y-1)]

# def parse_numbers(line, y): # return type: tuple(value, list[xy])
#     acc = 0
#     xys = []

#     for x, c in enumerate(line):
#         if c.isdigit():
#             xys.append((x, y))
#             acc = 10 * acc + int(c)
#         else:
#             yield(acc, xys)
#             acc = 0
#             xys = []

#     if acc:
#         yield(acc, xys)

# def is_part(number):
#     _, xys = number
#     return any(map(is_symbol, flatten_list(map(adjecents8, xys))))

# ## PART 1
# input_lines = open(sys.argv[1]).readlines()
# diagram = { (x,y): c for y, line in enumerate(input_lines) for x, c in enumerate(line.strip()) }
# numbers = flatten_list(parse_numbers(line, y) for y, line in enumerate(input_lines))
# parts = [number for number in numbers if is_part(number)]

# print(f'1: {sum(val for val, _ in parts)}')


# ## PART 2
# stars = [xy for xy, c in diagram.items() if c == '*']
# adj_parts_vals = [ [val for val, part_xys in parts if set(part_xys) & set(adjecents8(star))] for star in stars ]

# print(f'2: {sum(v[0] * v[1] for v in adj_parts_vals if len(v) == 2)}')