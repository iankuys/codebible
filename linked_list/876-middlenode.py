# smart as fuck, use two pointers fast and slow, fast will travel twice the speed. SO when traverse till the end the slow will
# have to be in the middle node

class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    count = 0
    count2 = 0
    tail = dummy = ListNode()
    temp = head
    
    while(temp):    
        count = count+1
        temp = temp.next
    
    middle = count/2
    
    if(isinstance(middle, float)):
        middle = int(middle+1)
    else:
        middle = int(middle) + 1
        
    print(middle)
        
    while(head):
        if((count2 := count2 + 1) == middle):
            tail.next = head
            return tail.next
        head = head.next
            
    return tail.next
