import math

def load_input():
  with open("input6.txt") as f:
    return f.readlines()

lines = load_input()

def parse(line):
  idx = line.index(")")
  parent = line[:idx]
  child = line[idx + 1:].strip()
  return (parent, child)

to_parent = dict()
nodes = set()

for line in lines:
  pair = parse(line)
  to_parent[pair[1]] = pair[0]
  nodes.add(pair[0])
  nodes.add(pair[1])

def get_ancestors(node, accumulator):
  if node not in to_parent:
    return []
  parent = to_parent[node]
  accumulator.append(parent)
  get_ancestors(parent, accumulator)

you_ancestors = []
get_ancestors("YOU", you_ancestors)

san_ancestors = []
get_ancestors("SAN", san_ancestors)

first_common = None
for i in range(0, len(you_ancestors)):
  if you_ancestors[i] in san_ancestors:
    first_common = you_ancestors[i]
    break

if first_common is None:
  raise AssertionError("boo, could not find a path!")

first_common_ancestors = []
get_ancestors(first_common, first_common_ancestors)

print(len(you_ancestors) + len(san_ancestors) - 2 * len(first_common_ancestors) - 2)
