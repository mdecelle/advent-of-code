def parse_input(file):
  clean_lines = [line for line in file.readlines()]
  return clean_lines[:-1], clean_lines[-1]
  

def process_input(vals, ops):
  ops_len = len(ops)
  grand_total = 0
  total = 0
  for i in range(ops_len):
    op = ops[i]
    if op == '+':
      current_op = op
      grand_total += total
      total = 0
    elif op == '*':
      current_op = op
      grand_total += total
      total = 1
    
    val_str = ''.join([v[i] for v in vals]).strip()
    if len(val_str) == 0:
      continue
    else:
      val = int(val_str)
      if current_op == '+':
        total += val
      else:
        total *= val
  grand_total += total
  return grand_total

def solution(filename):
  with open(filename) as f:
    vals, ops = parse_input(f)
    return process_input(vals, ops)
  
    
