# There is a common trick to use we can take advantage of.
# suppose an array a of length of the main array that all of its elements are zero initially. 
# For each update [l, r] we add 1 to a[l] and negate 1 from a[r+1]. after all operations are done, prefix sum array for each index is the number of times the operation is done on that index, so we can derive the final number that reside in that index.
# https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/#
def getFinalData(data, updates):
    n = len(data)
    a = [0 for _ in range(n + 1)]
    prefix_sum = [0 for _ in range(n)]

    for l, r in updates:
        # Since the problem used 1-indexed updates
        # l, r + 1 ----> l - 1, r
        a[l - 1] += 1
        a[r] -= 1

    prefix_sum[0] = a[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + a[i]

    return [
        -num if prefix_sum[i] % 2 == 1 else num for i, num in enumerate(data)
    ]

print(getFinalData(
    [1,-4,-5,2],
    [
        [2,4],
        [1,2]
    ]
))