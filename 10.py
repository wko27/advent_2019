import math
import sys

def load_input():
  with open("input10.txt") as f:
    lines = f.readlines()
    width = len(lines[0])
    height = len(lines)
    field = [point == '#' for row in lines for point in row]
    return (width, height, field)

(width, height, field) = load_input()

def is_visible(current, target):
  cur_x = int(current / width)
  cur_y = int(current % width)

  tar_x = int(target / width)
  tar_y = int(target % width)

  delta_x = tar_x - cur_x
  delta_y = tar_y - cur_y
  scale = math.gcd(abs(delta_x), abs(delta_y))

  if scale == 1:
    # No other obstacles in the way
    return True

  inc_delta_x = int(delta_x / scale)
  inc_delta_y = int(delta_y / scale)

  for delta in range(1, scale):
    check_x = cur_x + delta * inc_delta_x
    check_y = cur_y + delta * inc_delta_y
    target = check_x * width + check_y
    if field[target]:
      return False

  return True

max_visible = 0
max_visible_loc = None
for potential in range(0, len(field)):
  if not field[potential]:
    continue

  num_visible = 0
  for target in range(0, len(field)):
    if not field[target]:
      continue

    if potential == target:
      continue

    if is_visible(potential, target):
      num_visible += 1
  if num_visible > max_visible:
    max_visible = num_visible
    max_visible_loc = potential

max_x = int(max_visible_loc / width)
max_y = int(max_visible_loc % width)
print(f"found {max_visible} asteroids from {max_y}, {max_x}")

unique_angles = set()
angle_to_direction = dict()
for target in range(0, len(field)):
  if target == max_visible_loc:
    continue

  if not field[target]:
    continue
  
  tar_x = int(target / width)
  tar_y = int(target % width)

  delta_x = tar_x - max_x
  delta_y = (tar_y - max_y)

  # Note that we need to invert because the field is oriented with positive y downwards
  # Also ... I mixed up my x and y and am too lazy rename all the variables
  angle = math.atan2(-delta_x, delta_y)

  if angle > math.pi / 2:
    angle -= 2 * math.pi

  angle_to_direction[angle] = (delta_x, delta_y)
  unique_angles.add(angle)

angles = list(unique_angles)
sorted_angles = sorted(angles, reverse=True)

explosion_counter = 0
while explosion_counter <= 200:
  hit_anything = False
  for angle in sorted_angles:
    (delta_x, delta_y) = angle_to_direction[angle]

    scale = math.gcd(abs(delta_x), abs(delta_y))

    inc_delta_x = int(delta_x / scale)
    inc_delta_y = int(delta_y / scale)

    for delta in range(1, width):
      check_x = max_x + delta * inc_delta_x
      check_y = max_y + delta * inc_delta_y
      target = check_x * width + check_y
      if target < len(field) and field[target]:
        # kabooooom
        field[target] = False

        hit_anything = True
        explosion_counter += 1
        print(f"{explosion_counter} vaporized asteroid at {check_y}, {check_x}")
        if explosion_counter == 200:
          print(f"{check_y}, {check_x} and value is {check_y * 100 + check_x}")
        break

    if explosion_counter >= 200:
      break

  if not hit_anything:
    breakpoint()
    break
  print("full rotation complete!")
  

