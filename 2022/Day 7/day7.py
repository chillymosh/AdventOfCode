from pathlib import Path
from collections import defaultdict
from itertools import accumulate

with open("AdventOfCode2022/day7/input.txt") as f:
    data = f.readlines()

# No imports

directories = {"/root": 0}
current = "/root"

for line in data:
    line = line.rstrip()
    if line[0] == "$":
        if line[2:4] == "cd":
            if line[5:6] == "/":
                current = "/root"
            elif line[5:7] == "..":
                current = current[: current.rfind("/")]
            else:
                current = current + "/" + (line[5:])
                directories[current] = 0
    elif line[:3] != "dir":
        size = int(line[: line.find(" ")])
        dict_loc = current

        for _ in range(dict_loc.count("/")):
            directories[dict_loc] += size
            dict_loc = dict_loc[: dict_loc.rfind("/")]

p1 = 0
max_used = directories["/root"] - 40000000
target_dir = []
for d in directories:
    if directories[d] < 100000:
        p1 += directories[d]
    if max_used <= directories[d]:
        target_dir.append(directories[d])

print(p1)
print(min(target_dir))

# Pathlib and defaultdict


def part1(data: list[str]) -> int:
    current_path = ""
    file_size = {}

    for l in data:
        if "$" in l:
            if " cd " in l:
                if l.split()[2] == "/":
                    current_path = "/"
                elif l.split()[2] == "..":
                    current_path = current_path.rsplit("/", 1)[0]
                else:
                    current_path += "/" + l.split()[2]
                    current_path = current_path.replace("//", "/")
        elif "dir" not in l:
            file_path = (current_path + "/" + l.split()[1]).replace("//", "/")
            file_size[file_path] = int(l.split()[0])

    folder_size = defaultdict(int)
    for f, value in file_size.items():
        folder = Path(f).parent
        while True:
            folder_size[folder] += value
            if folder == Path("/"):
                break
            folder = folder.parent

    return sum(filter(lambda x: x <= 100000, folder_size.values()))


def part2(data: list[str]) -> int | None:
    current_path = ""
    file_size = {}

    for l in data:
        if "$" in l:
            if " cd " in l:
                if l.split()[2] == "/":
                    current_path = "/"
                elif l.split()[2] == "..":
                    current_path = current_path.rsplit("/", 1)[0]
                else:
                    current_path += "/" + l.split()[2]
                    current_path = current_path.replace("//", "/")
        elif "dir" not in l:
            file_path = (current_path + "/" + l.split()[1]).replace("//", "/")
            file_size[file_path] = int(l.split()[0])

    folder_size = defaultdict(int)
    for f, value in file_size.items():
        folder = Path(f).parent
        while True:
            folder_size[folder] += value
            if folder == Path("/"):
                break
            folder = folder.parent

    total_space = 70000000
    needed_space = 30000000

    least_del = needed_space - (total_space - folder_size[Path("/")])

    for s in sorted(folder_size.values()):
        if s > least_del:
            return s

part1(data)
part2(data)


# Using accumulate, defaultdict and match case

from collections import defaultdict
from itertools import accumulate


dirs = defaultdict(int)

for line in open("AdventOfCode2022/day7/input.txt"):
    match line.split():

        case "$", "cd", "/":
            current = ["/"]
        case "$", "cd", "..":
            current.pop()
        case "$", "cd", x:
            current.append(x + "/")
        case "$", "ls":
            pass
        case "dir", _:
            pass
        case size, _:
            for p in accumulate(current):
                dirs[p] += int(size)

# Part 1
print(sum(s for s in dirs.values() if s <= 100000))

# Part 2
print(min(s for s in dirs.values() if s >= dirs["/"] - 40000000))
