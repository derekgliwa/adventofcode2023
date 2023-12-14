from functools import reduce
import re

input = """"""
# input = """1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# three7938"""

def find_first_digit(line):
  digits = re.findall(r"(\d)", line)
  if digits != []:
    return digits[0]
  else:
    raise Exception("ERROR")

def find_last_digit(line):
  digits = re.findall(r"(\d)", line)
  if digits != []:
    return digits[len(digits) - 1]
  else:
    raise Exception("ERROR")

def line_number(line):
  if len(line) == 0:
    return 0
  first_digit = find_first_digit(line)
  last_digit = find_last_digit(line)
  return int(first_digit + last_digit)

def split_input_into_lines(input):
  return input.split('\n')

if __name__ == '__main__':
  input_file = open('input.txt', 'r')
  input = input_file.read()
  print(type(input))
  lines = split_input_into_lines(input)
  print(len(lines))
  lines_as_numbers = map(lambda line: line_number(line), lines)
  lines_sum = reduce(lambda x, y: x + y, lines_as_numbers)
  print(lines_sum)
