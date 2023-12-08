import math
from itertools import cycle
instructions, nodes = open('input.txt').read().split('\n\n')

node_map = {}
for node in nodes.splitlines():
    key, leftright = node.split(' = ')
    l, r = map(str.strip,leftright[1:-1].split(','))
    node_map[key.strip()] = {'L':l, 'R':r}

positions = sorted([k for k in node_map if k[-1] == 'A'])

found = []
for pos in positions:
    for step, inst in enumerate(cycle(instructions), start=1):
        pos = node_map[pos][inst]
        if pos[-1] == 'Z':
            found.append(step)
            break

print('p1', found[0])
print('p2', math.lcm(*found))