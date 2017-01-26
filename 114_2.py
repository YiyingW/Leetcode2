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
        if root:
            pre = None
            stack = [(root, False)]
            while stack:
                cur, flag = stack.pop()
                if flag:
                    cur.right = pre
                    cur.left = None
                    pre = cur
                else:
                    stack.append((cur, True))

                    if cur.left:
                        stack.append((cur.left, False))
                    if cur.right:
                        stack.append((cur.right, False))
                    
