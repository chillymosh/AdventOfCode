input_data = open("input.txt", "r").read()

sections = input_data.strip().split("\n\n")
data = {
    lines[0].split(":")[0]: [int(seed) for seed in lines[0].split()[1:]]
    if lines[0].startswith("seeds:")
    else [[int(num) for num in line.split()] for line in lines[1:]]
    for lines in (section.split("\n") for section in sections)
}


def part_1(seed: int) -> int:
    for map_name, map_values in data.items():
        if map_name != "seeds":
            for dest_start, src_start, length in map_values:
                if src_start <= seed < src_start + length:
                    offset = seed - src_start
                    seed = dest_start + offset
                    break
    return seed


def part_2() -> int:
    seeds = data["seeds"]
    ranges: list[tuple[int, int]] = [(seeds[i], seeds[i + 1] + seeds[i] - 1) for i in range(0, len(seeds), 2)]

    for map_name, map_values in data.items():
        if map_name != "seeds":
            nums: list[tuple[int, int]] = []
            overlaps = ranges
            for value in map_values:
                new_overlaps: list[tuple[int, int]] = []
                for overlap in overlaps:
                    overlap_start = max(value[1], overlap[0])
                    overlap_end = min(value[1] + value[2] - 1, overlap[1])
                    if overlap_start <= overlap_end:
                        nums.append((overlap_start + value[0] - value[1], overlap_end + value[0] - value[1]))
                        if overlap[0] < overlap_start:
                            new_overlaps.append((overlap[0], overlap_start - 1))
                        if overlap[1] > overlap_end:
                            new_overlaps.append((overlap_end + 1, overlap[1]))
                    else:
                        new_overlaps.append(overlap)
                overlaps = new_overlaps
            ranges = overlaps + nums

    return min(r[0] for r in ranges)


p1 = min(part_1(seed) for seed in data["seeds"])
print(p1)
p2 = part_2()
print(p2)


# Cool one liners

from functools import reduce
from itertools import chain
from re import findall

(f:=input_data.split('\n\n')) and print(min(reduce((lambda s,m:[(z:=map(int,findall(r'\d+',m))) and next((u+x-v for u,v,w in zip(z,z,z) if v<=x<v+w),x) for x in s]),f[1:],map(int,findall(r'\d+',f[0])))))

(f:=input_data.split('\n\n')) and print(min(reduce((lambda s,m:(z:=map(int,findall(r'\d+',m))) and (p:=[*zip(z,z,z)]) and [next(((u+x-v,l) for u,v,w in p if v<=x and x+l<=v+w),(x,l)) for x,l in reduce((lambda r,a:{*chain(*([(x,a-x),(a,x+l-a)] if x<a<x+l else [(x,l)] for x,l in r))}),chain(*((v,v+w) for _,v,w in p)),s)]),f[1:],(i:=map(int,findall(r'\d+',f[0]))) and [*zip(i,i)]))[0])


