from sortedcontainers import SortedList
from collections import Counter

def process_input(file):
  return [[int(coord) for coord in line.strip().split(',')] for line in file.readlines()]

def distance(box1, box2):
  total = 0
  for i in range(3):
    total += (box1[i] - box2[i]) ** 2
  return total

def calc_distances(boxes, max_connections):
    
  boxes_len = len(boxes)
  distances = SortedList()
  for i in range(boxes_len):
    for j in range(i+1, boxes_len):
      d = distance(boxes[i], boxes[j])
      if len(distances) < max_connections:
        distances.add((d,i,j))
      elif distances[-1][0] > d:
        distances.add((d,i,j))
        distances.pop()
  return distances

def connect_boxes(connections, boxes_len):
  def find_head(v):
    while v != head_box[v]:
      v = head_box[v]
    return v
  head_box = [i for i in range(boxes_len)]
  for _,b1,b2 in connections:
    h1 = find_head(b1)
    h2 = find_head(b2)
    head_val = min(h1,h2)
    head_box[h1] = head_val
    head_box[h2] = head_val
  
  circuits = Counter()
  for box in head_box:
    b = box
    while head_box[b] != b:
      b = head_box[b]
    circuits[b] += 1
  return circuits

def solution(filename):
  if 'sample' in filename:
    max_connections = 10
  else:
    max_connections = 1000
  with open(filename) as file:
    boxes = process_input(file)
  distances = calc_distances(boxes, max_connections)
  circuits = connect_boxes(distances, len(boxes))
  top_circuits = SortedList()
  for c in circuits:
    top_circuits.add(circuits[c])
    if len(top_circuits) > 3:
      top_circuits.pop(0)
  return top_circuits[0] * top_circuits[1] * top_circuits[2]
      

