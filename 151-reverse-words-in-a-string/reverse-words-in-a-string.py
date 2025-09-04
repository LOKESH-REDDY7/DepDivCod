class Solution(object):
    def reverseWords(self, s):
        new_arr = s.split()
        return " ".join(new_arr[::-1])

        