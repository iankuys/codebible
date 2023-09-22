import collections

def shortest_path(edges, node_A, node_B):
  graph = generate_graph(edges)
  visited = set()
  queue = [[node_A, 0]]

  while queue:
    cur = queue.pop(0)
    
    if cur[0] == node_B:
      return cur[1]
    
    for neighbor in graph[cur[0]]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append([neighbor, cur[1]+1])
  
  return -1
    
  pass # todo

def generate_graph(edges):
  graph = collections.defaultdict(list)

  for node in edges:
    a = node[0]
    b = node[1]
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
    
  return graph

      