def parse_line(line):
  val = int(line[1:])
  if line[0] == 'R':
    return val
  else:
    return -val

def solution(filename):
  f = open(filename)
  position = 50
  mod = 100
  password = 0
  for line in f.readlines():
    val = parse_line(line)
    position += val
    position %= mod
    if position == 0:
      password += 1

  return password

