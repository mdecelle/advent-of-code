def parse_input(file):
  all_vals = []
  for line in file.readlines():
    vals = []
    raw_split = line.strip().split(' ')
    for raw_val in raw_split:
      clean_val = raw_val.strip()
      if len(clean_val) == 0:
        continue
      vals.append(clean_val)
    all_vals.append(vals)
  
  all_vals_len = len(all_vals)
  all_nums = []
  for i in range(all_vals_len - 1):
    all_nums.append([int(v) for v in all_vals[i]])
  
  all_ops = all_vals[-1]
  return all_nums, all_ops

def process_input(vals, ops):
  vals_len = len(vals)
  ops_len = len(ops)
  grand_total = 0
  for i in range(ops_len):
    op = ops[i]
    if op == '+':
      total = 0
    else:
      total = 1
    for j in range(vals_len):
      if op == '+':
        total += vals[j][i]
      else:
        total *= vals[j][i]
    grand_total += total
  
  return grand_total

def solution(filename):
  with open(filename) as f:
    vals, ops = parse_input(f)
    return process_input(vals, ops)
  
    
