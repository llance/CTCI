# Given a linked list, swap every two adjacent nodes and return its head.

# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):gs
        """
        :type head: ListNode
        :rtype: ListNode
        """

        curr = dummy = ListNode(0)

        dummy.next = head

        while curr.next and curr.next.next:
            temp = curr.next.next
            curr.next.next = curr
            curr.next = temp
            curr = temp

        return dummy.next