import re
import math

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

def calculate_turn_count(current_node, directions, mappings):
  turn_count = 0
  while not current_node.endswith('Z'):

    direction = directions[turn_count % len(directions)]
    current_node = mappings[current_node][direction]
    turn_count = turn_count + 1
  return turn_count

if __name__ == '__main__':
  directions, mappings = parse_input()
  nodes = mappings.keys()
  current_nodes = list(filter(lambda x: x.endswith('A'), nodes))
  print(current_nodes)
  count_for_nodes = list(map(lambda x: calculate_turn_count(x, directions, mappings), current_nodes))

  print(math.lcm(*count_for_nodes))










