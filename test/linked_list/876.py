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
            count2 = count2 + 1
            if(count2 == middle):
                tail.next = head
                return tail.next
            head = head.next
                
        return tail.next