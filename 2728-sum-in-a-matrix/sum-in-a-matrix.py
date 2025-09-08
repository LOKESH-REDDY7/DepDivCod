class Solution(object):
    def matrixSum(self, nums):
        for row in nums:
            row.sort(reverse=True)
        sum = 0
        n = len(nums)
        m = len(nums[0])
        for i in range(m):
            max_element = 0
            for j in range(n):
                max_element = max(max_element, nums[j][i])
            sum += max_element
        return sum
        # num_rows = len(nums)
        # num_columns = len(nums[0])
        # sum = 0
        # for i in range(num_columns):
        #     min_element = 0
        #     for j in range(num_rows):
        #         element = nums[j][i]
        #         if element > min_element:
        #             min_element = element
        #     sum = sum + min_element

        # return sum


        