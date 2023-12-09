def differences(seq: list[int]) -> list[int]:
    return [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]

def build_sequences(seq: list[int]) -> list[list[int]]:
    if all(d == 0 for d in seq):
        return [seq]
    else:
        return [seq] + build_sequences(differences(seq))

def solve_sequence(seq: list[int]) -> int:
    sequences = build_sequences(seq)
    return sum(seq[-1] for seq in sequences)

def solve_from_file(filename: str) -> tuple[int, int]:
    with open(filename, 'r') as f:
        lines = f.readlines()
        p1 = sum(solve_sequence(list(map(int, line.split()))) for line in lines)
        p2 = sum(solve_sequence(list(map(int, line.split()))[::-1]) for line in lines)
    return p1, p2


p1, p2 = solve_from_file("input.txt")
print(f"Part One Result: {p1}\nPart Two Result: {p2}")


# Class based solution

class SequenceSolver:
    def __init__(self, sequence: list[int]) -> None:
        self.sequence = sequence
        self.sequences = [sequence]

    def build_sequences(self) -> None:
        while any(d != 0 for d in self.sequences[-1]):
            self.sequences.append([self.sequences[-1][i+1] - self.sequences[-1][i] for i in range(len(self.sequences[-1]) - 1)])

    def solve(self) -> int:
        self.build_sequences()
        return sum(seq[-1] for seq in reversed(self.sequences))

def solve_from_file(filename: str) -> tuple[int, int]:
    with open(filename, "r") as f:
        lines = f.readlines()
        p1 = sum(SequenceSolver(list(map(int, line.split()))).solve() for line in lines)
        p2 = sum(SequenceSolver(list(map(int, line.split()))[::-1]).solve() for line in lines)
    return p1, p2

p1, p2 = solve_from_file("input.txt")
print(f"Part One Result: {p1}\nPart Two Result: {p2}")


# More functional
f = open("input.txt").read().strip().split("\n")

def solve(seq: list[list[int]]) -> int:
    i = 0
    while any(seq[-1]):
        seq.append([seq[i][j+1] - seq[i][j] for j in range(len(seq[i]) -1)])
        i += 1
    for i in range(len(seq) - 2, -1, -1):
        seq[i].append(seq[i][-1] + seq[i+1][-1])
    return seq[0][-1]

p1 = p2 = 0
for line in f:
    line = list(map(int, line.split()))
    p1 += solve([line])
    p1 += solve([line[::-1]])
print(p1, p2)