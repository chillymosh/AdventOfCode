with open("input.txt", "r") as f:
    data = f.read()


lines = [line.split()[1:] for line in data.strip().split('\n')]
time_distance_pairs = list(zip(map(int, lines[0]), map(int, lines[1])))

def calculate_ways_to_win(time: int, distance: int) -> int:
    return sum(hold_time * (time - hold_time) > distance for hold_time in range(time))


def optimised_calculate_ways_to_win(time: int, distance: int) -> int:
    max_hold_time = 1
    while max_hold_time * (time - max_hold_time) <= distance:
        max_hold_time += 1
    return time - 2 * max_hold_time + 1

p1 = 1
for time, distance in time_distance_pairs:
    p1 *= optimised_calculate_ways_to_win(time, distance)

time_p2, distance_p2 = map(int, (''.join(lines[0]), ''.join(lines[1])))
p2 = optimised_calculate_ways_to_win(time_p2, distance_p2)

# even quicker quadratic
print(time_p2 - 2*int(time_p2/2 - (time_p2**2/4 - distance_p2)**.5) - 1)

# Part2 timings
# calculate_ways_to_win - 2.87 s ± 6.58 ms per loop
# optimised_calculate_ways_to_win - 484 ms ± 2.88 ms per loop
# quadratic - 825 ns ± 13.7 ns per loop


import math
from functools import reduce

p1 = 1
p1 = reduce(lambda x, pair: x * optimised_calculate_ways_to_win(*pair), time_distance_pairs, 1)
time, distance = map(int, (''.join(lines[0]), ''.join(lines[1])))
p2 = time - 2 * int(time / 2 - math.sqrt((time ** 2) / 4 -distance)) - 1