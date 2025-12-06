from pathlib import Path

data = Path(__file__).parent.parent.joinpath("input.txt").read_text().splitlines()

dial_size = 100
pos = 50
p1 = p2 = 0

def count_hits(pos: int, turns: int, direction: str) -> int:
    base = (dial_size - pos) % dial_size if direction == "R" else pos % dial_size
    if base == 0:
        base = dial_size
    return 0 if base > turns else 1 + (turns - base) // dial_size


for line in data:
    direction, turns = line[0], int(line[1:])

    p2 += count_hits(pos, turns, direction)
    
    step = 1 if direction == "R" else -1
    pos = (pos + step * turns) % dial_size

    if pos == 0:
        p1 += 1

print(p1)
print(p2)
        

# Some code golf
D=100;p=50;a=b=0
for s in data:
 d,t=s[0],int(s[1:])
 x=((D-p)%D if d>'L'else p)%D or D
 b+=t>=x and 1+(t-x)//D;p=(p+(d>'L'and 1or-1)*t)%D;a+=p<1
print(a,b)
