# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # reverse the linked list and return head
        
        # want: go down list -> hit tail -> go back up
        # give back node representing head of list
        
        # base case: no node
        if head == None:
            return None
          
        # base case: single node
        if head.next == None:
            return head
          
        else:
            # construct new nodes
            result = ListNode(head.val, None)
            head = head.next
            
            while head.next != None:
                # make last node and update to point to tail
                newNode = ListNode(head.val, result)
                # update result pointer
                result = newNode
                # continue down original chain
                head = head.next
                
            # no next but node remains in head
            lastNewNode = ListNode(head.val, result)
            result = lastNewNode
            
        return result 
