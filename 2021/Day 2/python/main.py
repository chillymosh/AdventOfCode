from pathlib import Path

data = [
    (cmd, int(n))
    for cmd, n in (
        line.split() for line in Path(__file__).parent.parent.joinpath("input.txt").read_text().splitlines()
    )
]

pos = depth = 0
for cmd, num in data:
    if cmd == "forward":
        pos += num
    elif cmd == "down":
        depth += num
    else:
        depth -= num

print(pos * depth)

pos = depth = aim = 0
for cmd, num in data:
    if cmd == "down":
        aim += num
    elif cmd == "forward":
        pos += num
        depth += aim * num
    else:
        aim -= num

print(pos * depth)
