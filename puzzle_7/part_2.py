from collections import Counter

def parse_file(file):
  lines = file.readlines()
  beam_location = lines[0].strip().find('S')
  splitter_lines = [lines[i].strip() for i in range(1, len(lines))]
  return beam_location, splitter_lines


def solution(filename):
  with open(filename) as file:
    beam, splitters = parse_file(file)
  
  max_width = len(splitters[0])
  current_beams = {beam: 1}
  for split in splitters:
    new_beams = Counter()
    for beam, count in current_beams.items():
      if split[beam] == '^':
        if beam - 1 >= 0:
          new_beams[beam-1] += count
        if beam + 1 < max_width:
          new_beams[beam + 1] += count
      else:
        new_beams[beam] += count
    current_beams = new_beams
  return sum(new_beams.values())
