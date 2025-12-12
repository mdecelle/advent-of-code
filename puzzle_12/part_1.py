class Board:
  piece_sizes = [6,5,7,7,7,7]
  def __init__(self, dimentions, piece_counts):
    self.x, self.y = dimentions
    self.piece_counts = piece_counts
    self.total_pieces = sum(self.piece_counts)
  
  def can_trivial_tile(self):
    if self.x // 3 * self.y // 3 >= len(self.piece_counts):
      return True
    else:
      return False
  
  def has_too_many_tiles(self):
    total_tiles = 0
    for i in range(6):
      total_tiles += self.piece_sizes[i] * self.piece_counts[i]
    if self.x * self.y < total_tiles:
      return True
    else:
      return False

def parse_input(filename) -> list[Board]:
  def parse_board(line):
    dim_str, piece_count_str = line.split(':')
    dimensions = [int(x) for x in dim_str.split('x')]
    piece_counts = [int(x) for x in piece_count_str.strip().split(' ')]
    return Board(dimensions, piece_counts)

  with open(filename) as file:
    boards = []
    for line in file.readlines():
      if 'x' in line:
        boards.append(parse_board(line.strip()))
  return boards

def solution(filename):
  total_count = 0
  boards = parse_input(filename)
  for board in boards:
    if board.has_too_many_tiles():
      continue
    elif board.can_trivial_tile():
      total_count += 1
    else:
      print('need to solve')
  return total_count