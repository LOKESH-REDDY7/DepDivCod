class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        max_sum =  nums[0]
        curr_sum = nums[0]
        for i in range(1,n):
            curr_sum = max(curr_sum+nums[i], nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum


        