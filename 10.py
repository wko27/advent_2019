import math

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

print(max_visible)

max_x = int(max_visible_loc / width)
max_y = int(max_visible_loc % width)
print(f"{max_x}, {max_y}")
