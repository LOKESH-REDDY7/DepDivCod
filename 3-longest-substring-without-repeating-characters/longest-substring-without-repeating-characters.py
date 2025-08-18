class Solution(object):
    def lengthOfLongestSubstring(self, s):
        best = 0
        n = len(s)
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break

                seen.add(s[j])
                best = max(best, j - i + 1)
        return best


