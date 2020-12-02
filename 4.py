lower = 178416
bound = 676461

def is_valid(value):
  as_str = str(value)
  has_adjacent_digits = False
  for i in range(0, 5):
    if as_str[i] != as_str[i + 1]:
      continue

    has_next_same = i + 2 < 6 and as_str[i + 1] == as_str[i + 2]
    has_prev_same = i != 0 and as_str[i - 1] == as_str[i]
    if not has_next_same and not has_prev_same:
      has_adjacent_digits = True
      break

  if not has_adjacent_digits:
    return False

  has_decrease = False
  for i in range(0, 5):
    if int(as_str[i]) > int(as_str[i + 1]):
      has_decrease = True
      break

  if has_decrease:
    return False

  return True

counter = 0
for i in range(lower, bound):
  if is_valid(i):
    counter += 1

print(counter)