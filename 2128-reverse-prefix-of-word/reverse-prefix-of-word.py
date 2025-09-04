class Solution(object):
    def reversePrefix(self, word, ch):
        if ch not in word:
            return word
        elif ch in word:
            num = word.index(ch)
            reversed_word = word[:num+1][::-1]
            remaining_word = word[num+1:]
            result_word = reversed_word + remaining_word
            return result_word

            

        

        
        