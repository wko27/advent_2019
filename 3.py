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
  coords = dict()
  curX = 0
  curY = 0
  step_count = 1
  for direction in path:
    (deltaX, deltaY) = get_direction(direction[0])
    num_steps = int(direction[1:])
    for i in range(0, num_steps):
      curX += deltaX
      curY += deltaY
      coord = (curX, curY)
      if coord not in coords:
        coords[coord] = step_count
      step_count += 1
  return coords

(path1, path2) = load_input()

coords1 = path_to_coords(path1)
coords2 = path_to_coords(path2)

crossed = set(coords1.keys()).intersection(set(coords2.keys()))

min_dist = min([coords1[coord] + coords2[coord] for coord in crossed])
print(min_dist)
# breakpoint()

