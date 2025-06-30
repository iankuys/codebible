"""
1091. Shortest Path in Binary Matrix
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.
"""

# without input replacements, using hashmap to track visited nodes
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(r, c):
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if not (0 <= nr <= m - 1 and 0 <= nc <= n - 1):
                    continue
                if grid[nr][nc] != 0:
                    continue
                yield (nr, nc) 
                # return exits a function completely after giving back a single value, 
                # while yield pauses the function, returning one value at a time and allowing the function to resume where it left off
            
        # Check that the first and last cells are open. 
        if grid[0][0] != 0 or grid[m - 1][n - 1] != 0:
            return -1

        queue = deque([(0, 0, 1)])
        visited = {(0, 0)}

        while queue:
            r, c, distance = queue.popleft()
            if (r, c) == (m - 1, n - 1):
                return distance
            for neighbour in get_neighbours(r, c):
                if neighbour in visited:
                    continue
                visited.add(neighbour)
                # Note that the * splits neighbour into its values.
                queue.append((*neighbour, distance + 1))
            
        return -1

# with input replacements
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(r, c):
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if not (0 <= nr <= m - 1 and 0 <= nc <= n - 1):
                    continue
                if grid[nr][nc] != 0:
                    continue
                yield (nr, nc) 
                # return exits a function completely after giving back a single value, 
                # while yield pauses the function, returning one value at a time and allowing the function to resume where it left off
            
        if grid[0][0] != 0 or grid[m - 1][n - 1] != 0:
            return -1

        queue = deque()
        queue.append((0, 0))
        grid[0][0] = 1

        while queue:
            r, c = queue.popleft()
            distance = grid[r][c]
            if (r, c) == (m - 1, n - 1):
                return distance
            for neighbour_row, neighbour_col in get_neighbours(r, c):
                grid[neighbour_row][neighbour_col] = distance + 1
                queue.append((neighbour_row, neighbour_col))
            
        return -1
