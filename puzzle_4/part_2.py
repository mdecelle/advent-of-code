def solution(filename):
  with open(filename) as file:
    paper_locations = [line.rstrip() for line in file]

  m = len(paper_locations)
  n = len(paper_locations[0])
  paper_count = [[1 if paper_locations[i][j] == '@' else 0 for j in range(n)] for i in range(m)]
  new_paper_count = [[0] * n for _ in range(m)]

  paper_coords = set()
  for c1 in range(m):
    for c2 in range(n):
      if paper_locations[c1][c2] == '@':
        paper_coords.add((c1,c2))

  for c1 in range(m):
    current_count = paper_count[c1][0]
    for c2 in range(n):
      if c2 < n-1:
        current_count += paper_count[c1][c2+1]
      if c2 > 1:
        current_count -= paper_count[c1][c2-2]

      new_paper_count[c1][c2] = current_count

  paper_count = new_paper_count
  new_paper_count = [[0] * n for _ in range(m)]

  for c2 in range(n):
    current_count = paper_count[0][c2]
    for c1 in range(m):
      if c1 < m-1:
        current_count += paper_count[c1+1][c2]
      if c1 > 1:
        current_count -= paper_count[c1-2][c2]
      new_paper_count[c1][c2] = current_count

  paper_count = new_paper_count

  count = 0
  remove_stack = list(paper_coords)
  while len(remove_stack) > 0:
    coord = remove_stack.pop()
    c1,c2 = coord
    if coord in paper_coords and paper_count[c1][c2] < 5:
      paper_coords.remove(coord)
      count += 1
      for i in range(c1-1,c1+2):
        for j in range(c2-1,c2+2):
          if 0 <= i < m and 0 <= j < n:
            paper_count[i][j] -= 1
            if paper_count[i][j] < 5:
              remove_stack.append((i,j))
          

  return count