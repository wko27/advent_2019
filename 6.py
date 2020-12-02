import math

def load_input():
  with open("input6.txt") as f:
    return f.readlines()

lines = load_input()

def parse(line):
  idx = line.index(")")
  first = line[:idx]
  second = line[idx + 1:].strip()
  return (first, second)

to_parent = dict()
nodes = set()

for line in lines:
  pair = parse(line)
  to_parent[pair[1]] = pair[0]
  nodes.add(pair[0])
  nodes.add(pair[1])

total_depth = 0
for node in nodes:
  while True:
    if node not in to_parent:
      break
    node = to_parent[node]
    total_depth += 1

print(total_depth)


