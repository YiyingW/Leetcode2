# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
    
        pre = [None]
        self.helper(root, pre)
        
    def helper(self, root, pre):
        if root:
            self.helper(root.right, pre)
            self.helper(root.left, pre)
            
            root.right = pre[0]
            root.left = None
            pre[0] = root
        
        
