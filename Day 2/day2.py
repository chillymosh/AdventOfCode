from enum import Enum

with open("AdventOfCode2022/Day2/input.txt", "r") as f:
    data = [line.strip().split(" ") for line in f]


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @classmethod
    def convert(cls, s: str):
        if s in {"A", "X"}:
            return cls.ROCK
        elif s in {"B", "Y"}:
            return cls.PAPER
        else:
            return cls.SCISSORS


class Result(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6

    @classmethod
    def convert(cls, s: str):
        if s == "X":
            return cls.LOSE
        elif s == "Z":
            return cls.WIN
        else:
            return cls.DRAW


OUTCOMES: dict[tuple[Shape, Shape], Result] = {
    (Shape.ROCK, Shape.ROCK): Result.DRAW,
    (Shape.ROCK, Shape.PAPER): Result.WIN,
    (Shape.ROCK, Shape.SCISSORS): Result.LOSE,
    (Shape.PAPER, Shape.ROCK): Result.LOSE,
    (Shape.PAPER, Shape.PAPER): Result.DRAW,
    (Shape.PAPER, Shape.SCISSORS): Result.WIN,
    (Shape.SCISSORS, Shape.ROCK): Result.WIN,
    (Shape.SCISSORS, Shape.PAPER): Result.LOSE,
    (Shape.SCISSORS, Shape.SCISSORS): Result.DRAW,
}


def part1(h: list[str]) -> int:
    p1 = Shape.convert(h[0])
    p2 = Shape.convert(h[1])
    res = OUTCOMES[(p1, p2)]
    if res == Result.WIN:
        return p2.value + res.value
    return p2.value + res.value if p1 == p2 else p2.value


def part2(h: list[str]) -> int:
    p1 = Shape.convert(h[0])
    res = Result.convert(h[1])
    choice = {(o, c1): c2 for (c1, c2), o in OUTCOMES.items()}
    return choice[(res, p1)].value + res.value

print(sum(part1(h) for h in data))
print(sum(part2(h) for h in data))

# If you wanted you could just pass data into part1 and part2 and then return the sum directly using a generator with inner / nested function
def part1a(data: list[list[str]]) -> int:
    def outcome(h: list[str]) -> int:
        p1, p2 = map(Shape.convert, h)
        return p2.value + OUTCOMES[p1, p2].value
    return sum(outcome(h) for h in data)

def part2a(data: list[list[str]]) -> int:
    choice = {(o, c1): c2 for (c1, c2), o in OUTCOMES.items()}
    def outcome(h: list[str]) -> int:
        s, o = Shape.convert(h[0]), Result.convert(h[1])
        return o.value + choice[o, s].value

    return sum(outcome(h) for h in data)

# For some unreadable ord nonsense
p=print
d=[(ord((c:=m.split(" "))[0])-65,ord(c[1][0])-88) for m in open("AdventOfCode2022/Day2/input.txt", "r").readlines()]
p(sum(1+b+3*((b-a+1)%3) for a,b in d))
p(sum(3*b+(1+(a+b+2)%3) for a,b in d))