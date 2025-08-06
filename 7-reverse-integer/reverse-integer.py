class Solution(object):
    def reverse(self, x):
        if x < 0:
            res = int("-"+str(int(abs(x)))[::-1])
        else:
            res = int(str(int(abs(x)))[::-1])

        if res < -2**31 or res > 2**31 - 1:
            return 0
        else:
            return res