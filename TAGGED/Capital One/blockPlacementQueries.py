"""
3161. Block Placement Queries
Attempted
Hard
Topics
Companies
Hint
There exists an infinite number line, with its origin at 0 and extending towards the positive x-axis.

You are given a 2D array queries, which contains two types of queries:

For a query of type 1, queries[i] = [1, x]. Build an obstacle at distance x from the origin. It is guaranteed that there is no obstacle at distance x when the query is asked.
For a query of type 2, queries[i] = [2, x, sz]. Check if it is possible to place a block of size sz anywhere in the range [0, x] on the line, such that the block entirely lies in the range [0, x]. A block cannot be placed if it intersects with any obstacle, but it may touch it. Note that you do not actually place the block. Queries are separate.
Return a boolean array results, where results[i] is true if you can place the block specified in the ith query of type 2, and false otherwise.

"""

# not efficient enough as the queries gets bigger and bigger, hence the gap is bigger we need to use segment tree
from sortedcontainers import SortedList

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        obstacles = SortedList()
        res = []

        for query in queries:
            if query[0] == 1:
                x = query[1]
                obstacles.add(x)
            else:
                x, sz = query[1], query[2]
                prev = 0
                possible = False

                for obs in obstacles.irange(0, x):
                    if obs - prev >= sz:
                        possible = True
                        break
                    prev = obs  # because touching is allowed
                    
                # Check the space from the last obstacle to x
                if not possible and x - prev>= sz:
                    possible = True

                res.append(possible)

        return res

# seg tree solution (complex)
from sortedcontainers import SortedList
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:

        # Blocks along the axis
        axis = SortedList()

        # Range Max of intervals from 0 to each block
        itvl = SegTree(max(q[1] for q in queries))

        res = []
        axis.add(0)
        itvl.update(0,0)

        for q in queries:
            if q[0] == 1:
                ind = axis.bisect(q[1])
                if ind < len(axis):
                    # Update the interval of the next block
                    nxt = axis[ind]
                    itvl.update(nxt, nxt-q[1])
                # Set the interval of the current block
                itvl.update(q[1], q[1] - axis[ind-1])
                # Add the current block on axis
                axis.add(q[1])
            else:
                # Find the previous block
                prv = axis[axis.bisect(q[1])-1]
                # Range query the max interval before prv
                mx = max(q[1]-prv, itvl.query(prv))

                res.append(q[2] <= mx)
        return res

class SegTree:

    def __init__(self, n: int):
        self.n = 1 << n.bit_length()
        self.tree = [0] * (self.n*2)

    def update(self, ind: int, val: int):
        ind += self.n
        self.tree[ind] = val
        while ind > 1:
            ind //= 2
            self.tree[ind] = max(self.tree[ind*2], self.tree[ind*2+1])
    
    def query(self, ind: int) -> int:
        ind += self.n
        res = self.tree[ind]
        while ind > 1:
            if ind%2 == 1:
                res = max(res, self.tree[ind-1])
            ind //= 2
        return res