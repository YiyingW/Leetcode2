# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        return self.dfs(nums, 0, len(nums)-1)
        
    def dfs(self, nums, l, r):
        if l <=r:
            mid = l + (r - l) / 2
            root = TreeNode(nums[mid])
            root.left = self.dfs(nums, l, mid-1)
            root.right = self.dfs(nums, mid+1, r)
            return root 
