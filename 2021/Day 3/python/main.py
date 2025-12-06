from pathlib import Path

data = (Path(__file__).parent.parent / "input.txt").read_text().splitlines()

gamma_bits: list[str] = []
for col in zip(*data):
    ones = col.count("1")
    zeros = len(col) - ones
    gamma_bits.append("1" if ones > zeros else "0")

gamma = int("".join(gamma_bits), 2)
epsilon = gamma ^ ((1 << len(data[0])) - 1)

print(gamma * epsilon)


def find_rating(numbers: list[str], keep_most_common: bool = True) -> int:
    remaining: list[str] = numbers[:]
    bit_len = len(numbers[0])

    for i in range(bit_len):
        if len(remaining) == 1:
            break

        ones = sum(num[i] == "1" for num in remaining)
        zeros = len(remaining) - ones
        most_common = "1" if ones >= zeros else "0"
        least_common = "0" if ones >= zeros else "1"
        bit_to_keep = most_common if keep_most_common else least_common
        remaining = [num for num in remaining if num[i] == bit_to_keep]

    return int(remaining[0], 2)

oxygen = find_rating(data)
co2 = find_rating(data, False)

print(oxygen * co2)