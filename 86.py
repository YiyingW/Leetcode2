# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = ListNode(0)
        h2 = ListNode(0)
        
        cur1 = h1
        cur2 = h2
        
        while head:
            if head.val < x:
                cur1.next = ListNode(head.val)
                cur1 = cur1.next
            else:
                cur2.next = ListNode(head.val)
                cur2 = cur2.next
            head = head.next
        cur1.next = h2.next
        cur2.next = None
        
        return h1.next
