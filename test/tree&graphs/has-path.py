#dfs
def has_path(graph, src, dst):
  if src == dst:
    return True
  
  for neighbor in graph[src]:
    if (has_path(graph,neighbor,dst) == True):
      return True
    
  return False

#bfs
def has_path(graph, src, dst):
    queue = [src]

    while queue:
        path = queue.pop(0)
        if path == dst:
            return True
        for neighbor in graph[src]:
            queue.append(neighbor)
    
    return False