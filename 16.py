class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        current = 2**31-1
        res = 0
        
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            
            while l < r:
                if nums[i] + nums[l] + nums[r] == target:
                    return target
                if abs(nums[i] + nums[l] + nums[r] - target) < current:
                    current = abs(nums[i] + nums[l] + nums[r] - target)
                    res = nums[i] + nums[l] + nums[r]
                if nums[i] + nums[l] + nums[r] - target > 0:
                    r -= 1
                else:
                    l += 1
        return res
                    
