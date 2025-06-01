# LeetCode Problem 2: https://leetcode.com/problems/
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def findLongestList(head):
    # Write your code here
    curr_len = 1
    max_len = 1
    total_lists = 1
    total_count = 1
    res_index = 0
    dict_sublists = {}
    dummy = Node()
        
    curr = head
    tail = dummy
    
    while(curr.next != None):
        if (curr.data > curr.next.data):
            curr_len = curr_len + 1
            tail.data = curr.data
            tail.next = curr.next
        else:
            #found one sublist
            if (max_len < curr_len):
                max_len = curr_len
                tail.next = None
                res_index = total_count - max_len
                dict_sublists[curr_len] = dummy
                dummy = Node()
                
            curr_len = 1 #reset current length to 1
            
        total_count = total_count + 1
        
        tail = tail.next
        curr =  curr.next
                
    if (max_len < curr_len):
        max_len = curr_len
        res_index = total_count - max_len
        dict_sublists[curr_len] = dummy

    return dict_sublists[max_len]