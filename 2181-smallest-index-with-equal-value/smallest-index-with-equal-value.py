class Solution(object):
    def smallestEqual(self, nums):
        n = len(nums)
        for i in range(n):
            if i % 10 == nums[i]:
                return i
        return -1

        
        