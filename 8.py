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

image = []
for pixel_idx in range(0, 25 * 6):
  for layer_idx in range(0, num_layers):
    color = layers[layer_idx][pixel_idx]
    if color == 2:
      continue
    image.append(color)
    break

for i in range(0, 6):
  for j in range(0, 25):
    color = image[i * 25 + j]
    print("X" if color == 1 else " ", end="")
  print()
