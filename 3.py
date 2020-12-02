import math

def load_input():
  with open("input3.txt") as f:
    line1 = f.readline()
    line2 = f.readline()
    path1 = [x for x in line1.split(",")]
    path2 = [x for x in line2.split(",")]
    return (path1, path2)

def get_direction(direction):
  if direction[0] == 'D':
    return (0, -1)
  elif direction[0] == 'R':
    return (1, 0)
  elif direction[0] == 'U':
    return (0, 1)
  elif direction[0] == 'L':
    return (-1, 0)

def path_to_coords(path):
  coords = set()
  curX = 0
  curY = 0
  for direction in path:
    (deltaX, deltaY) = get_direction(direction[0])
    num_steps = int(direction[1:])
    for i in range(0, num_steps):
      curX += deltaX
      curY += deltaY
      coords.add((curX, curY))
  return coords

(path1, path2) = load_input()

coords1 = path_to_coords(path1)
coords2 = path_to_coords(path2)

crossed = coords1.intersection(coords2)

min_dist = min([abs(x) + abs(y) for (x, y) in crossed])
print(min_dist)
# breakpoint()

