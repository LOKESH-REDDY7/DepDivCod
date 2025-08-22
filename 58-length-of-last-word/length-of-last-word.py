class Solution(object):
    def lengthOfLastWord(self, s):
        arr = list(s.split())
        return len(arr[-1])
        