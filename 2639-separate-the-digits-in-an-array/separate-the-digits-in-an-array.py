class Solution(object):
    def separateDigits(self, nums):
        res = []
        for i in nums:
            if len(str(i)) > 1:
                for j in str(i):
                    res.append(int(j))

            else:
                res.append(i)

        return res

        