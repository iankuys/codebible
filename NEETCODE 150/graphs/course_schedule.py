# 207. Course Schedule
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# https://leetcode.com/problems/course-schedule/description/
class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear scan
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = defaultdict(list)

        for prereq in prerequisites:
            adj_list[prereq[0]].append(prereq[1])
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if adj_list[course] == []:
                return True
            visited.add(course)
            for neighbor in adj_list[course]:
                if not dfs(neighbor): return False
            visited.remove(course)
            adj_list[course] = []
            return True
        
        for prereq in prerequisites:        
            if not dfs(prereq[1]):
                return False

        return True
