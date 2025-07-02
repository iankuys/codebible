"""
142. Linked List Cycle II
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# hash set solution
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dup = {}
        while head:
            if head in dup:
                return head
            dup[head] = 1
            head = head.next
        
        return None
    
# Floyd's Tortoise
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize tortoise and hare pointers
        tortoise = head
        hare = head

        # Move tortoise one step and hare two steps
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

            # Check if the hare meets the tortoise
            if tortoise == hare:
                break

        # Check if there is no cycle
        if not hare or not hare.next:
            return None

        # Reset either tortoise or hare pointer to the head
        hare = head

        """
        You may ask, "Why is this the entrance to the cycle?" Well, let's consider the distances each has traveled.

        The first time that the hare and the tortoise meet within the cycle, we have established that:

        The tortoise has travelled a+b distance.
        The hare has traveled a+b+k⋅c distance, where k represents how many times the hare has lapped the cycle.
        Because the hare moves at twice the speed, a+b+k⋅c=2(a+b), rearrange for k⋅c=a+b.
        If we move the hare back to the start of the straight path and make it move at the same speed as the tortoise, here's what happens:

        The hare has a distance to travel to reach the entrance of the cycle. We can rearrange the above equation to say that the hare will reach the entrance of the cycle in a=k⋅c−b steps.
        Currently, the tortoise is b away from the entrance of the cycle. In k⋅c−b steps, where will the tortoise be? Relative to the entrance of the cycle, the tortoise will be at (k⋅c−b)+b=k⋅c. Because k is an integer, c is defined as the length of the cycle, and this distance is relative to the entrance of the cycle, the tortoise will be at the entrance!
        """
        # Move both pointers one step until they meet again
        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next