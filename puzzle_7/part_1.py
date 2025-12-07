def parse_file(file):
  lines = file.readlines()
  beam_location = lines[0].strip().find('S')
  splitter_lines = [lines[i].strip() for i in range(1, len(lines))]
  return beam_location, splitter_lines


def solution(filename):
  with open(filename) as file:
    beam, splitters = parse_file(file)
  
  max_width = len(splitters[0])
  split_count = 0
  current_beams = [beam]
  for split in splitters:
    new_beams = set()
    for beam in current_beams:
      if split[beam] == '^':
        split_count += 1
        if beam - 1 >= 0:
          new_beams.add(beam - 1)
        if beam + 1 < max_width:
          new_beams.add(beam + 1)
      else:
        new_beams.add(beam)
    current_beams = list(new_beams)
  return split_count
