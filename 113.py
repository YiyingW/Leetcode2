# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        self.dfs(root, sum, [], res)
        return res
        
    def dfs(self, root, sum, current, res):
        if root:
            if not root.left and not root.right and root.val == sum:
                res.append(current + [root.val])
                return 
            self.dfs(root.left, sum - root.val, current + [root.val], res)
            self.dfs(root.right, sum - root.val, current + [root.val], res)
        
        
