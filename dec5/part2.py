import re

def parse_mappings():
  input_file = open('test_input.txt', 'r')
  input = input_file.read()
  lines = input.strip().split('\n\n')
  seeds = list(map(lambda x: int(x), re.split('\s', lines[0])[1:]))
  seeds_with_ranges = zip(seeds[::2], seeds[1::2])
  maps_in_order = list(map(lambda x: parse_mapping(x), lines[1:]))
  return { 'seeds': seeds_with_ranges, 'maps_in_order': maps_in_order }

def parse_mapping(mapping):
  mappings = list(map(lambda x: calculate_mapping_row(x), re.split('\n', mapping)[1:]))
  sorted_mappings = sorted(mappings, key=lambda x: x['source'])
  final_mappings = []
  for i in range(len(sorted_mappings)):
    current_mapping = sorted_mappings[i]

    if i == 0 and current_mapping['source'] > 0:
      final_mappings.append({ 'source': 0, 'destination': 0, 'count': current_mapping['source'], 'destination_end': current_mapping['destination'] - 1, 'source_end': current_mapping['source'] - 1})
    if i >= 0 and i < len(sorted_mappings) - 1:
      next_mapping = sorted_mappings[i+1]
      if current_mapping['source'] + current_mapping['count'] < next_mapping['source']:
        gap_mapping = { 'source': current_mapping['source'] + current_mapping['count'], 'destination': current_mapping['source'] + current_mapping['count'], 'count': next_mapping['source'] - (current_mapping['source'] + current_mapping['count']) }
        final_mappings.append(gap_mapping)
    final_mappings.append(current_mapping)
  return final_mappings

def flatten_mapping(mappings):
  flattened_mappings = mappings[0]
  for i in range(1, len(mappings[0:2])):
    sorted_mapping = mappings[i]
    flattened_mappings = sorted(flattened_mappings, key=lambda x: x['destination'])
    for mapping in sorted_mapping:
      for j in range(len(flattened_mappings)):
        # print(j)
        print(flattened_mappings)
        mapping_for_compare = flattened_mappings[j]
        if mapping['source'] >= mapping_for_compare['destination']:
          if mapping['source'] != mapping_for_compare['destination']: # insert one before overlap
            new_mapping_count = mapping['source'] - mapping_for_compare['destination']
            source_end= mapping_for_compare['source'] + new_mapping_count -1
            destination_end= mapping_for_compare['destination'] + new_mapping_count -1
            flattened_mappings = flattened_mappings[0:j] +[{ 'source': mapping_for_compare['source'], 'destination': mapping_for_compare['destination'], 'count': new_mapping_count, 'destination_end': destination_end, 'source_end': source_end }] + flattened_mappings[j:]
            j = j + 1
            mapping_for_compare = flattened_mappings[j]
            mapping_for_compare['source'] = source_end + 1
            mapping_for_compare['destination'] = destination_end + 1

          if mapping['source_end'] < mapping_for_compare['destination_end']: # split into two
            mapping_for_compare['source'] = mapping_for_compare['source'] + mapping['count']
            mapping_for_compare['destination'] = mapping_for_compare['destination'] + mapping['count']
            flattened_mappings = flattened_mappings[0:j] + [mapping] + flattened_mappings[j:]
            j = j + 1

          elif mapping['source_end'] == mapping_for_compare['destination_end']: # replace
            mapping_for_compare['destination'] = mapping['destination']
            mapping_for_compare['destination_end'] = mapping['destination_end']
          # elif j + 1 < len(flattened_mappings): # dip into the next one
          #   print('HELLOOOOO')
          #   next_to_replace = flattened_mappings[j + 1]
          #   while (mapping['source_end'] > next_to_replace['destination_end']):
          #     if j + 1 >= len(flattened_mappings):
          #       next_to_replace = None
          #       break
          #     deleted_mapping = flattened_mappings.pop(j + 1)
          #     mapping_for_compare['source_end'] = deleted_mapping['source_end']
          #     next_to_replace = flattened_mappings[j + 1]
          #   if next_to_replace != None:
          #     mapping_for_compare['destination'] = mapping['destination']
          #     mapping_for_compare['destination_end'] = mapping['destination_end']
          #     next_to_replace['source'] = mapping_for_compare['source_end'] + 1
          else: # end of the road
            mapping_for_compare['destination'] = mapping['destination']
            mapping_for_compare['destination_end'] = mapping['destination_end']
  flattened_mappings = sorted(flattened_mappings, key=lambda x: x['source'])
  return flattened_mappings





def calculate_mapping_row(row):
  destination, source, count = re.split('\s', row)
  return {
    'destination': int(destination),
    'source': int(source),
    'count': int(count),
    'source_end': int(source) + int(count) - 1,
    'destination_end': int(destination) + int(count) - 1,
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
  flattened_mappings = flatten_mapping(mappings_in_order)
  print(flattened_mappings)
  # for seed, seed_range in list(mappings['seeds']):
  #   seed_options = find_seed_options((seed, seed + seed_range - 1), mappings_in_order)
  #   print('seed_options')
  #   print(seed_options)
  #   for seed in seed_options:
  #     print(seed)
  #     start = seed
  #     for sorted_mappings in mappings_in_order:
  #       for mapping in sorted_mappings:
  #         if start >= mapping['source'] and start < mapping['source'] + mapping['count']:
  #           start = start + (mapping['destination'] - mapping['source'])
  #           break
  #     final_locations.append(start)
  # print(min(final_locations))

