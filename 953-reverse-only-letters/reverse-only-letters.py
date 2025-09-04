class Solution(object):
    def reverseOnlyLetters(self, s):
        arr = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if not arr[left].isalpha():
                left += 1
            elif not arr[right].isalpha():
                right -= 1
            else:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        return "".join(arr)