with open("input.txt", "r") as f:
    data = [line.strip() for line in f]


cube_limits = {"red": 12, "green": 13, "blue": 14}


def is_game_possible(game: str) -> bool:
    rounds = game.split(": ")[1].split("; ")
    for colour in cube_limits:
        max_colour = max(sum(int(score.split(" ")[0]) for score in round.split(", ") if score.endswith(colour)) for round in rounds)
        if max_colour > cube_limits[colour]:
            return False
    return True

def total_power_of_cubes():
    total_power = 0
    for game in data:
        min_cubes = {colour: 0 for colour in cube_limits}
        rounds = game.split(": ")[1].split("; ")
        for round in rounds:
            round_counts = {colour: sum(int(score.split(" ")[0]) for score in round.split(", ") if score.endswith(colour)) for colour in cube_limits}
            for colour in cube_limits:
                min_cubes[colour] = max(min_cubes[colour], round_counts[colour])
        total_power += min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
    return total_power


possible_games = [game for game in data if is_game_possible(game)]
p1 = sum(int(game.split(":")[0].split(" ")[1]) for game in possible_games)
p2 = total_power_of_cubes()

print(p1, p2)

# All in one version

def all_in_one():
    sum_of_possible_game_ids = 0
    total_power = 0

    for game in data:
        game_id, rounds_info = game.split(": ")
        game_id = int(game_id.split(" ")[1])

        rounds = rounds_info.split("; ")
        min_cubes = {"red": 0, "green": 0, "blue": 0}
        possible = True

        for round in rounds:
            round_counts = {colour: int(value) for value, colour in (score.split(" ") for score in round.split(", "))}
            for colour in min_cubes:
                min_cubes[colour] = max(min_cubes[colour], round_counts.get(colour, 0))
                if min_cubes[colour] > cube_limits.get(colour, float("inf")):
                    possible = False

        if possible:
            sum_of_possible_game_ids += game_id

        power = min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
        total_power += power

    return sum_of_possible_game_ids, total_power

print(all_in_one())




# More broken down version
def get_game_id(game: str) -> int:
    return int(game.split(":")[0].split(" ")[1])

def is_game_possible2(game: str) -> bool:
    rounds = game.split(": ")[1].split("; ")
    for round in rounds:
        scores = round.split(", ")
        for score in scores:
            value, colour = score.split(" ")
            if int(value) > cube_limits[colour]:
                return False
    return True

p1_a = sum(get_game_id(game) for game in data if is_game_possible2(game))

print(p1_a)


def calculate_minimum_cubes(game: str) -> dict[str, int]:
    rounds = game.split(": ")[1].split("; ")
    min_cubes = {"red": 0, "green": 0, "blue": 0}

    for round in rounds:
        round_counts = {"red": 0, "green": 0, "blue": 0}
        scores = round.split(", ")
        for score in scores:
            value, colour = score.split(" ")
            round_counts[colour] += int(value)
        for colour in round_counts:
            min_cubes[colour] = max(min_cubes[colour], round_counts[colour])

    return min_cubes


p2_a: list[int] = []
for game in data:
    min_cubes = calculate_minimum_cubes(game)
    power = min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
    p2_a.append(power)

print(sum(p2_a))
         