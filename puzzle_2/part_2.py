def get_min_prefix(size):
  return int(''.join(['1'] + ['0'] * (size - 1)))

def calc_sum(start_prefix, end_prefix, repeats):
  size = len(str(start_prefix))
  factor = 0
  for _ in range(repeats):
    factor *= (10 ** size)
    factor += 1
  diff = end_prefix - start_prefix
  return factor * (start_prefix * (diff + 1) + ((diff * (diff + 1)) // 2))

def get_valid_repeats(start_val, end_val, size):
  min_repeats = 1 + (len(str(start_val)) - 1) // size
  max_repeats = len(str(end_val)) // size
  if min_repeats > max_repeats:
    return []
  else:
    return list(range(min_repeats, max_repeats + 1))

def get_prefix(val, size, repeats, is_start):
  val_len = len(str(val))
  if val_len == size * repeats:
    prefix = int(str(val)[:size])
    if is_start:
      if int(str(prefix) * repeats) < val:
        prefix += 1
    else:
      if int(str(prefix) * repeats) > val:
        prefix -= 1
    if len(str(prefix)) != size:
      return None
    return prefix
  elif is_start and val_len < size * repeats:
    return int(''.join(['1'] + ['0'] * (size - 1)))
  elif not is_start and val_len > size * repeats:
    return int('9' * size)
  else:
    return None

def calc_total_sum_size(start_val, end_val, size, repeats):
  if repeats <= 1:
    return 0
  start_prefix = get_prefix(start_val, size, repeats, True)
  end_prefix = get_prefix(end_val, size, repeats, False)
  total_len = size * repeats
  if start_prefix != None and end_prefix != None and start_prefix <= end_prefix:
    total = calc_sum(start_prefix, end_prefix, repeats)
    for duplicate_size in range(size-1,0,-1):
      if size % duplicate_size == 0:
        new_start = int(str(start_prefix) * repeats)
        new_end = int(str(end_prefix) * repeats)
        total -= calc_total_sum_size(new_start, new_end, duplicate_size, total_len // duplicate_size)
    return total
  else:
    return 0

def calc_total_sum(start_val, end_val):
  max_size = len(str(end_val))
  total = 0
  for size in range(1, max_size + 1):
    for repeats in get_valid_repeats(start_val, end_val, size):
      if repeats <= 1:
        continue
      total += calc_total_sum_size(start_val, end_val, size, repeats)
  return total


def solution(filename):
  f = open(filename)
  ranges = [[int(r) for r in section.split('-')] for section in f.readline().split(',')]
  total = 0
  for start,end in ranges:
    v = calc_total_sum(start,end)
    total += v

  return total
