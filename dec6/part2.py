import re

def parse_race():
  input_file = open('input.txt', 'r')
  input = input_file.read()
  lines = input.strip().split('\n')
  time = int(''.join(re.split('\s+', lines[0])[1:]))
  distance = int(''.join(re.split('\s+', lines[1])[1:]))
  return (time, distance)

if __name__ == '__main__':
  race = parse_race()

  valid_races = len(list(filter(lambda x: x, [i*(race[0] - i) > race[1] for i in range(race[0])])))
  print(valid_races)


