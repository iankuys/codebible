# Example 1:

# Input: rooms = [[1],[2],[3],[]]
# Output: true
# Explanation: 
# We visit room 0 and pick up key 1.
# We then visit room 1 and pick up key 2.
# We then visit room 2 and pick up key 3.
# We then visit room 3.
# Since we were able to visit every room, we return true.

class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear operation
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        can_visit = set()
        def dfs(key):
            if key in can_visit:
                return
            can_visit.add(key)
            for entry in rooms[key]:
                dfs(entry)
        dfs(0)
        return len(can_visit) == len(rooms)

        