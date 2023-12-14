import re

def parse_mappings():
  input_file = open('input.txt', 'r')
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
      final_mappings.append({ 'source': 0, 'destination': 0, 'destination_end': current_mapping['source'] - 1, 'source_end': current_mapping['source'] - 1 })
    if i >= 0 and i < len(sorted_mappings) - 1:
      next_mapping = sorted_mappings[i+1]
      if current_mapping['source_end'] + 1 < next_mapping['source']:
        gap_mapping = { 'source': current_mapping['source_end'] + 1, 'destination': current_mapping['destination_end'] + 1, 'source_end': next_mapping['source'] - 1, 'destination_end': next_mapping['destination'] - 1 }
        final_mappings.append(gap_mapping)
        i = i + 1
    final_mappings.append(current_mapping)
  return final_mappings

def calculate_mapping_row(row):
  destination, source, count = re.split('\s', row)
  return {
    'destination': int(destination),
    'source': int(source),
    'source_end': int(source) + int(count) - 1,
    'destination_end': int(destination) + int(count) - 1,
  }

def flatten_mapping(mappings):
  while(len(mappings) > 1):
    mappings = [merge_rows(mappings[0], mappings[1])] + mappings[2:]
  return mappings[0]

def merge_rows(left_mapping, right_mapping):
  left_mapping = sorted(left_mapping, key=lambda x: x['destination'], reverse=True)
  right_mapping = sorted(right_mapping, key=lambda x: x['source'], reverse=True)
  merged_mappings = []
  while len(right_mapping) > 0 or len(left_mapping) > 0:
    if len(right_mapping) == 0:
      merged_mappings.append(left_mapping.pop())
      continue
    if len(left_mapping) == 0:
      merged_mappings.append(right_mapping.pop())
      continue
    right = right_mapping.pop()
    left = left_mapping.pop()
    if left['destination'] == right['source']: #start at same spot
      if left['destination_end'] == right['source_end']: # replace
        new_mapping = {
          'source': left['source'],
          'source_end': left['source_end'],
          'destination': right['destination'],
          'destination_end': right['destination_end']
        }
        merged_mappings.append(new_mapping)
        continue
      elif left['destination_end'] > right['source_end']: # use up all of right side
        # NEED TO DEAL W DELTA HERE
        delta = left['destination_end'] - right['source_end']
        new_mapping = {
          'source': left['source'],
          'source_end': left['source_end'] - delta,
          'destination': right['destination'],
          'destination_end': right['destination_end']
        }
        merged_mappings.append(new_mapping)
        left_mapping.append({
          'source': left['source'] + (right['source_end'] - right['source']) + 1,
          'source_end': left['source_end'] ,
          'destination': right['source_end'] + 1,
          'destination_end': left['destination_end']
        })
        continue
      elif left['destination_end'] < right['source_end']: # use up all of right side
        delta = right['source_end'] - left['destination_end']
        new_mapping = {
          'source': left['source'],
          'source_end': left['source_end'],
          'destination': right['destination'],
          'destination_end': right['destination_end'] - delta
        }
        merged_mappings.append(new_mapping)
        right_mapping.append({
          'source': left['destination_end'] + 1,
          'source_end': right['source_end'],
          'destination': right['destination_end'] - delta + 1,
          'destination_end': right['destination_end']
        })
        continue
  return merged_mappings

if __name__ == '__main__':
  mappings = parse_mappings()
  final_locations = []
  mappings_in_order = list(mappings['maps_in_order'])
  flattened_mappings = flatten_mapping(mappings_in_order)
  flattened_mappings = list(sorted(flattened_mappings, key=lambda x: x['source']))

  seeds_with_ranges = mappings['seeds']
  final_locations = []
  for seed_with_range in seeds_with_ranges:
    min_seed = seed_with_range[0]
    max_seed = seed_with_range[0] + seed_with_range[1] - 1
    for mapping in flattened_mappings:
      if mapping['source_end'] > min_seed and mapping['source'] < max_seed:
        seed_value = max(min_seed, mapping['source'])
        final_locations.append(mapping['destination'] + seed_value - mapping['source'])
  print(min(final_locations))

