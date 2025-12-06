import bisect

def collapse_ranges(ranges):
  ranges.sort()
  new_ranges = [ranges[0]]
  for r in ranges:
    if r[0] > new_ranges[-1][1]:
      new_ranges.append(r)
    else:
      update_range = new_ranges[-1]
      update_range[1] = max(update_range[1], r[1])
  return new_ranges
    
def parse_input(lines):
  def parse_range(raw_range):
    return [int(s) for s in raw_range.split('-')]
  
  def parse_id(raw_id):
    return int(raw_id)

  ranges = []
  ids = []
  is_range = True
  for line in lines:
    line = line.strip()
    if len(line) == 0:
      is_range = False
      continue
    
    if is_range:
      ranges.append(parse_range(line))
    else:
      ids.append(parse_id(line))
  
  return collapse_ranges(ranges), ids  

def solution(filename):
  with open(filename) as f:
    ranges, ids = parse_input(f.readlines())
  
  range_starts = [r[0] for r in ranges]
  range_len = len(ranges)

  fresh_count = 0
  for id in ids:
    idx = bisect.bisect(range_starts, id) - 1
    if 0 <= idx < range_len and ranges[idx][0] <= id <= ranges[idx][1]:
      fresh_count += 1

  return fresh_count


