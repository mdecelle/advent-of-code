def get_joltage(bank):
  def find_idx(start_idx, end_idx):
    idx = start_idx
    top_val = 0
    for i in range(start_idx, end_idx):
      if int(bank[i]) > top_val:
        top_val = int(bank[i])
        idx = i
    return (top_val, idx + 1)
  bank_len = len(bank)
  prior_start = 0
  joltage = ''
  for i in range(12):
    c, prior_start = find_idx(prior_start, bank_len + i - 11)
    joltage += str(c)
  return joltage

def solution(filename):
  f = open(filename)
  total_joltage = 0
  for bank in f.readlines():
    j = get_joltage(bank.strip())
    total_joltage += int(j)
  return total_joltage

