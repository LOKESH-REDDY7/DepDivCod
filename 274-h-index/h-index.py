class Solution(object):
    def hIndex(self, citations):
        citations.sort(reverse=True)
        n = len(citations)
        count = 0
        while count < n and citations[count] > count:
            count+=1

        return count
        