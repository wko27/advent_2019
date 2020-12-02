import math

from itertools import permutations, repeat

PROGRAM_SIZE = 1024

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
  "adjust-relative-base",
]

def load_input():
  with open("input9.txt") as f:
    line = f.readline()
    # line = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
    # line = "1102,34915192,34915192,7,4,7,99,0"
    # line = "104,1125899906842624,99"
    return [int(x) for x in line.split(",")]

instruction_arr = load_input()

class AmplifierState:
  def __init__(self, amplifier_idx):
    self.amplifier_idx = amplifier_idx
    self.instruction_arr = list(instruction_arr) + list(repeat(0, PROGRAM_SIZE))
    self.input_array = []
    self.output_array = []
    self.idx = 0
    self.relative_base_offset = 0

  def get_store_address(self, modes, arr, idx, offset):
    if modes[offset] == 0:
      # position mode
      return arr[idx + offset]
    elif modes[offset] == 1:
      # parameter mode
      return arr[idx + offset]
    elif modes[offset] == 2:
      # relative mode
      return arr[idx + offset] + self.relative_base_offset

  def get_value(self, modes, arr, idx, offset):
    if modes[offset] == 0:
      # position mode
      return arr[arr[idx + offset]]
    elif modes[offset] == 1:
      # parameter mode
      return arr[idx + offset]
    elif modes[offset] == 2:
      # relative mode
      return arr[arr[idx + offset] + self.relative_base_offset]

def calculate(state):
  arr = state.instruction_arr

  counter = 0
  while True:
    finished = False

    idx = state.idx
    opcode = arr[idx] % 100
    modes = [None]
    modes.append(int((arr[idx] / 100) % 10))
    modes.append(int((arr[idx] / 1000) % 10))
    modes.append(int((arr[idx] / 10000) % 10))

    if opcode == 1:
      first = state.get_value(modes, arr, idx, 1)
      second = state.get_value(modes, arr, idx, 2)
      store = state.get_store_address(modes, arr, idx, 3)
      arr[store] = first + second
      state.idx += 4
    elif opcode == 2:
      first = state.get_value(modes, arr, idx, 1)
      second = state.get_value(modes, arr, idx, 2)
      store = state.get_store_address(modes, arr, idx, 3)
      arr[store] = first * second
      state.idx += 4
    elif opcode == 3:
      store = state.get_store_address(modes, arr, idx, 1)
      arr[store] = state.input_array.pop(0)
      state.idx += 2
    elif opcode == 4:
      first = state.get_value(modes, arr, idx, 1)
      state.output_array.append(first)
      state.idx += 2
      finished = True
    elif opcode == 5:
      first = state.get_value(modes, arr, idx, 1)
      second = state.get_value(modes, arr, idx, 2)
      if first != 0:
        state.idx = second
      else:
        state.idx += 3
    elif opcode == 6:
      first = state.get_value(modes, arr, idx, 1)
      second = state.get_value(modes, arr, idx, 2)
      if first == 0:
        state.idx = second
      else:
        state.idx += 3
    elif opcode == 7:
      first = state.get_value(modes, arr, idx, 1)
      second = state.get_value(modes, arr, idx, 2)
      store = state.get_store_address(modes, arr, idx, 3)
      arr[store] = 1 if first < second else 0
      state.idx += 4
    elif opcode == 8:
      first = state.get_value(modes, arr, idx, 1)
      second = state.get_value(modes, arr, idx, 2)
      store = state.get_store_address(modes, arr, idx, 3)
      arr[store] = 1 if first == second else 0
      state.idx += 4
    elif opcode == 9:
      first = state.get_value(modes, arr, idx, 1)
      state.relative_base_offset += first
      state.idx += 2
    else:
      print(f"last op code was {arr[idx]}")
      return (True, None)

    # print(f"{state.amplifier_idx} executed [{OPCODE_MAPPING[opcode]} - {opcode}] at {idx}, moving to {state.idx}")

    if finished:
      break

  return (False, state.output_array[0])

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

breakpoint()
state = AmplifierState(0)
state.input_array.append(2)
calculate(state)

print(state.output_array)
