
def parse_file(file):
  return [tuple([int(v) for v in line.split(',')]) for line in file.readlines()]

def get_edges(coordinates):
  tl,tr,bl,br = [],[],[],[]

  min_top = float('-inf')
  max_bottom = float('inf')
  sorted_coordinates = sorted(coordinates)
  for c in sorted_coordinates:
    _,y = c
    if y >= min_top:
      tl.append(c)
      min_top = y
    if y <= max_bottom:
      bl.append(c)
      max_bottom = y
  
  min_top = float('-inf')
  max_bottom = float('inf')
  for c in sorted_coordinates[::-1]:
    _,y = c
    if y >= min_top:
      tr.append(c)
      min_top = y
    if y <= max_bottom:
      br.append(c)
      max_bottom = y
  
  return tl,tr,bl,br

def get_rectange(tl,tr,bl,br):
  tl.sort()
  br.sort(reverse=True)
  max_area = 0
  for x1,y1 in tl:
    for x2,y2 in br:
      if x2 < x1:
        break
      if y1 < y2:
        continue
      area = (x2 - x1 + 1) * (y1 - y2 + 1)
      max_area = max(max_area, area)
  
  bl.sort()
  tr.sort(reverse=True)
  max_area = 0
  for x1,y1 in bl:
    for x2,y2 in tr:
      if x2 < x1:
        break
      if y2 < y1:
        continue
      area = (x2 - x1 + 1) * (y2 - y1 + 1)
      max_area = max(max_area, area)
  
  return max_area

def solution(filename):
  with open(filename) as file:
    coordinates = parse_file(file)
  tl,tr,bl,br = get_edges(coordinates)
  area = get_rectange(tl,tr,bl,br)
  return area
  