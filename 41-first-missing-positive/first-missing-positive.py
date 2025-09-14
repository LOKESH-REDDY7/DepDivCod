class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 1
        for i in nums:
            if i == res:
                res += 1
            if i > res:
                return res
        return res

        