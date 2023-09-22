# Sudoku checker

def solution(grid):
    dict = {}
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] not in dict):
                dict[grid[i][j]] = 1
            else:
                return False
                
        dict = {}
    
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if (grid[j][i] not in dict):
                dict[grid[j][i]] = 1
            else:
                return False
                
        dict = {}
        
    for i in range(len(grid)//3):
        for j in range(len(grid[0])//3):
            for k in range(i*3, i*3+3):
                for l in range(j*3, j*3+3):
                    if (grid[k][l] not in dict):
                        dict[grid[k][l]] = 1
                    else:
                        return False
            dict = {}
                
        
    return True

