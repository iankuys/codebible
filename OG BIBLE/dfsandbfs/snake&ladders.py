class Solution(object):
    # Time Complexity:
    #   Best case: O(n²) - nested iteration
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        #~ is used for complementary index e.g. ~1 = -2. equation (~i) = -( i + 1), index from right


        n = len(board)
        need = {1: 0}
        bfs = [1]
        for x in bfs:
            for i in range(x + 1, x + 7):
                a, b = (i - 1) / n, (i - 1) % n
                nxt = board[~a][b if a % 2 == 0 else ~b]
                if nxt > 0: 
                    i = nxt
                if i == n * n: 
                    return need[x] + 1
                if i not in need:
                    need[i] = need[x] + 1
                    bfs.append(i)
        return -1
            
class Solution:
    # Time Complexity:
    #   Best case: O(n²) - nested iteration
    #   Average case: O(n²)
    #   Worst case: O(n²)
    # Space Complexity: O(1)
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        # BFS Solution - Since its BFS it will find the path with least steps.
        
        n = len(board)
        
        # Computes the indices in the array of the square
        def computeIndex(square):
            
            # Computes quotient (r) and remainder (c) of square-1 / n
            r, c = divmod(square-1, n)
            
            # The order (left-right, or left-right) that the numbers increase
            # changes depending on the row
            if r % 2 == 0:
                # Calculating the indices ([n][0] is square 1)
                return n-1-r, c
            else:
                return n-1-r, n-1-c
        
        visited = set()
        queue = deque([])
        queue.append((1,0))
        while queue:
            curr_square, step_num = queue.popleft()
            r, c = computeIndex(curr_square)
            
            # There is a snake or ladder
            if board[r][c] != -1:
                curr_square = board[r][c]
                
            # Reached the last square, return the step number
            if curr_square == n*n:
                return step_num
            
            # All possible future steps (next 6 squares) that are less than n*n, the last square
            for new_square in range(curr_square + 1, min(curr_square + 6, n*n)+1):

                # Ensures no cycles
                if new_square not in visited:
                    
                    # Add to set
                    visited.add(new_square)
                    
                    # Add to queue, increment step number
                    queue.append((new_square, step_num+1))
        
        return -1