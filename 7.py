import math

from itertools import permutations, repeat

OPCODE_MAPPING = [
  "[unknown]",
  "add-store",
  "multiply-store",
  "read",
  "write",
  "jump-if-true",
  "jump-if-false",
  "store-if-less",
  "store-if-equal",
]

def load_input():
  with open("input7.txt") as f:
    line = f.readline()
    # line = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
    # line = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
    return [int(x) for x in line.split(",")]

instruction_arr = load_input()

class AmplifierState:
  def __init__(self, amplifier_idx, phase_setting):
    self.amplifier_idx = amplifier_idx
    self.instruction_arr = list(instruction_arr)
    self.input_array = [phase_setting]
    self.idx = 0

def calculate(state):
  arr = state.instruction_arr
  output_array = []

  counter = 0
  while True:
    finished = False

    idx = state.idx
    opcode = arr[idx] % 100
    first_mode = int((arr[idx] / 100) % 10) == 0
    second_mode = int((arr[idx] / 1000) % 10) == 0
    third_mode = int((arr[idx] / 10000) % 10) == 0

    if opcode == 1:
      first = arr[arr[idx + 1]] if first_mode else arr[idx + 1]
      second = arr[arr[idx + 2]] if second_mode else arr[idx + 2]
      store = arr[idx + 3]
      arr[store] = first + second
      state.idx += 4
    elif opcode == 2:
      first = arr[arr[idx + 1]] if first_mode else arr[idx + 1]
      second = arr[arr[idx + 2]] if second_mode else arr[idx + 2]
      store = arr[idx + 3]
      arr[store] = first * second
      state.idx += 4
    elif opcode == 3:
      store = arr[idx + 1]
      arr[store] = state.input_array.pop(0)
      state.idx += 2
    elif opcode == 4:
      output = arr[arr[idx + 1]] if first_mode else arr[idx + 1]
      output_array.append(output)
      state.idx += 2
      finished = True
    elif opcode == 5:
      first = arr[arr[idx + 1]] if first_mode else arr[idx + 1]
      second = arr[arr[idx + 2]] if second_mode else arr[idx + 2]
      if first != 0:
        state.idx = second
      else:
        state.idx += 3
    elif opcode == 6:
      first = arr[arr[idx + 1]] if first_mode else arr[idx + 1]
      second = arr[arr[idx + 2]] if second_mode else arr[idx + 2]
      if first == 0:
        state.idx = second
      else:
        state.idx += 3
    elif opcode == 7:
      first = arr[arr[idx + 1]] if first_mode else arr[idx + 1]
      second = arr[arr[idx + 2]] if second_mode else arr[idx + 2]
      store = arr[idx + 3]
      arr[store] = 1 if first < second else 0
      state.idx += 4
    elif opcode == 8:
      first = arr[arr[idx + 1]] if first_mode else arr[idx + 1]
      second = arr[arr[idx + 2]] if second_mode else arr[idx + 2]
      store = arr[idx + 3]
      arr[store] = 1 if first == second else 0
      state.idx += 4
    else:
      print(f"last op code was {arr[idx]}")
      return (True, None)

    # print(f"{state.amplifier_idx} executed [{OPCODE_MAPPING[opcode]} - {opcode}] at {idx}, moving to {state.idx}")

    if finished:
      break

  return (False, output_array[0])

def meta_calculate(phase_settings):
  amplifier_states = list(AmplifierState(idx, phase_settings[idx]) for idx in range(0, 5))
  
  output = 0
  amplifier_idx = 0
  while True:
    amplifier_state = amplifier_states[amplifier_idx]

    amplifier_state.input_array.append(output)

    input_copy = list(amplifier_state.input_array)

    last_output = output

    (complete, output) = calculate(amplifier_state)
    if complete:
      return last_output

    print(f"({amplifier_idx}): {input_copy} => [{output}]")

    amplifier_idx = (amplifier_idx + 1) % 5

outputs = []
for i in permutations([9, 8, 7, 6, 5]):
# for i in permutations([5, 6, 7, 8, 9]):
  output = meta_calculate(i)
  if output is None:
    breakpoint()
  outputs.append(output)

print(max(outputs))
