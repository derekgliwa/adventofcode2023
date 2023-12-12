from functools import reduce

def parse_input():
  input_file = open('input.txt', 'r')
  input = input_file.read()
  lines = input.strip().split('\n')

  i = 0
  while i < len(lines):
    row_has_galaxy = False
    for j in range(len(lines[i])):
      if lines[i][j] == '#':
        row_has_galaxy = True
        break
    if not row_has_galaxy:
      lines.insert(i, ''.join(['.' for k in range(len(lines[i]))]))
      i = i + 1
    i = i + 1

  i = 0
  while i < len(lines[0]):
    column_has_galaxy = False
    for j in range(len(lines)):
      if lines[j][i] == '#':
        column_has_galaxy = True
        break
    if not column_has_galaxy:
      for j in range(len(lines)):
        lines[j] = lines[j][0:i] + '.' + lines[j][i:]
      i = i + 1
    i = i + 1
  return lines

def plot_galaxies(universe):
  galaxies = []
  for i in range(len(universe)):
    universe_row = universe[i]
    for j in range(len(universe_row)):
      if universe_row[j] == '#':
        galaxies.append((i, j))
  return galaxies

if __name__ == '__main__':
  universe = parse_input()
  galaxies = list(plot_galaxies(universe))
  min_distances = []
  for i in range(len(galaxies)):
    galaxy = galaxies[i]
    for j in range(i + 1, len(galaxies)):
      other_galaxy = galaxies[j]
      min_distance = abs(galaxy[0] - other_galaxy[0]) + abs(galaxy[1] - other_galaxy[1])
      min_distances.append(min_distance)
  print(reduce(lambda x, y: x + y, min_distances))



