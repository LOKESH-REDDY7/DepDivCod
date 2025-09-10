class Solution(object):
    def removeElement(self, nums, val):
        new_val = 0
        for value in range(len(nums)):
            if nums[value] != val:
                nums[new_val] = nums[value]
                new_val += 1
        return new_val