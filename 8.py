def load_input():
  with open("input8.txt") as f:
    line = f.readline()
    return [int(x) for x in line.strip()]

pixels = load_input()

num_layers = int(len(pixels) / (25 * 6))

layers = []
idx = 0
for i in range(0, num_layers):
  start_idx = i * (25 * 6)
  end_idx = start_idx + 25 * 6
  layers.append(pixels[start_idx : end_idx])

min_num_zeros = float("inf")
min_layer_idx = -1
for i in range(0, len(layers)):
  num_zeros = sum([1 for x in layers[i] if x == 0]) 
  if num_zeros <= min_num_zeros:
    min_num_zeros = num_zeros
    min_layer_idx = i

num_ones = sum([1 for x in layers[min_layer_idx] if x == 1])
num_twos = sum([1 for x in layers[min_layer_idx] if x == 2])

value = num_ones * num_twos

print(value)
