import re
from functools import reduce
from operator import mul

def parse_races():
  input_file = open('input.txt', 'r')
  input = input_file.read()
  lines = input.strip().split('\n')
  times = map(lambda x: int(x), re.split('\s+', lines[0])[1:])
  distances = map(lambda x: int(x), re.split('\s+', lines[1])[1:])
  return list(zip(times, distances))

if __name__ == '__main__':
  races = parse_races()
  print(races)

  valid_races = map(lambda race: len(list(filter(lambda x: x, [i*(race[0] - i) > race[1] for i in range(race[0])]))), races)
  total = reduce(mul, valid_races, 1)
  print(total)


