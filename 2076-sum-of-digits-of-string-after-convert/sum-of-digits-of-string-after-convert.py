class Solution(object):
    def getLucky(self, s, k):
        res = ''
        for i in s:
            res += str(ord(i) - ord('a') + 1)

        while k > 0:
            temp = 0
            for j in res:
                temp += int(j)
            res = str(temp)
            k -= 1

        return int(res)

        