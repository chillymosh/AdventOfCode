import re

with open("input.txt", "r") as f:
    data = [line.strip() for line in f]


num_words_to_digits = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def replace_words_with_digits(line: str):
    result = ""
    while line:
        replaced = False
        for word, digit in num_words_to_digits.items():
            if line.startswith(word):
                result += digit
                line = line[len(word) :]
                replaced = True
                break
        if not replaced:
            result += line[0]
            line = line[1:]
    return result


processed_data = [replace_words_with_digits(l) for l in data]

p1 = sum(int("".join(i for i in l if i.isdigit())[0] + "".join(i for i in l if i.isdigit())[-1]) for l in data)
print(p1)

p2 = sum(
    int("".join(i for i in l if i.isdigit())[0] + "".join(i for i in l if i.isdigit())[-1]) for l in processed_data
)
print(p2)

# Alternatives

p1_a = sum(
    int((next((i for i in l if i.isdigit()), "0") + next((i for i in reversed(l) if i.isdigit()), "0"))) for l in data
)
p2_a = sum(
    int((next((i for i in l if i.isdigit()), "0") + next((i for i in reversed(l) if i.isdigit()), "0")))
    for l in processed_data
)


# Regex solutions for part 2

p2_regex = sum(
    int(num_words_to_digits.get(first_last[0], first_last[0]) + num_words_to_digits.get(first_last[1], first_last[1]))
    for c in data
    for first_last in [
        re.findall(
            "|".join(list(num_words_to_digits) + [str(i) for i in range(1, 10)]),
            c,
        )[:1]
        + re.findall(
            "|".join(list(num_words_to_digits) + [str(i) for i in range(1, 10)]),
            c,
        )[-1:]
    ]
)


total = 0
for line in data:
    matches = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
    total += int(num_words_to_digits.get(matches[0], matches[0]) + num_words_to_digits.get(matches[-1], matches[-1]))
