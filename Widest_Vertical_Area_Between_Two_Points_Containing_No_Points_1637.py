class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        lis = []
        for i in points:
            lis.append(i[0])
        lis.sort()
        m = 0
        for i in range(1, len(lis)):
            m = max(m, lis[i] - lis[i-1])
        return m
