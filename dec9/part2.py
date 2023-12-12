import re
from functools import reduce


def parse_input():
  input_file = open('input.txt', 'r')
  input = input_file.read()
  lines = input.strip().split('\n')
  return list(map(lambda x: [int(y) for y in re.split('\s+', x)], lines))

def predict_next(environmental_report):
  row_structure = [environmental_report] + build_next_rows(environmental_report)
  calculate_next_vals(row_structure)
  print(row_structure)
  return row_structure[0][0]



def build_next_rows(report_row):
  next_row = []
  for i in range(len(report_row) - 1):
    next_row.append(report_row[i + 1] - report_row[i])
  if all([x == 0 for x in next_row]):
    return [next_row]
  else:
    return  [next_row] + build_next_rows(next_row)

def calculate_next_vals(row_structure):
  for i in reversed(range(1, len(row_structure))):
    upper_row = row_structure[i-1]
    lower_row = row_structure[i]
    if all([x == 0 for x in lower_row]):
      lower_row.append(0)
    upper_row.insert(0, upper_row[0] - lower_row[0])


if __name__ == '__main__':
  environmental_reports = parse_input()
  next_vals = [predict_next(x) for x in environmental_reports]

  print(reduce(lambda x,y: x + y, next_vals))
