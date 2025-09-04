class Solution(object):
    def countVowels(self, word):
        n = len(word)
        vowels = 'aeiou'
        count = 0
        for i, ch in enumerate(word):
            if ch in vowels:
                count += (i + 1)*(n - i)

        return count

