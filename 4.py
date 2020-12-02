lower = 178416
bound = 676461

def is_valid(i):
  as_str = str(i)
  has_adjacent_digits = False
  for i in range(0, 5):
    if as_str[i] == as_str[i + 1]:
      has_adjacent_digits = True

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