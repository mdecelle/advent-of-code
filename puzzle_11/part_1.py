def parse_input(filename):
  server_connections = {}
  with open(filename) as file:
    for line in file.readlines():
      servers = line.strip().split(' ')
      server_connections[servers[0][:-1]] = servers[1:]
  return server_connections

def calc_paths_to_out(server_name, servers, paths_to_out):
  if server_name == 'out':
    return 1
  if paths_to_out[server_name] == None:
    paths_to_out[server_name] = sum([calc_paths_to_out(server, servers, paths_to_out) for server in servers[server_name]])
  return paths_to_out[server_name]

def solution(filename):
  start_server = 'you'
  servers = parse_input(filename)
  paths_to_out = {server: None for server in servers}
  return calc_paths_to_out(start_server, servers, paths_to_out)
  

  
  