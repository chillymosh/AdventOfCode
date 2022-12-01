from itertools import groupby

with open("AdventOfCode2022/day1/data.txt", "r") as f:
    data = [line.strip() for line in f]

res = sorted([sum(int(d) for d in sub)for ele, sub in groupby(data, key = bool) if ele])

# Part 1
p1 = res[-1]

# Part 2
p2 = sum(res[-3:])

# If you wanted to then could have done
# Part 1
print(max(sum(int(d) for d in sub)for ele, sub in groupby(data, key = bool) if ele))
# Part 2
print(sum(sorted([sum(int(d) for d in sub)for ele, sub in groupby(data, key = bool) if ele])[-3:]))
