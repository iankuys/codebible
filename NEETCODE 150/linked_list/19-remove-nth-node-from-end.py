# LeetCode Problem 19: https://leetcode.com/problems/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# two pass
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head
        while first is not None:
            length += 1
            first = first.next
        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next
        first.next = first.next.next
        return dummy.next
    
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        # Advances first pointer so that the gap between first and second is n nodes apart
        for i in range(n + 1):
            first = first.next

        # Move first to the end, maintaining the gap
        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
    
class Solution:
    # Time Complexity:
    #   Best case: O(n) - linear operation
    #   Average case: O(n)
    #   Worst case: O(n)
    # Space Complexity: O(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newHead = ListNode(0)
        newHead.next = self.reverseLinkedList(head)
        dummy = newHead
        count = 0
        
        while newHead:
            if count == n:
                if count == 1 and head.next is None:
                    newHead.next = None
                    return newHead.next
                elif count == 1:
                    dummy.next = newHead.next
                    break
                else:
                    oldHead.next = newHead.next
            oldHead = newHead
            count+=1
            newHead = newHead.next
        
        return self.reverseLinkedList(dummy.next)
            
        
    def reverseLinkedList(self, head):
        dummy = ListNode()
        tail = dummy
        
        while head:
            if not tail:
                tail.next = head
                head = head.next
            else:
                dum2 = ListNode(head.val, tail.next)
                tail.next = dum2
                head = head.next
        
        return dummy.next