def process_input(file):
  return [[int(coord) for coord in line.strip().split(',')] for line in file.readlines()]

def distance(box1, box2):
  total = 0
  for i in range(3):
    total += (box1[i] - box2[i]) ** 2
  return total

def calc_distances(boxes):
  boxes_len = len(boxes)
  distances = []
  for i in range(boxes_len):
    for j in range(i+1, boxes_len):
      d = distance(boxes[i], boxes[j])
      distances.append((d,i,j))
  distances.sort(key=lambda x:x[0])
  return distances

def connect_boxes(connections, boxes_len):
  def find_head(v):
    while v != head_box[v]:
      v = head_box[v]
    return v
  head_box = [i for i in range(boxes_len)]
  connection_idx = 0
  box_idx = 0
  while box_idx < boxes_len:
    if head_box[box_idx] != 0:
      _,b1,b2 = connections[connection_idx]
      h1 = find_head(b1)
      h2 = find_head(b2)
      if h1 != h2:
        head_val = min(h1,h2)
        head_box[h1] = head_val
        head_box[h2] = head_val
      connection_idx += 1
    else:
      box_idx += 1
      if box_idx < boxes_len:
        head_box[box_idx] = find_head(box_idx)
  
  return connection_idx - 1

def solution(filename):
  with open(filename) as file:
    boxes = process_input(file)
  connections = calc_distances(boxes)
  last_connection = connect_boxes(connections, len(boxes))
  _,b1,b2 = connections[last_connection]
  return boxes[b1][0] * boxes[b2][0]

      

