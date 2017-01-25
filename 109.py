# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.myTree(head, None)
    
    def myTree(self, l, r):
        
        if not l:
            return None
        if l == r:
            return None
        fast = l
        slow = l
        
        while fast != r and fast.next != r:
            slow = slow.next
            fast = fast.next.next
            
        root = TreeNode(slow.val)
        root.left = self.myTree(l, slow)
        root.right = self.myTree(slow.next, r)
        return root
        
