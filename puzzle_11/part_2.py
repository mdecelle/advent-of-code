def parse_input(filename):
  server_connections = {}
  with open(filename) as file:
    for line in file.readlines():
      servers = line.strip().split(' ')
      server_connections[servers[0][:-1]] = servers[1:]
  return server_connections

def calc_paths_to_destination(start_server, destination_server, servers, paths_to_out):
  if paths_to_out[start_server] == None:
    paths_to_out[start_server] = sum([calc_paths_to_destination(server, destination_server, servers, paths_to_out) for server in servers[start_server]])
  return paths_to_out[start_server]

def clear_paths(paths_to_out):
  for p in paths_to_out:
    if paths_to_out[p] != None:
      paths_to_out[p] = 0

def traverse_route(route, servers):
  paths_to_out = {server: None for server in servers}
  path_count = 1
  for i in range(len(route)-1,0,-1):
    paths_to_out[route[i]] = path_count
    path_count = calc_paths_to_destination(route[i-1], route[i], servers, paths_to_out)
    clear_paths(paths_to_out)
  return path_count

def solution(filename):
  servers = parse_input(filename)
  return traverse_route(['svr','fft','dac','out'], servers)
  

  
  