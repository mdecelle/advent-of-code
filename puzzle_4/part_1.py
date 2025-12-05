def solution(filename):
  with open(filename) as file:
    paper_locations = [line.rstrip() for line in file]

  m = len(paper_locations)
  n = len(paper_locations[0])
  paper_count = [[1 if paper_locations[i][j] == '@' else 0 for j in range(n)] for i in range(m)]
  new_paper_count = [[0] * n for _ in range(m)]

  for i in range(m):
    current_count = paper_count[i][0]
    for j in range(n):
      if j < n-1:
        current_count += paper_count[i][j+1]
      if j > 1:
        current_count -= paper_count[i][j-2]

      new_paper_count[i][j] = current_count

  paper_count = new_paper_count
  new_paper_count = [[0] * n for _ in range(m)]

  for j in range(n):
    current_count = paper_count[0][j]
    for i in range(m):
      if i < m-1:
        current_count += paper_count[i+1][j]
      if i > 1:
        current_count -= paper_count[i-2][j]
      new_paper_count[i][j] = current_count

  paper_count = new_paper_count

  count = 0
  for i in range(m):
    for j in range(n):
      if paper_locations[i][j] == '@' and paper_count[i][j] < 5:
        count += 1

  return count