import re
from functools import reduce
import numpy as np

def parse_input():
  input_file = open('test_input.txt', 'r')
  input = input_file.read()
  grids = input.strip().split('\n\n')
  return [[[0 if c == '.' else 1 for c in line] for line in re.split('\n', grid)] for grid in grids]

def calculate_symmetry(grid, index):
  npgrid = np.array(grid)
  grid_length = len(npgrid)
  for i in range(1, (grid_length//2) + 1):
    if abs((npgrid[:i][::-1] - npgrid[i:i+i])).sum() == 1:
      return i * 100
    if abs((npgrid[grid_length - i * 2:-i][::-1] - npgrid[-i:])).sum() == 1:
      return (grid_length - i) * 100
  npgrid = npgrid.transpose()
  grid_length = len(npgrid)
  for i in range(1, (grid_length//2) + 1):
    if abs((npgrid[:i][::-1] - npgrid[i:i+i])).sum() == 1:
      return i
    if abs((npgrid[grid_length - i * 2:-i][::-1] - npgrid[-i:])).sum() == 1:
      return (grid_length - i)
  print(index)
  raise "ERROR"


if __name__ == '__main__':
  grids = parse_input()
  scores = [calculate_symmetry(grid, i) for i, grid in enumerate(grids)]
  for score in scores:
    print(score)
  symmetries = reduce(lambda x, y: x + y, scores)
  print(symmetries)
