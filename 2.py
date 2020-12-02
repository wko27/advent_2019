import math

def load_input():
  with open("input2.txt") as f:
    line = f.readline()
    return [int(x) for x in line.split(",")]

original_arr = load_input()

def calculate(noun, verb):
  arr = list(original_arr)
  arr[1] = noun
  arr[2] = verb

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

  return arr[0]

def find():
  for i in range(0, 100):
    for j in range(0, 100):
      if calculate(i, j) == 19690720:
        print("noun is " + str(i))
        print("verb is " + str(j))
        return (i, j)

(noun, verb) = find()
print(100 * noun + verb)
