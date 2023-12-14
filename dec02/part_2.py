from functools import reduce
import re

def parse_input_into_game_data():
  input_file = open('input.txt', 'r')
  input = input_file.read()
  lines = input.strip().split('\n')
  return map(lambda line: parse_game(line), lines)

def parse_game(line):
  game, results = line.split(':')
  _, game_id = re.split('\s', game)
  pulls = results.strip().split(';')
  formatted_pulls = map(lambda pull: parse_pull(pull), pulls)
  return { 'game_id': game_id, 'color_results': formatted_pulls }

def parse_pull(pull):
  color_pull = pull.split(',')
  colors = {}
  for cp in color_pull:
    count, color = cp.strip().split(' ')
    colors[color] = int(count)
  return colors

def calculate_game_power_sets(games):
  return map(lambda game: calculate_game_power_set(game), games)

def calculate_game_power_set(game):
  min_red = 0
  min_blue = 0
  min_green = 0
  for pull in game['color_results']:
    if ('blue' in pull and pull['blue'] > min_blue):
      min_blue = pull['blue']
    if 'red' in pull and pull['red'] > min_red:
      min_red = pull['red']
    if 'green' in pull and pull['green'] > min_green:
      min_green = pull['green']

  if min_green == 0 or min_red == 0 or min_blue == 0:
    print(game['game_id'])
    raise Exception('ERROR')
  return min_green * min_blue * min_red

def sum_power_sets(game_power_sets):
  return reduce(lambda x, y: x + y, game_power_sets)

if __name__ == '__main__':
  games = parse_input_into_game_data()
  power_sets = calculate_game_power_sets(games)
  game_sum = sum_power_sets(power_sets)

  print(game_sum)
