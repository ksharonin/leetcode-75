# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    
# Definition for Linked List instance
# class LinkedList:
    # def __init__(self):
       # self.head = None 
        
class Solution(object):
  
    def __init__(self):
            head = None
        
    def mergeTwoLists(self, list1, list2):
        dummy = None
        
        # base cases
        if not list1:
            return list2
        if not list2:
            return list1
        
        # both existent 
        if list1 and list2:
          
            if list1.val <= list2.val:
                dummy = list1
                list1 = dummy.next
            else:
                dummy = list2
                list2 = dummy.next
            # pointer to front, will be returned
            
            new_node = dummy
            
        # iterate through the rest of the lists
        while list1 and list2:
          
            if list1.val <= list2.val:
                dummy.next = list1
                summy = list1
                list1 = dummy.next
                
            else:
                dummy.next = list2
                dummy = list2
                list2 = dummy.next
                
        # if one runs out, point rest to remaining
        if not list1:
            dummy.next = list2
        if not list2:
            dummy.next = list1
            
        return new_node
