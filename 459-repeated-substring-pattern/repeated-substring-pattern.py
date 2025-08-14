class Solution(object):
    def repeatedSubstringPattern(self, s):
        if s in s[1:] + s[:-1]:
            return True

        else:
            return False        