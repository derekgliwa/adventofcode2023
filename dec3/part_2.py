from functools import reduce

def parse_input_schematic():
  input_file = open('input.txt', 'r')
  input = input_file.read()
  lines = input.strip().split('\n')
  return lines

def find_all_gears(line):
  indices = []
  for i, c in enumerate(line):
    if c == '*':
      indices.append(i)
  return indices

def calculate_gear_ratio(line_index, gear_index, lines):
  multipliers = []
  line = lines[line_index]

  # checking line above
  # if the middle char is a digit we know that there's just one number above (same for below)
  if line_index > 0:
    line_above = lines[line_index - 1]
    middle_char = line_above[gear_index]
    if middle_char.isdigit():
      lower_index = find_lower_bound(line_above, gear_index)
      upper_index = find_upper_bound(line_above, gear_index)
      multipliers.append(line_above[lower_index:upper_index+1])
    else:
      if gear_index > 0 and line_above[gear_index - 1].isdigit():
        lower_index = find_lower_bound(line_above, gear_index - 1)
        multipliers.append(line_above[lower_index:gear_index])
      if gear_index + 1 < len(line_above) and line_above[gear_index + 1].isdigit():
        upper_index = find_upper_bound(line_above, gear_index + 1)
        multipliers.append(line_above[gear_index + 1:upper_index + 1])

  # checking current line
  if gear_index > 0 and line[gear_index - 1].isdigit():
    lower_index = find_lower_bound(line, gear_index - 1)
    multipliers.append(line[lower_index:gear_index])
  if gear_index + 1 < len(line) and line[gear_index + 1].isdigit():
    upper_index = find_upper_bound(line, gear_index + 1)
    multipliers.append(line[gear_index + 1:upper_index + 1])

  # checking line below
  if line_index + 1 < len(lines):
    line_below = lines[line_index + 1]
    middle_char = line_below[gear_index]
    if middle_char.isdigit():
      lower_index = find_lower_bound(line_below, gear_index)
      upper_index = find_upper_bound(line_below, gear_index)
      multipliers.append(line_below[lower_index:upper_index+1])
    else:
      if gear_index > 0 and line_below[gear_index - 1].isdigit():
        lower_index = find_lower_bound(line_below, gear_index - 1)
        multipliers.append(line_below[lower_index:gear_index])
      if gear_index + 1 < len(line_below) and line_below[gear_index + 1].isdigit():
        upper_index = find_upper_bound(line_below, gear_index + 1)
        multipliers.append(line_below[gear_index + 1:upper_index + 1])
    if len(multipliers) < 2:
      return 0
    return reduce(lambda x, y: x * y, map(lambda x: int(x), multipliers))

def find_lower_bound(line, index):
  if index == 0:
    return index
  while index > 0:
    if line[index - 1].isdigit():
      index = index - 1
    else:
      return index
  return index

def find_upper_bound(line, index):
  if index + 1 == len(line):
    return index
  while index + 1 < len(line):
    if line[index + 1].isdigit():
      index = index + 1
    else:
      return index
  return index

def sum_ratios(gear_ratios):
  return reduce(lambda x, y: x + y, gear_ratios)

if __name__ == '__main__':
  lines = parse_input_schematic()
  gears_by_line = [find_all_gears(line) for line in lines]
  gear_ratios = [calculate_gear_ratio(line_index, gear_index, lines) for line_index, line_gears in enumerate(gears_by_line) for gear_index in line_gears]

  game_sum = sum_ratios(gear_ratios)
  print(game_sum)
