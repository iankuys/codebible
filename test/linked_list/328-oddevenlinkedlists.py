# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = ListNode(0)
        even_tail = even

        odd = ListNode(0)
        odd_tail = odd
        count = 1

        while head:
            if count % 2 == 0:
                even_tail.next = head
                even_tail = even_tail.next
            else:
                odd_tail.next = head
                odd_tail = odd_tail.next
            head = head.next
            count+=1

        even_tail.next = None
        odd_tail.next = even.next

        return odd.next