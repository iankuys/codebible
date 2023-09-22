def largest_component(graph):
  largest = 0
  visited = set()
  for node in graph:
    largest = max(largest, exploreSize(graph, node, visited))
    
  return largest
  pass # todo

def exploreSize(graph, node, visited):
  if node in visited:
    return 0
  visited.add(node)
  size = 1
  
  for neighbor in graph[node]:
    size += exploreSize(graph, neighbor, visited)
    
  return size