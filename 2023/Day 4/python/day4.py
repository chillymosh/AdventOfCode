with open("input.txt", "r") as f:
    data = [line.strip() for line in f]

def calculate_total_points(cards: dict[int, dict[str, set[str]]], matches: dict[int, int]) -> int:
    return sum(2 ** (matches[i] - 1) for i in cards if matches[i] > 0)

def calculate_total_scratchcards(cards: dict[int, dict[str, set[str]]], matches: dict[int, int]) -> int:
    instances = {i: 1 for i in range(len(cards))}
    for i in range(len(cards)):
        for j in range(i + 1, min(len(cards) + 1, i + 1 + matches[i])):
            instances[j] += instances[i]
    return sum(instances.values())

cards = {i: {"winning": set(n.split("|")[0].split()[2:]),
             "mine": set(n.split("|")[1].split())}
         for i, n in enumerate(data)}

matches: dict[int, int] = {i: len(cards[i]["winning"].intersection(cards[i]["mine"])) for i in cards}

p1 = calculate_total_points(cards, matches)
print(p1)

p2 = calculate_total_scratchcards(cards, matches)
print(p2)



# My refactor of Mysty's attempt
p1_total = 0
p2_total = 0
thing = {i: 1 for i in range(len(data))}

for i, r in enumerate(data):
    numbers_s, winning_s = r.split(": ")[1].split(" | ")

    numbers = [int(n) for n in numbers_s.split() if n.isdigit()]
    winning = [int(n) for n in winning_s.split() if n.isdigit()]
    matching = [n for n in numbers if n in winning]

    # PART TWO
    for j in range(1, len(matching) + 1):
        thing[i + j] += thing[i]

    # PART ONE
    p1_total += 2 ** (len(matching) - 1) if matching else 0

p2_total = sum(thing.values())
print(f"PART ONE TOTAL: {p1_total}")
print(f"PART TWO TOTAL: {p2_total}")
