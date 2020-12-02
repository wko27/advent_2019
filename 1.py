import math

def calculate_fuel(value):
  if value <= 0:
    return 0
  fuel = math.floor(value / 3) - 2
  if fuel < 0:
    return 0
  return fuel + calculate_fuel(fuel)

sum_fuel = 0
with open("input1.txt") as f:
  lines = f.readlines()
  for line in lines:
    mass = int(line.strip())
    # breakpoint()
    fuel = calculate_fuel(mass)
    sum_fuel += fuel

print(sum_fuel)
