class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left += 1
            else:
                right -= 1
        return left 
        