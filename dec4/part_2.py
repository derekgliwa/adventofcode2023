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
  return { 'game_numbers': map(lambda x: int(x), game_numbers), 'winning_numbers': { s for s in map(lambda x: int(x), winning_numbers) }, 'copies': 1 }

def score_scratcher(scratcher, scratcher_index, scratchers):
  match_count = 0
  game_numbers = scratcher['game_numbers'] # a list
  winning_numbers = scratcher['winning_numbers'] # a set
  for n in game_numbers:
    if n in winning_numbers:
      match_count = match_count + 1
  scratcher_copies = scratcher['copies']

  for i in range(scratcher_index + 1, scratcher_index + match_count + 1):
    scratchers[i]['copies'] = scratchers[i]['copies'] + (1 * scratcher_copies)

  return scratcher_copies

if __name__ == '__main__':
  scratchers = list(parse_scratchers())
  scratchers_total = reduce(lambda x, y: x + y, [score_scratcher(scratcher, i, scratchers) for i, scratcher in enumerate(scratchers)])
  print(scratchers_total)
