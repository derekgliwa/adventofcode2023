import re

def parse_mappings():
  input_file = open('test_input.txt', 'r')
  input = input_file.read()
  lines = input.strip().split('\n\n')
  seeds = list(map(lambda x: int(x), re.split('\s', lines[0])[1:]))
  seeds_with_ranges = zip(seeds[::2], seeds[1::2])
  maps_in_order = map(lambda x: parse_mapping(x), lines[1:])
  return { 'seeds': seeds_with_ranges, 'maps_in_order': maps_in_order }

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

def find_seed_options(seed_range, mappings):
  min_seed = seed_range[0]
  max_seed = seed_range[1]
  if len(mappings) == 0:
    return { min_seed }

  seed_options = set()
  for mapping in mappings[0]:
    if min_seed >= mapping['source'] and max_seed < mapping['source'] + mapping['count']:
      seed_options.add(min_seed)
      return seed_options
    elif min_seed >= mapping['source'] and max_seed >= mapping['source'] + mapping['count']:
      seed_options.add(min_seed)
      min_seed = mapping['source'] + mapping['count']
    elif min_seed < mapping['source']:
      if max_seed < mapping['source']:
        return seed_options.union(find_seed_options((min_seed, max_seed), mappings[1:]))
      elif max_seed >= mapping['source'] and max_seed < mapping['source'] + mapping['count']:
        seed_options.union(find_seed_options(min_seed, mapping['source'] - 1), mappings[1:])
        seed_options.add(mapping['source'])
      elif max_seed >= mapping['source'] and max_seed >= mapping['source'] + mapping['count']:
        seed_options.union(find_seed_options(min_seed, mapping['source'] - 1), mappings[1:])
        seed_options.add(mapping['source'])
        min_seed = mapping['source'] + mapping['count']
  if min_seed != max_seed:
    seed_options.add(min_seed)
  return seed_options

if __name__ == '__main__':
  mappings = parse_mappings()
  final_locations = []
  mappings_in_order = list(mappings['maps_in_order'])
  for seed, seed_range in list(mappings['seeds']):
    seed_options = find_seed_options((seed, seed + seed_range - 1), mappings_in_order)
    print('seed_options')
    print(seed_options)
    for seed in seed_options:
      print(seed)
      start = seed
      for sorted_mappings in mappings_in_order:
        for mapping in sorted_mappings:
          if start >= mapping['source'] and start < mapping['source'] + mapping['count']:
            start = start + (mapping['destination'] - mapping['source'])
            break
      final_locations.append(start)
  print(min(final_locations))

