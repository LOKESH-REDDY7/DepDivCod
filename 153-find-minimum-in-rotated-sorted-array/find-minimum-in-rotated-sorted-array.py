class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        min_ele = nums[0]
        for i in range(1,n):
            min_ele = min(min_ele, nums[i])

        return min_ele