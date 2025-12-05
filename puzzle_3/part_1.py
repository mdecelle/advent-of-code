def get_joltage(bank):
  bank_len = len(bank)
  top_val = 0
  second_val = 0
  for i in range(bank_len):
    val = int(bank[i])

    if i < bank_len - 1 and val > top_val:
      top_val = val
      second_val = int(bank[i+1])
    elif val > second_val:
      second_val = val
  
  return 10 * top_val + second_val

def get_joltage_str(bank, trim):
  top_val = 0
  idx = 0
  for i,b in bank[:trim]:
    if int(b) > top_val:
      idx = i
      top_val = int(b)
  
  return (top_val, idx)

def get_alternate_joltage():
  pass
  
def solution(filename):
  f = open(filename)
  total_joltage = 0
  for bank in f.readlines():
    total_joltage += get_joltage(bank.strip())

  return total_joltage

