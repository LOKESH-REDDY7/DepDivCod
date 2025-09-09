class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_num = 0
        n = len(s)
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break

                seen.add(s[j])
                max_num = max(max_num, j - i + 1)
        return max_num


        