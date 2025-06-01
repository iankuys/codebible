# Link: https://leetcode.com/problems/a-gate/
# Description
# Walls and Gates
# You are given a m x n 2D grid initialized with these three possible values.
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should remain filled with INF
# Input:
# [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# Output:
# [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

# Explanation:
# the 2D grid is:
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# the answer is:
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4
# VERY SIMILAR TO ROTTEN ORANGES
# https://www.lintcode.com/problem/663/

from typing import (
    List,
)
from collections import deque 

class Solution:
    """
    @param rooms: m x n 2D rooms
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        m = len(rooms)
        n = len(rooms[0])
        empty_rooms = 0

        q = deque()
        visit = set()

        # we are using a function instead of a loop here
        def addRoom(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or (row, col) in visit or rooms[row][col] == -1:
                return
            visit.add((row, col))
            q.append([row, col])

        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)

            dist += 1
            
        
        