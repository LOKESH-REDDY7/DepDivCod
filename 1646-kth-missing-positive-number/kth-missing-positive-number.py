class Solution(object):
    def findKthPositive(self, arr, k):
        s = set(arr)
        count = 0
        curr = 0
        while  count < k:
            curr+=1
            if curr not in s:
                count+=1

        return curr
        