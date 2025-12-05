from puzzle_1.part_1 import parse_line

def solution(filename):
  f = open(filename)
  position = 50
  mod = 100
  password = 0
  for line in f.readlines():
    val = parse_line(line)
    old_position = position
    position += val
    position %= mod
    if position == 0:
      password += 1

    if val < 0:
      password += val // -100
      if old_position != 0 and position > old_position:
        password += 1
    else:
      password += val // 100
      if position != 0 and position < old_position:
        password += 1

  return password

