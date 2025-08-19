class Solution(object):
    def maxArea(self, height):
        n = len(height)
        l = 0
        r = n - 1
        max_water = 0
        while l < r:
            width = r - l
            h = min(height[l], height[r])
            max_water = max(max_water, h * width)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water

         
            
