from collections import deque

class Machine():
  def __init__(self, light_config: int, buttons: list[int]):
    self.buttons = buttons
    self.light_config = light_config

def parse_file(filename):
  def parse_line(line):
    def parse_lights(light_string):
      num_string = ''.join(['1' if c == '#' else '0' for c in light_string[1:-1]])
      return int(num_string[::-1], 2)

    def parse_button(button_string):
      return sum([2 ** int(c) for c in button_string[1:-1].split(',')])

    line_splits = line.split(' ')
    light_config = parse_lights(line_splits[0])
    buttons = [parse_button(button_string) for button_string in line_splits[1:-1]]
    return light_config, buttons

  machines = []
  with open(filename) as file:
    for line in file.readlines():
      machines.append(Machine(*parse_line(line)))
  return machines

def get_possible_buttons(machine: Machine, light_config):
  needed_lights = machine.light_config ^ light_config
  if needed_lights == 0:
    return None
  
  v = 1
  while v & needed_lights == 0:
    v <<= 1
  return set([button for button in machine.buttons if button & v != 0])
  

def get_min_buttons(machine: Machine):
  possibilities = deque([(0,set())])
  while True:
    light_config, used_buttons = possibilities.pop()
    potential_buttons = get_possible_buttons(machine, light_config)
    potential_buttons.difference_update(used_buttons)
    for button in list(potential_buttons):
      new_buttons = used_buttons.union([button])
      new_light_config = button ^ light_config
      if new_light_config == machine.light_config:
        return len(new_buttons)
      possibilities.appendleft((new_light_config, new_buttons))
    
def solution(filename):
  machines = parse_file(filename)
  total_buttons = 0
  for machine in machines:
    total_buttons += get_min_buttons(machine)
  return total_buttons