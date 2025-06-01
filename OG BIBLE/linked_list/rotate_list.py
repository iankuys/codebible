# Definition for singly-linked list.
# Given the head of a linked list, rotate the list to the right by k places.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear operation
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        cur = head
        length = 1

        while cur.next:
            length += 1
            cur = cur.next
        cur.next = head

        k = length - (k % length)

        while (k > 0):
            k -= 1
            cur = cur.next

        head = cur.next
        cur.next = None

        return head