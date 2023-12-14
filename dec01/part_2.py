from functools import reduce
import re

input = """"""
# input = """1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# three7938"""

digit_mapping = {
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9",
}

reverse_digit_mapping = {
  "eno": "1",
  "owt": "2",
  "eerht": "3",
  "ruof": "4",
  "evif": "5",
  "xis": "6",
  "neves": "7",
  "thgie": "8",
  "enin": "9",
}

def find_first_digit(line):
  digits = re.findall(r"(\d|one|two|three|four|five|six|seven|eight|nine)", line)
  if digits != []:
    print(digits)
    digit = digits[0]
    if digit in digit_mapping:
      digit = digit_mapping[digit]
    return digit
  else:
    raise Exception("ERROR")

def find_last_digit(line):
  digits = re.findall(r"(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)", line[::-1])
  if digits != []:
    print(digits)
    digit = digits[0]
    if digit in reverse_digit_mapping:
      digit = reverse_digit_mapping[digit]
    return digit
  else:
    raise Exception("ERROR")

def line_number(line):
  if len(line) == 0:
    return 0
  first_digit = find_first_digit(line)
  last_digit = find_last_digit(line)
  print (first_digit + last_digit)
  return int(first_digit + last_digit)

def split_input_into_lines(input):
  return input.split('\n')

if __name__ == '__main__':
  # input_file = open('part_2_text_input.txt', 'r')
  input_file = open('input.txt', 'r')
  input = input_file.read()
  lines = split_input_into_lines(input)
  lines_as_numbers = map(lambda line: line_number(line), lines)
  lines_sum = reduce(lambda x, y: x + y, lines_as_numbers)
  print(lines_sum)
