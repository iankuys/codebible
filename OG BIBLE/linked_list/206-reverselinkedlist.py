# Link: https://leetcode.com/problems/reverse-linked-list/
#206. Reverse Linked List

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
        
    while(head):
            
        if(not tail):
            tail.next = head
            head = head.next
        else:
            dum2 = ListNode(head.val, head.next)
            dum2.next = tail.next
            tail.next = dum2
            head = head.next
                
                        
    return dummy.next