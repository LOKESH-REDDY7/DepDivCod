class Solution(object):
    def findSubstring(self, s, words):

        if not s or not words:
            return []
        n = len(s)
        word_len = len(words[0])
        len_words = len(words)
        total_length = word_len * len_words
        result = []

        sorted_words = sorted(words)

        for i in range(n - total_length + 1):
            curr_sub = s[i:i+total_length]
            temp_words = []

            for j in range(0, total_length, word_len):
                temp_words.append(curr_sub[j:j+word_len])

            if sorted(temp_words) == sorted_words:
                result.append(i)

        return result