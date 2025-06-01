# LeetCode Problem 234: https://leetcode.com/problems/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        return self.areIdentical(head, self.reverseList(head))

    def areIdentical(self, head1, head2):
        while (head1 and head2):
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        
        return ( head1 == None and head2 == None)

    def reverseList(self, head):
        dummy = ListNode(0)
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