def getMinimumCost(arr):
    # Write your code here
    # find neighbor has max difference
    cost = 0
    max_cost = 0
    f_index, s_index = 0, 0
    # find max diff between neighbors
    for i in range(len(arr)-1):
        first = arr[i]
        second = arr[i+1]
        if abs(second-first) > max_cost:
            max_cost = abs(second-first)
            f_index = i
            s_index = i + 1
    # new number between the max diff
    mid = (arr[f_index] + arr[s_index]) // 2
    # add the cost
    cost += (arr[f_index] - mid) * (arr[f_index] - mid)
    cost += (arr[s_index] - mid) * (arr[s_index] - mid)
    # add the cost
    for i in range(len(arr)-1):
        if i == f_index:
            continue
        first = arr[i]
        second = arr[i+1]
        cost += (first - second) * (first - second)
    return cost