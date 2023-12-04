with open("input.txt", "r") as f:
    data = [line.strip() for line in f]

cards: dict[int, dict[str, set[int]]] = {}

for i, n in enumerate(data, start=1):
    winning, mine = n.split("|")
    cards[i] = {
        "winning": set(winning.split()[2:]),
        "mine": set(mine.split())
    }

def calculate_total_points(cards: dict[int, dict[str, set[int]]], matches: dict[int, int]) -> int:
    return sum(2 ** (matches[i] - 1) for i in cards if matches[i] > 0)

def calculate_total_scratchcards(cards: dict[int, dict[str, set[int]]], matches: dict[int, int]) -> int:
    instances = {i: 1 for i in range(1, len(cards) + 1)}
    for i in range(1, len(cards)):
        for j in range(i + 1, min(len(cards) + 1, i + 1 + matches[i])):
            instances[j] += instances[i]
    return sum(instances.values())


matches: dict[int, int] = {i: len(cards[i]["winning"].intersection(cards[i]["mine"])) for i in cards}

p1 = calculate_total_points(cards, matches)
print(p1)

p2 = calculate_total_scratchcards(cards, matches)
print(p2)

