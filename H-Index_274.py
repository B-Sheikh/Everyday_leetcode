class Solution(object):
    def hIndex(self, citations):
        citations.sort(reverse=True)
        c = 0
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                c = i + 1
            else:
                break
        return c
