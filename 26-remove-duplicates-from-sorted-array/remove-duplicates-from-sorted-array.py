class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        n = len(nums)
        k = 1
        for i in range(1,n):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k+=1

        return k
                
        