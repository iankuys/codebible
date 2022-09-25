    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyNode = ListNode()
        tail = dummyNode #tail is also head
        
        while (list1 and list2):
            if (list1.val < list2.val):
                tail.next = list1
                list1, tail = list1.next, tail.next
            else:
                tail.next = list2
                list2, tail = list2.next, tail.next
                
        if(list1): tail.next = list1
        if(list2): tail.next = list2
        
        
        return dummyNode.next
                