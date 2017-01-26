class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        
        mostWater = 0
        
        while l < r:
            currentWater = min(height[l], height[r])*(r-l)
            mostWater = max(mostWater, currentWater)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return mostWater
