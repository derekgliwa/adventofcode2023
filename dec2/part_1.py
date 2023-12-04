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

def filter_invalid_games(games):
  return filter(lambda game: evaluate_game_validity(game), games)

def evaluate_game_validity(game):
  for pull in game['color_results']:
    if ('blue' in pull and pull['blue'] > 14) or ('red' in pull and pull['red'] > 12) or ('green' in pull and pull['green'] > 13):
      return False
  return True

def sum_valid_games(games):
  game_ids = map(lambda game: int(game['game_id']), games)
  return reduce(lambda x, y: x + y, game_ids)

if __name__ == '__main__':
  games = parse_input_into_game_data()
  valid_games = filter_invalid_games(games)
  game_sum = sum_valid_games(valid_games)

  print(game_sum)
