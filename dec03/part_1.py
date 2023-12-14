from functools import reduce
import string
import re

def parse_input_schematic():
  input_file = open('input.txt', 'r')
  input = input_file.read()
  lines = input.strip().split('\n')
  return lines

def calculate_line_schematics(line, line_index, lines):
  digit_starting_index = None
  digit_in_schematic = False
  digits_in_line = []
  for i, c in enumerate(line):
    if c.isdigit():
      if digit_in_schematic:
        # check if last digit
        if i + 1 == len(line):
          digits_in_line.append(int(line[digit_starting_index:]))
        continue

      if digit_starting_index is None:
        digit_starting_index = i

      if is_adjacent_to_symbols(line_index, i, lines):
        digit_in_schematic = True
    else:
      if digit_in_schematic:
        digits_in_line.append(int(line[digit_starting_index:i]))
      digit_in_schematic = False
      digit_starting_index = None
  return digits_in_line

def is_adjacent_to_symbols(line_index, char_index, lines):
  punctuation = re.sub('\.', '', string.punctuation)

  # check previous line for symbols
  if line_index > 0:
    if char_index > 0:
      if lines[line_index-1][char_index - 1] in punctuation:
        return True
    if char_index + 1 < len(lines[line_index]):
      if lines[line_index-1][char_index + 1] in punctuation:
        return True
    if lines[line_index-1][char_index] in punctuation:
      return True

  # check next line for symbols
  if line_index + 1 < len(lines):
    if char_index > 0:
      if lines[line_index+1][char_index - 1] in punctuation:
        return True
    if char_index + 1 < len(lines[line_index]):
      if lines[line_index+1][char_index + 1] in punctuation:
        return True
    if lines[line_index+1][char_index] in punctuation:
      return True

  # check current line for symbols
  if char_index > 0:
    if lines[line_index][char_index - 1] in punctuation:
      return True
  if char_index + 1 < len(lines[line_index]):
    if lines[line_index][char_index + 1] in punctuation:
      return True
  return False

def sum_schematics(schematics):
  return reduce(lambda x, y: x + y, schematics)

if __name__ == '__main__':
  lines = parse_input_schematic()
  schematics_by_line = [calculate_line_schematics(line, i, lines) for i, line in enumerate(lines) ]
  schematics = [num for nums in schematics_by_line for num in nums]
  game_sum = sum_schematics(schematics)

  print(game_sum)
