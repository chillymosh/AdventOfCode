with open("input.txt", "r") as f:
    data = [l.split() for l in f.readlines()]

card_values = dict(zip('23456789TJQKA', range(13)))
card_values2 = dict(zip('J23456789TQKA', range(13)))

def count_cards(cards: str) -> dict[str, int]:
    counts = {}
    for c in cards:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts

def part1(hand: list[str]) -> tuple[list[int], list[int]]:
    counts = count_cards(hand[0])
    hand_type = sorted(counts.values(), reverse=True)
    return hand_type, [card_values[c] for c in hand[0]]

def part2(hand: list[str]) -> tuple[list[int], list[int]]:
    counts = count_cards(hand[0])
    jokers = counts.pop('J', 0)
    hand_type = sorted(counts.values(), reverse=True)
    if hand_type:
        hand_type[0] += jokers
    else:
        hand_type = [jokers,]
    return hand_type, [card_values2[c] for c in hand[0]]

print(sum(int(bid) * (i + 1) for i, (_, bid) in enumerate(sorted(data, key=part1))))
print(sum(int(bid) * (i + 1) for i, (_, bid) in enumerate(sorted(data, key=part2))))

# Using Counter
from collections import Counter

def part1a(hand: list[str]):
    return sorted(Counter(hand[0]).values(), reverse=True), [card_values[c] for c in hand[0]]

def part2a(hand: list[str]) -> tuple[list[int], list[int]]:
    c = Counter(hand[0])
    jokers = c.pop('J', 0)
    hand_type = sorted(c.values(), reverse=True)
    if hand_type:
        hand_type[0] += jokers
    else:
        hand_type = [jokers,]
    return hand_type, [card_values2[c] for c in hand[0]]