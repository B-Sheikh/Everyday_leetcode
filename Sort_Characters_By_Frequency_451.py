class Solution(object):
    def frequencySort(self, s):
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] = dic[i] + 1
        t = ""
        while len(dic) > 0:
            m = 0
            c = ""
            for j in dic:
                if dic[j] > m:
                    m = dic[j]
                    c = j
            t = t + c * m
            del dic[c]
        return t
