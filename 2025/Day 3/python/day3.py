from pathlib import Path

with open(Path(__file__).parent.parent / "input.txt") as f:
    data = [i.strip() for i in f.readlines()]

def max_bank_joltage(bank: str) -> int:
    max_right = int(bank[-1])
    best = 0

    for c in reversed(bank[:-1]):
        left = int(c)
        best = max(best, 10 * left + max_right)
        max_right = max(max_right, left)

    return best

# We could also use this for part 1 as it takes any number of digits
def max_k_digits(bank: str, k: int) -> int:
    digits = [int(c) for c in bank]
    n = len(digits)
    result_digits: list[int] = []
    start = 0

    for remaining in range(k, 0, -1):
        end = n - remaining
        max_digit = -1
        max_index = start
        
        for i in range(start, end + 1):
            if digits[i] > max_digit:
                max_digit = digits[i]
                max_index = i
                if max_digit == 9:
                    break

        result_digits.append(max_digit)
        start = max_index + 1

    return int("".join(str(d) for d in result_digits))


p1 = sum(max_bank_joltage(bank) for bank in data)
print(p1)


p2 = sum(max_k_digits(bank, 12) for bank in data)
print(p2)

# Can also be used for part 1
print(sum(max_k_digits(bank, 2) for bank in data))