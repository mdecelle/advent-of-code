from puzzle_5.part_1 import parse_input

def solution(filename):
  with open(filename) as f:
    ranges, ids = parse_input(f.readlines())
  
  fresh_id_count = 0
  for r in ranges:
    fresh_id_count += r[1] - r[0] + 1
  
  return fresh_id_count

  