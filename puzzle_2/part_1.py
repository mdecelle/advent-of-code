def get_endpoint(val_str):
  val_len = len(val_str)
  val_mid = (val_len // 2)
  if val_len % 2 == 1:
    val = ''.join(['1'] + ['0'] * (val_len // 2))
  else:
    val = val_str[:val_mid]
  return int(val)

def compare(val, str_compare):
  doubled = int(str(val) + str(val))
  value = int(str_compare)
  if doubled > value:
    return 1
  elif doubled < value:
    return -1
  else:
    return 0

def add_duplicates(start, end):
  def add_range(s, e):
    diff = e - s
    return s * (diff + 1) + ((diff * (diff + 1)) // 2)
  def dup_val(v, l):
    return v * (10 ** l) + v
  start_s, end_s = str(start), str(end)
  total = 0
  while len(start_s) < len(end_s):
    temp_end = int(''.join(['9'] * len(start_s)))
    total += dup_val(add_range(start, temp_end), len(start_s))
    start = temp_end + 1
    start_s = str(temp_end + 1)
  total += dup_val(add_range(start, end), len(start_s))
  return total

def solution(filename):
  f = open(filename)
  ranges = [section.split('-') for section in f.readline().split(',')]
  total = 0
  for start,end in ranges:
    s = get_endpoint(start)
    e = get_endpoint(end)
    if compare(s, start) < 0:
      s += 1
    if compare(e, end) > 0:
      e -= 1
    if s <= e:
      total += add_duplicates(s,e)
  return total
  
