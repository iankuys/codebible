# 1. traveler need to reach the bottom right of grid
# 2. traveler can only move right or down

grid_dict = {}

def gridTraveler(m,n):
    key = str(m) + ',' + str(n)
    # are the arguments in the memo
    if (key in grid_dict):
        return grid_dict[key]
    if (m == 1 and n ==1): return 1
    if (m == 0 or n == 0): return 0
    # gridTraveler(m-1, n) means going down and gridTraveler(m, n-1) means going right
    grid_dict[key] = gridTraveler(m-1, n) + gridTraveler(m, n-1) 
    return grid_dict[key]

print(gridTraveler(2,3))
print(grid_dict)
print(gridTraveler(3,2))
print(grid_dict)
print(gridTraveler(18,18))
