# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# merge sort
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        left = self.sortList(head)
        print('starting right')
        right = self.sortList(head2)

        return self.merge(left, right)

    def merge(self, head1, head2):
        dummy = ListNode(0)
        tail = dummy

        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        if head1:
            tail.next = head1
        if head2:
            tail.next = head2

        return dummy.next

# cheesy solution
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        array = []
        dummy = ListNode(0)
        tail = dummy
        i = 0

        while head:
            array.append(head.val)
            head = head.next

        array.sort()

        while i <= len(array) - 1:
            node = ListNode(array[i], None)
            tail.next = node
            tail = tail.next
            i += 1
        
        return dummy.next
            