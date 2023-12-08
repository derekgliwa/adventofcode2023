import re
from functools import reduce


def parse_hands():
  input_file = open('input.txt', 'r')
  input = input_file.read()
  lines = input.strip().split('\n')
  return map(lambda x: parse_hand(x), lines)

def parse_hand(line):
  cards, wager = re.split('\s+', line)
  wager = int(wager)
  return { 'cards': cards, 'wager': wager, 'score': score_hand(cards) }

def score_hand(hand):
  cards = {}
  for card in hand:
    if card in cards:
      cards[card] = cards[card] + 1
    else:
      cards[card] = 1
  counts = list(cards.values())
  count_max = max(counts)
  count_min = min(counts)
  if count_max == 5:
    return convert_to_decimal('A' + hand)
  if count_max == 4:
    return convert_to_decimal('K' + hand)
  elif count_max == 3 and count_min == 2:
    return convert_to_decimal('Q' + hand)
  elif count_max == 3 and count_min == 1:
    return convert_to_decimal('J' + hand)
  elif count_max == 2 and len(counts) == 3:
    return convert_to_decimal('T' + hand)
  elif count_max == 2 and len(counts) == 4:
    return convert_to_decimal('9' + hand)
  else:
    return convert_to_decimal('8' + hand)

def convert_to_decimal(hand):
  vals = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    '1': 1
  }
  val = 0
  for i,c in enumerate(reversed(hand)):
    val = val + vals[c] * 14**i
  return val


if __name__ == '__main__':
  hands = parse_hands()

  hands = sorted(hands, key=lambda hand: hand['score'])
  score = reduce(lambda x,y: x + y, [(i+1) * hand['wager'] for i, hand in enumerate(hands)])

  print(score)





