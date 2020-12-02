import math

def load_input():
  with open("input2.txt") as f:
    line = f.readline()
    return [int(x) for x in line.split(",")]

arr = load_input()

arr[1] = 12
arr[2] = 2

counter = 0
idx = 0
while True:
  opcode = arr[idx]
  first = arr[arr[idx + 1]]
  second = arr[arr[idx + 2]]
  store = arr[idx + 3]

  if opcode == 1:
    arr[store] = first + second
  elif opcode == 2:
    arr[store] = first * second
  else:
    print(f"last op code was {arr[idx]}")
    break
  idx += 4


  counter += 1

print(arr[0])
breakpoint()