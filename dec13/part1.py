import re
from functools import reduce


def parse_input():
  input_file = open('input.txt', 'r')
  input = input_file.read()
  grids = input.strip().split('\n\n')
  return [re.split('\n', grid) for grid in grids]

def calculate_symmetry(grid):
  for i in range(1, len(grid[0])):
    if all([is_row_symmetric_at_i(row, i) for row in grid]):
      return i
  for i in range(1, len(grid)):
    rotated_grid = [[row[i] for row in grid] for i in range(len(grid[0]))]
    if all([is_row_symmetric_at_i(row, i) for row in rotated_grid]):
      return i * 100
  raise "ERROR"


def is_row_symmetric_at_i(row, i):
  j = i - 1
  k = i
  while j >= 0 and k < len(row):
    if row[j] != row[k]:
      return False
    j = j - 1
    k = k + 1
  return True

if __name__ == '__main__':
  grids = parse_input()
  symmetries = reduce(lambda x, y: x + y, [calculate_symmetry(grid) for grid in grids])
  print(symmetries)










