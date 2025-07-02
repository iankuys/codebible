# 684. Redundant Connection
# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# https://leetcode.com/problems/redundant-connection/description/
 
class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear operation
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]

            while p != par[p]:
                # shortening the length as we go up the chain of parents
                par[p] = par[par[p]]
                p = par[p]
            return p

        # return False if cant complete
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            # p1 is gonna be the parent of p2
            if rank[p1] > rank[p2]:
                par[p2] = p1
                # update rank since it has more children
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
            
class DSU:
    def __init__(self, N):
        # Initialize DSU class, size of each component will be one and each node
        # will be representative of its own.
        self.N = N
        self.size = [1] * N
        self.representative = list(range(N))

    def _find(self, node):
        # Returns the ultimate representative of the node.
        if self.representative[node] == node:
            return node
        self.representative[node] = self._find(self.representative[node])
        return self.representative[node]

    def _do_union(self, nodeOne, nodeTwo):
        # Returns true if node nodeOne and nodeTwo belong to different component and update the
        # representatives accordingly, otherwise returns false.
        nodeOne = self._find(nodeOne)
        nodeTwo = self._find(nodeTwo)

        if nodeOne == nodeTwo:
            return False
        else:
            if self.size[nodeOne] > self.size[nodeTwo]:
                self.representative[nodeTwo] = nodeOne
                self.size[nodeOne] += self.size[nodeTwo]
            else:
                self.representative[nodeOne] = nodeTwo
                self.size[nodeTwo] += self.size[nodeOne]
            return True


class Solution:
    def findRedundantConnection(self, edges):
        N = len(edges)

        dsu = DSU(N)
        for edge in edges:
            # If union returns false, we know the nodes are already connected
            # and hence we can return this edge.
            if not dsu._do_union(edge[0] - 1, edge[1] - 1):
                return edge

        return []     
    
# DFS
from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # returns True if cycle is found, false if not
        def dfs(src, target, visited):
            if src == target:
                return True # Found a path from src to target => cycle will be formed
            visited.add(src)
            for neighbor in graph[src]:
                if neighbor not in visited:
                    if dfs(neighbor, v, visited):
                        return True
            return False # No path found from src to target
        
        graph = defaultdict(list)

        for u, v in edges:
            visited = set()
            # If both nodes already exist in the graph, check if a path exists
            # between them. If yes, adding this edge would form a cycle.
            if u in graph and v in graph:
                if dfs(u, v, visited):
                    return [u, v]
            # Otherwise, safely add the edge to the graph (no cycle yet)
            graph[u].append(v)
            graph[v].append(u)

        return []

        