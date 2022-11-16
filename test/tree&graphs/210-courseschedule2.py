from collections import defaultdict
class Solution:

    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # Create the adjacency list representation of the graph
        adj_list = defaultdict(list)

        # A pair [a, b] in the input represents edge from b --> a
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        topological_sorted_order = []
        is_possible = True

        # By default all vertces are WHITE
        color = {k: Solution.WHITE for k in range(numCourses)}
        def dfs(node):
            nonlocal is_possible

            # Don't recurse further if we found a cycle already
            if not is_possible:
                return

            # Start the recursion
            color[node] = Solution.GRAY

            # Traverse on neighboring vertices
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                         # An edge to a GRAY vertex represents a cycle
                        is_possible = False

            # Recursion ends. We mark it as black
            color[node] = Solution.BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            # If the node is unprocessed, then call dfs on it.
            if color[vertex] == Solution.WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []


# (MY SOLUTION)
# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         requisites = {}
#         result = []

#         if len(prerequisites) == 0:
#             for i in range(numCourses):
#                 result.insert(0, i)
#             return result

#         for prereq in prerequisites:
#             array = []
#             if prereq[0] not in requisites:
#                 array.append(prereq[1])
#                 requisites[prereq[0]] = array
#             else:
#                 array = requisites[prereq[0]]
#                 array.append(prereq[1])
#                 requisites[prereq[0]] = array
        
#         for prereq in prerequisites:
#             ans = self.dfs(requisites, prereq[0], [], False)
#             result = max(result, ans, key=len)

#         print(result)
#         if result:
#             difference = numCourses - len(result)
#             print(len(result))
#             print("HI")
#             if difference > 0:
#                 for i in range(difference):
#                     result.insert(0,max(result)+1)

#         return result

#     def dfs(self, graph, source, array, nope):
#         if source in array:
#             array.remove(source)
#             array.insert(0,source)
#         else:
#             array.insert(0,source)
#         if source in graph and not nope:
#             for neighbor in graph[source]:
#                 if neighbor in graph:
#                     if graph[neighbor] == [source]:
#                         nope = True
#                 self.dfs(graph, neighbor, array, nope)

#         if nope:
#             return []

#         return array

