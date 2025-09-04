class Solution(object):
    def reverseWords(self, s):
        new_arr = s.split()
        new_res = []
        for i in new_arr:
            new_res.append(i[::-1])

        return " ".join(new_res)
        