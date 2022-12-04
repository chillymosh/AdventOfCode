with open("AdventOfCode2022/Day4/input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

total = 0
total2 = 0

for a in data:
    g1 = a.split(",")[0].split("-")
    g2 = a.split(",")[1].split("-")
    set1 = {int(x) for x in range(int(g1[0]), int(g1[1])+1)}
    set2 = {int(x) for x in range(int(g2[0]), int(g2[1])+1)}
    if all(i in set1 for i in set2) or all(i in set2 for i in set1):
        total +=1

    # Part 2
    if any(i in set1 for i in set2) or any(i in set2 for i in set1):
        total2 +=1

print(total)
print(total2)