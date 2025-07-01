"""
Question 1: A server network is represented as a tree of g_nodes servers indexed from 1 to g_nodes and g_nodes - 1 edges where the ith edges connect the servers g_from[i] and g_to[i]. The transfer time between any two connected servers is 1 unit.
Given the graph g, find the maximum time taken to transfer the data between any two servers in the system.

Example
Suppose g_nodes = 3, g_from = [1, 2], g_to = [2, 3]
The maximum time required to transfer data from 1 to 3 that takes 2 units of time. Hence, the answer is 2.

Sample Case 0:
Sample Input:
5 4
1 5
1 3
1 2
5 4
g_nodes = 5, g_nodes - 1 = 4
g_from[] = [1, 1, 1, 5], g_to[] = [5, 3, 2, 4]
Sample Output: 3

Sample Case 1:
Sample Input:
7
6
4 2
4 7
2 5
1 6
2 3
g_nodes = 7, g_nodes = 1 - 6
g_from[] = [4, 4, 2, 1, 2], g_to[] = [2, 7, 5, 6, 3]
Sample Output: 4
"""

from collections import defaultdict, deque

def max_transfer_time(g_nodes, g_from, g_to):
    # Step 1: Build the graph
    graph = defaultdict(list)
    for u, v in zip(g_from, g_to):
        graph[u].append(v)
        graph[v].append(u)

    def bfs(start):
        visited = set()
        queue = deque([(start, 0)])
        visited.add(start)
        farthest_node = start
        max_dist = 0
        
        while queue:
            node, dist = queue.popleft()
            if dist > max_dist:
                farthest_node = node
                max_dist = dist
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
                    
        return farthest_node, max_dist
    
    start_node = g_from[0]
    far_node, _ = bfs(start_node)
    _, diameter = bfs(far_node)
    
    return diameter