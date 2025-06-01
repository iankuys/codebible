# LeetCode Problem 57: https://leetcode.com/problems/
import collections

def undirected_path(edges, node_A, node_B):
  graph = buildGraph(edges)
  visited_set = set()
  
  return hasPath(graph, node_A, node_B, visited_set)

def hasPath(graph, source, dest, visited):

  if source == dest:
    return True
  if source in visited:
    return False
  visited.add(source)
  for neighbor in graph[source]:
    if hasPath(graph, neighbor, dest, visited) == True:
      return True
    
  return False

def buildGraph(edges):
  graph = collections.defaultdict(list)
  
  for edge in edges:
    a = edge[0]
    b = edge[1]
    
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
    
  return graph
  

