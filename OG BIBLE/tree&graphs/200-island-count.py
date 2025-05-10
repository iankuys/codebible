def island_count(grid):
  visited = set()
  count = 0
  
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if(exploreIsland(grid, i, j, visited)):
        count += 1
        
  return count
      
  pass # todo

def exploreIsland(grid, r, c, visited):
  if (r < 0 or r >= len(grid)) or (c < 0 or c>=len(grid[0])):
    return False
  
  if grid[r][c] == "W": return False
  if (r,c) in visited: return False
  visited.add((r,c))
  
  exploreIsland(grid, r+1, c, visited)
  exploreIsland(grid, r, c+1, visited)
  exploreIsland(grid, r-1, c, visited)
  exploreIsland(grid, r, c-1, visited)
               
  return True
  
  
    