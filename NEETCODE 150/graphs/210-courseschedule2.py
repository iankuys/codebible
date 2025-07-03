# LeetCode Problem 210: https://leetcode.com/problems/
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Course prerequisites: adjacency list where key: course, value: list of next courses
        graph = defaultdict(list)
        for dest, src in prerequisites:
            graph[src].append(dest)

        # Color states: 0 = unvisited, 1 = visiting, 2 = visited
        UNVISITED, VISITING, VISITED = 0, 1, 2
        state = [UNVISITED] * numCourses
        order = []
        self.has_cycle = False

        def dfs(course):
            if state[course] == VISITING:
                self.has_cycle = True
                return
            if state[course] == VISITED:
                return

            state[course] = VISITING
            for neighbor in graph[course]:
                dfs(neighbor)
                if self.has_cycle:
                    return
            state[course] = VISITED
            order.append(course)

        for course in range(numCourses):
            if state[course] == UNVISITED:
                dfs(course)
                if self.has_cycle:
                    return []

        return order[::-1]
