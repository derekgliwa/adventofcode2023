import re


def parse_input():
  input_file = open('input.txt', 'r')
  input = input_file.read()
  directions_text, mappings_text = input.strip().split('\n\n')
  directions = directions_text.strip()
  mappings = parse_mappings(mappings_text)
  return (directions, mappings)

def parse_mappings(mappings_text):
  mapping_lines = re.split('\n', mappings_text)
  graph = {}
  for line in mapping_lines:
    (start, left, right) = re.match('^(\w+).*\((\w+),\s+(\w+)\)', line).groups()
    graph[start] = { 'L': left, 'R': right}
  return graph

if __name__ == '__main__':
  directions, mappings = parse_input()
  current_node = 'AAA'
  turn_count = 0
  while current_node != 'ZZZ':
    direction = directions[turn_count % len(directions)]
    current_node = mappings[current_node][direction]
    turn_count = turn_count + 1

  print(turn_count)










