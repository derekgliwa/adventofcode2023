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
  # if hand == 'JJQK9' or hand == '23372':
  #   breakpoint()
  counts = list(cards.values())
  count_max = max(counts)
  count_min = min(counts)
  score_balancers = ['7', '8', '9', 'T', 'Q', 'K', 'A']
  score_balancer_index = 0
  if 'J' in cards:
    j_count = cards['J']
    del cards['J']
    counts = list(cards.values())
    if len(counts) == 0 or j_count == 4: # all cards are 'J'
      count_max = 5
    else:
      count_max = max(counts)
    if count_max == 5:
      score_balancer_index = 6
    elif count_max == 4: # 4 cards + 1 J
      score_balancer_index = 6
    elif count_max == 3: # 3 of a kind or full house - both upgraded to either 4 of a kind or 5 of a kind
      score_balancer_index = 4 + j_count
    elif count_max == 2: # pair or two pair
      if j_count == 3:
        score_balancer_index = 6
      elif j_count == 2:
        score_balancer_index = 5
      else:
        if len(counts) == 2:
          score_balancer_index = 4
        elif len(counts) == 3:
          score_balancer_index = 3
    else:
      if j_count == 1:
        score_balancer_index = 1
      elif j_count == 2:
        score_balancer_index = 3
      elif j_count == 3:
        score_balancer_index = 5
  else:
    if count_max == 5:
      score_balancer_index = 6
    if count_max == 4:
      score_balancer_index = 5
    elif count_max == 3 and count_min == 2:
      score_balancer_index = 4
    elif count_max == 3 and count_min == 1:
      score_balancer_index = 3
    elif count_max == 2 and len(counts) == 3:
      score_balancer_index = 2
    elif count_max == 2 and len(counts) == 4:
      score_balancer_index = 1
  return convert_to_decimal(score_balancers[score_balancer_index] + hand)

def convert_to_decimal(hand):
  vals = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'T': 11,
    '9': 10,
    '8': 9,
    '7': 8,
    '6': 7,
    '5': 6,
    '4': 5,
    '3': 4,
    '2': 3,
    '1': 2,
    'J': 1
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





