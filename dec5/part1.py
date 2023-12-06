import re

def parse_mappings():
  input_file = open('input.txt', 'r')
  input = input_file.read()
  lines = input.strip().split('\n\n')
  seeds = map(lambda x: int(x), re.split('\s', lines[0])[1:])
  maps_in_order = map(lambda x: parse_mapping(x), lines[1:])
  return { 'seeds': seeds, 'maps_in_order': maps_in_order }

def parse_mapping(mapping):
  mappings = list(map(lambda x: calculate_mapping_row(x), re.split('\n', mapping)[1:]))
  return sorted(mappings, key=lambda x: x['source'])

def calculate_mapping_row(row):
  destination, source, count = re.split('\s', row)
  return {
    'destination': int(destination),
    'source': int(source),
    'count': int(count)
  }


if __name__ == '__main__':
  mappings = parse_mappings()
  final_locations = []
  mappings_in_order = list(mappings['maps_in_order'])
  for seed in list(mappings['seeds']):
    start = seed
    for sorted_mappings in mappings_in_order:
      for mapping in sorted_mappings:
        if start >= mapping['source'] and start < mapping['source'] + mapping['count']:
          start = start + (mapping['destination'] - mapping['source'])
          break
    final_locations.append(start)
  print(min(final_locations))

  # prEEt(scratchers)
  # scratchers_total = reduce(lambda x, y: x + y, [score_scratcher(scratcher) for scratcher in scratchers])
  # print(scratchers_total)

