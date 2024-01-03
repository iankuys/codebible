class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def capture(i, j):
            if i < 0 or i == ROWS or j < 0 or j == COLS or board[i][j] != "O":
                return 

            board[i][j] = "T"

            capture(i + 1, j)
            capture(i - 1, j)
            capture(i, j + 1)
            capture(i, j - 1)

        # 1. (DFS) Caputure unsurrounded regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and ((r in [0, ROWS - 1]) or (c in [0, COLS - 1]))):
                    print(board[r][c])
                    capture(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                print(board[r][c])


        # 2. Capture surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O"):
                    board[r][c] = "X"

        # 3. Uncapture unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "T"):
                    board[r][c] = "O"

