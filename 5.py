import math

def load_input():
  with open("input5.txt") as f:
    line = f.readline()

    # line = '3,9,8,9,10,9,4,9,99,-1,8'
    # line = '3,9,7,9,10,9,4,9,99,-1,8'
    # line = '3,3,1108,-1,8,3,4,3,99'
    # line = '3,3,1107,-1,8,3,4,3,99'
    return [int(x) for x in line.split(",")]

instruction_arr = load_input()
input_arr = [5]

def calculate():
  arr = list(instruction_arr)
  input_array = list(input_arr)
  output_array = []

  counter = 0
  idx = 0
  input_idx = 0
  while True:
    opcode = arr[idx] % 100
    first_mode = int((arr[idx] / 100) % 10) == 0
    second_mode = int((arr[idx] / 1000) % 10) == 0
    third_mode = int((arr[idx] / 10000) % 10) == 0

    if opcode == 1:
      first = arr[arr[idx + 1]] if first_mode else arr[idx + 1]
      second = arr[arr[idx + 2]] if second_mode else arr[idx + 2]
      store = arr[idx + 3]
      arr[store] = first + second
      idx += 4
    elif opcode == 2:
      first = arr[arr[idx + 1]] if first_mode else arr[idx + 1]
      second = arr[arr[idx + 2]] if second_mode else arr[idx + 2]
      store = arr[idx + 3]
      arr[store] = first * second
      idx += 4
    elif opcode == 3:
      store = arr[idx + 1]
      arr[store] = input_array[input_idx]
      input_idx += 1
      idx += 2
    elif opcode == 4:
      output = arr[arr[idx + 1]] if first_mode else arr[idx + 1]
      output_array.append(output)
      idx += 2
    elif opcode == 5:
      first = arr[arr[idx + 1]] if first_mode else arr[idx + 1]
      second = arr[arr[idx + 2]] if second_mode else arr[idx + 2]
      if first != 0:
        idx = second
      else:
        idx += 3
    elif opcode == 6:
      first = arr[arr[idx + 1]] if first_mode else arr[idx + 1]
      second = arr[arr[idx + 2]] if second_mode else arr[idx + 2]
      if first == 0:
        idx = second
      else:
        idx += 3
    elif opcode == 7:
      first = arr[arr[idx + 1]] if first_mode else arr[idx + 1]
      second = arr[arr[idx + 2]] if second_mode else arr[idx + 2]
      store = arr[idx + 3]
      arr[store] = 1 if first < second else 0
      idx += 4
    elif opcode == 8:
      first = arr[arr[idx + 1]] if first_mode else arr[idx + 1]
      second = arr[arr[idx + 2]] if second_mode else arr[idx + 2]
      store = arr[idx + 3]
      arr[store] = 1 if first == second else 0
      idx += 4
    else:
      print(f"last op code was {arr[idx]}")
      break

  return output_array

print(calculate())
