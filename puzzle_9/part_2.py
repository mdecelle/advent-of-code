from sortedcontainers import SortedDict

def parse_file(file):
  return [tuple([int(v) for v in line.split(',')]) for line in file.readlines()]

def get_lines(coordinates):
  vertical = SortedDict()
  horizontal = SortedDict()
  x1,y1 = coordinates[-1]
  inside = -1
  prior_direction = 1
  for x2,y2 in coordinates:
    if x1 == x2:
      if x1 not in vertical:
        vertical[x1] = []
      direction = 1 if y1 < y2 else -1
      inside = inside * direction * prior_direction * -1
      if direction == 1:
        vertical[x1].append([y1,y2,inside])
      else:
        vertical[x1].append([y2,y1,inside])

    else:
      if y1 not in horizontal:
        horizontal[y1] = []
      direction = 1 if x1 < x2 else -1
      inside = inside * direction * prior_direction * - 1
      if direction == 1:
        horizontal[y1].append([x1,x2,inside])
      else:
        horizontal[y1].append([x2,x1,inside])
    prior_direction = direction
    x1 = x2
    y1 = y2
  
  return horizontal, vertical

def reverse_direction(lines):
  for idx in lines:
    for line in lines[idx]:
      line[2] *= -1

def get_rectangles(coordinates):
  c_len = len(coordinates)
  rectanges = []
  for i in range(c_len):
    for j in range(i+1,c_len):
      rectanges.append([coordinates[i], coordinates[j]])
  return rectanges

def crosses_line(segment, constant, lines):
  start, end = segment
  for line_key in lines.irange(start, end, inclusive=(False,False)):
    for bottom, top, _ in lines[line_key]:
      if bottom < constant < top:
        return True
  return False

def make_segment(a,b):
  if a < b:
    return (a,b)
  else:
    return (b,a)

def get_line(val, intercept, lines):
  for line in lines[intercept]:
    if line[0] == val or line[1] == val:
      return line
      
def line_check(start, end, intercept, lines, alt_lines):
  direction = 1 if start < end else -1
  line = get_line(start, intercept, lines)
  if direction == 1:
    if line[0] == start:
      if line[1] >= end:
        return True
      else:
        return line_check(line[1], end, intercept, lines, alt_lines)
  else:
    if line[1] == start:
      if line[0] <= end:
        return True
      else:
        return line_check(line[0], end, intercept, lines, alt_lines)
      
  alt_line = get_line(intercept, start, alt_lines)
  return alt_line[2] == direction

def test_direction(x1,y1,x2,y2, horizontal, vertical):
  return \
    line_check(x1,x2,y1, horizontal, vertical) and \
    line_check(x2,x1,y2, horizontal, vertical) and \
    line_check(y1,y2,x1, vertical, horizontal) and \
    line_check(y2,y1,x2, vertical, horizontal)
    

def is_valid(rectangle, horizontal, vertical):
  c1,c2 = rectangle
  x1,y1 = c1
  x2,y2 = c2
  h = make_segment(y1,y2)
  v = make_segment(x1,x2)
  if crosses_line(h,x1,horizontal) or crosses_line(h,x2,horizontal) or crosses_line(v,y1,vertical) or crosses_line(v,y2,vertical):
    return False
  
  return test_direction(x1,y1,x2,y2, horizontal, vertical) and test_direction(x2,y2,x1,y1, horizontal, vertical)

def area(rectange):
  c1, c2 = rectange
  x1,y1 = c1
  x2,y2 = c2
  a = abs(x1-x2) + 1
  b = abs(y1-y2) + 1
  return a * b

def solution(filename):
  with open(filename) as file:
    coordinates = parse_file(file)
  horizontal, vertical = get_lines(coordinates)
  if horizontal.peekitem(0)[1][0][2] != 1:
    reverse_direction(horizontal)
    reverse_direction(vertical)
  rectanges = get_rectangles(coordinates)
  max_area = 0


  for rectangle in rectanges:
    if is_valid(rectangle, horizontal, vertical):
      max_area = max(max_area, area(rectangle))
  return max_area

  
