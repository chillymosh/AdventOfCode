from pathlib import Path
import itertools

Coord  = tuple[int, int]

data = [
    (int(x), int(y))
    for x, y in (
        line.split(",")
        for line in Path(__file__).parent.parent.joinpath("input.txt").read_text().splitlines()
    )
]

def area(a: Coord , b: Coord) -> int:
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

def part1(coords: list[Coord]) -> int: 
    return max(area(a, b) for a, b in itertools.combinations(coords, 2))

def line(a: Coord, b: Coord) -> set[tuple[int, int]]:
    a1, a2 = min(a[0], b[0]), max(a[0], b[0])
    b1, b2 = min(a[1], b[1]), max(a[1], b[1])
    return set(itertools.product(range(a1, a2 + 1), range(b1, b2 + 1)))

def find_perimeter(data: list[Coord]) -> set[Coord]: 
    perimeter: set[Coord] = set() 
    for i in range(1, len(data)): 
        perimeter |= line(data[i - 1], data[i]) 
    perimeter |= line(data[-1], data[0]) 
    return perimeter 

def contains_perimeter(a: Coord, b: Coord, perimeter: set[Coord]) -> bool:
    a1, a2 = min(a[0], b[0]), max(a[0], b[0])
    b1, b2 = min(a[1], b[1]), max(a[1], b[1])
    return not any((a1 < s[0] < a2) and (b1 < s[1] < b2) for s in perimeter)

def part2(data: list[Coord]) -> int: 
    perimeter = find_perimeter(data)
    max_area = 0
    
    for a, b in itertools.combinations(data, 2):
        rect_area = area(a, b)
        
        if rect_area <= max_area:
            continue    
        if contains_perimeter(a, b, perimeter):
            max_area = rect_area
    
    return max_area

print(part1(data))
print(part2(data))
