class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        lis = []
        for i in queries:
            s = 0
            m = min(i)
            c = i.count(m)
            for j in words:
                mt = min(j)
                ct = j.count(mt)
                if ct > c:
                    s = s+1
            lis.append(s)
        return lis
