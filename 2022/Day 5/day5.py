with open("AdventOfCode2022/day5/input.txt", "r") as f:
    stacks, data = f.read().split("\n\n")
    stacks = stacks.splitlines()[:-1][::-1]
    stacks = [[s[i] for s in stacks if s[i] != " "] for i in range(1, len(stacks[0]), 4)]
    p1 = [x[:] for x in stacks]
    p2 = [x[:] for x in stacks]
    for row in data.splitlines():
        qty, from_stack, to_stack = [int(d) for d in row.split(" ") if d.isdigit()]
        for _ in range(qty):
            p1[to_stack - 1].append(p1[from_stack - 1].pop(-1))
        for i in range(qty, 0, -1):
            p2[to_stack - 1].append(p2[from_stack - 1].pop(-i))
    # Part 1
    print(''.join([s[-1] for s in p1]))

    #Part 2
    print(''.join([s[-1] for s in p2]))
