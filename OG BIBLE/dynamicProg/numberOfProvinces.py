# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2

class Solution:
    # Time Complexity:
    #   Best case: O(V + E) - graph traversal
    #   Average case: O(V + E)
    #   Worst case: O(V + E)
    # Space Complexity: O(1)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        
        def dfs(node):
            for index, adj in enumerate(isConnected[node]):
                if adj and index not in visited:
                    visited.add(index)
                    dfs(index)
        
        ans = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                ans += 1
        
        return ans
