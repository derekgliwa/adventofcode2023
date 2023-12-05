from functools import reduce
import re

def parse_scratchers():
  input_file = open('input.txt', 'r')
  input = input_file.read()
  lines = input.strip().split('\n')
  return map(lambda line: parse_scratcher(line), lines)

def parse_scratcher(scratcher_line):
  _, game = scratcher_line.split(':')
  game_numbers_line, winning_numbers_line = game.strip().split('|')
  game_numbers = re.split('\s+', game_numbers_line.strip())
  winning_numbers = re.split('\s+', winning_numbers_line.strip())
  return { 'game_numbers': map(lambda x: int(x), game_numbers), 'winning_numbers': { s for s in map(lambda x: int(x), winning_numbers) } }

def score_scratcher(scratcher):
  matching_numbers = []
  game_numbers = scratcher['game_numbers'] # a list
  winning_numbers = scratcher['winning_numbers'] # a set
  for n in game_numbers:
    if n in winning_numbers:
      matching_numbers.append(n)
  return 2 ** (len(matching_numbers) - 1) if len(matching_numbers) > 0 else 0

if __name__ == '__main__':
  scratchers = parse_scratchers()
  print(scratchers)
  scratchers_total = reduce(lambda x, y: x + y, [score_scratcher(scratcher) for scratcher in scratchers])
  print(scratchers_total)
