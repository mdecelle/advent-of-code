from math import gcd

class Machine:
  def __init__(self, buttons: list[list[int]], joltage: list[int]):
    self.buttons = buttons
    self.joltage = joltage
    self.button_count = len(buttons)
    self.joltage_count = len(joltage)
    self.calc_button_press()
  
  def calc_button_press(self):
    self.max_button_presses = [0] * self.button_count
    for i,button in enumerate(self.buttons):
      self.max_button_presses[i] = min([jolt for idx, jolt in enumerate(self.joltage) if idx in button])

class Matrix:
  def __init__(self, grid, values):
    self.matrix = []
    self.m = len(grid)
    self.n = len(grid[0])
    for row in grid:
      self.matrix.append(list(row))
    self.values = list(values)
    self.reduce()
    self.compute_variable_columns()
    self.variable_columns_len = len(self.variable_columns)
    self.compute_significant_mapping()
    self.sign_col_len = len(self.significant_mapping)
  
  def print(self):
    for row in self.matrix:
      print(row)
    print("Values: ", self.values)
  
  def compute_vals(self, variable_column_vals):
    vals = [0] * self.n
    for col in self.variable_columns:
      vals[col] = variable_column_vals[col]
    
    for row_idx in range(self.sign_col_len):
      sig_position = self.significant_mapping[row_idx]
      remainder = self.values[row_idx]
      for col in self.variable_columns:
        remainder -= self.matrix[row_idx][col] * variable_column_vals[col]
      sig_val = self.matrix[row_idx][sig_position]
      if remainder < 0 or remainder % sig_val != 0:
        return None
      else:
        vals[sig_position] = remainder // sig_val
    return vals

  def compute_significant_mapping(self):
    self.significant_mapping = []
    for i in range(self.m):
      if all(v == 0 for v in self.matrix[i]) and self.values[i] != 0:
        raise Exception("row of zeros does not equal zero")
      for j in range(self.n):
        if self.matrix[i][j] != 0:
          self.significant_mapping.append(j)
          break

  def compute_variable_columns(self):
    self.variable_columns = []
    for j in range(self.n):
      sig_count = 0
      for i in range(self.m):
        if self.matrix[i][j] != 0:
          sig_count += 1
          if sig_count > 1:
            self.variable_columns.append(j)
            break
    self.variable_columns

  def reduce(self):
    significant_row_idx = 0
    col = 0
    while col < self.n and significant_row_idx < self.m:
      select_row_idx = self.find_significant_row(col)
      if select_row_idx != None:
        for row_idx in self.find_non_zero_rows(col):
          if row_idx == select_row_idx:
            continue
          self.zero_row(select_row_idx, row_idx, col)
        self.swap_rows(significant_row_idx,select_row_idx)
        significant_row_idx += 1
      # self.print()
      col += 1


  def find_significant_row(self, column):
    for i in range(self.m):
      if self.matrix[i][column] != 0 and all(v == 0 for v in self.matrix[i][:column]):
        return i
    return None
  
  def find_non_zero_rows(self, column):
    rows = []
    for i in range(self.m):
      if self.matrix[i][column] != 0:
        rows.append(i)
    
    return rows
  
  def zero_row(self, keep_row_idx, zero_row_idx, col_idx):
    k_val = self.matrix[keep_row_idx][col_idx]
    z_val = self.matrix[zero_row_idx][col_idx]

    g = gcd(k_val, z_val)
    self.scale_row(keep_row_idx, z_val // g)
    self.scale_row(zero_row_idx, k_val // g)
    self.add_rows(zero_row_idx, keep_row_idx, -1)
    self.reduce_row(keep_row_idx)
    
  def scale_row(self, row_idx, scale):
    if scale == 1:
      return
    row = self.matrix[row_idx]
    for i in range(self.n):
      row[i] *= scale
    
    self.values[row_idx] *= scale
  
  def swap_rows(self,i,j):
    t = self.matrix[i]
    self.matrix[i] = self.matrix[j]
    self.matrix[j] = t

    v = self.values[i]
    self.values[i] = self.values[j]
    self.values[j] = v
  
  def add_rows(self, replace_row_idx, add_row_idx, scale):
    non_zero = False
    replace_row = self.matrix[replace_row_idx]
    add_row = self.matrix[add_row_idx]
    for i in range(self.n):
      replace_row[i] += add_row[i] * scale
      if non_zero and replace_row[i] != 0:
        non_zero = True
    
    self.values[replace_row_idx] += self.values[add_row_idx] * scale
    
    self.reduce_row(replace_row_idx)
  
  def reduce_row(self, row_idx):
    row = self.matrix[row_idx]
    factor = gcd(*row,self.values[row_idx])
    if factor == 0:
      return
    first_val = False
    for i in range(self.n):
      if row[i] != 0:
        if not first_val:
          if row[i] < 0:
            factor *= -1
          first_val = True
        row[i] //= factor
    self.values[row_idx] //= factor

def parse_file(filename) -> list[Machine]:
  def parse_line(line):
    def parse_button(button_string):
      return [int(c) for c in button_string[1:-1].split(',')]

    def parse_joltage(joltage_string):
      return [int(c) for c in joltage_string[1:-1].split(',')]

    line_parts = line.split(' ')
    buttons = [parse_button(button) for button in line_parts[1:-1]]
    joltage = parse_joltage(line_parts[-1])
    return buttons, joltage

  machines = []
  with open(filename) as file:
    for line in file.readlines():
      buttons, joltage = parse_line(line.strip())
      machines.append(Machine(buttons, joltage))
    
  return machines

def build_button_matrix(machine: Machine):
  matrix = [[0] * machine.button_count for _ in range(machine.joltage_count)]
  for i,button in enumerate(machine.buttons):
    for idx in button:
      matrix[idx][i] = 1
  return Matrix(matrix, machine.joltage)

# This is sort of lazy checking all possible variable presses, this could be optimized to check better.
def calc_min_button_presses(matrix: Matrix, machine: Machine):
  def increment(current_vals, max_vals):
    idx = 0
    for idx in current_vals:
      if current_vals[idx] < max_vals[idx]:
        current_vals[idx] += 1
        return
      else:
        current_vals[idx] = 0
  
  max_vals = {i:machine.max_button_presses[i] for i in matrix.variable_columns}
  current_vals = {i:0 for i in max_vals}
  min_button_presses = float('inf')
  while True:
    vals = matrix.compute_vals(current_vals)
    if vals != None:
      min_button_presses = min(min_button_presses, sum(vals))
    increment(current_vals, max_vals)
    if all(current_vals[v] == 0 for v in current_vals):
      return min_button_presses


def solution(filename):
  machines = parse_file(filename)
  total_buttons = 0
  for i,machine in enumerate(machines):
    matrix = build_button_matrix(machine)
    button_presses = calc_min_button_presses(matrix, machine)
    total_buttons += button_presses
  return total_buttons
  

   