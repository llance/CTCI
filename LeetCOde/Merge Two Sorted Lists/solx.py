# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        mergedList = ListNode(None)
        curr = mergedList
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        while l1 or l2:
            # print("l1 is : ", l1.val, " l2 is : ", l2.val)
            if l1 and not l2:
                curr.next = ListNode(l1.val)
                curr = curr.next
                l1 = l1.next
            if l2 and not l1:
                curr.next = ListNode(l2.val)
                curr = curr.next
                l2 = l2.next
            if l1 and l2:    
                if l1.val >= l2.val:
                    curr.next = ListNode(l2.val)
                    l2 = l2.next 
                    # curr = curr.next
                    # curr.next.next = ListNode(l1.val)

                else:
                    curr.next = ListNode(l1.val)
                    # curr = curr.next
                    # curr.next.next = ListNode(l2.val)
                    l1 = l1.next

                curr = curr.next
                
                
            
        return mergedList.next