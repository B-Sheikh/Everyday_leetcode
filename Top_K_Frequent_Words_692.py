class Solution(object):
    def topKFrequent(self, words, k):
        dic = {}
        for i in words:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        lis = []
        num = []
        for i in dic:
            lis.append(i)
            num.append(dic[i])
        nlis = []
        for _ in range(k):
            f = -1
            c = ""
            d = -1
            for j in range(len(num)):
                if num[j] > f or (num[j] == f and lis[j] < c):
                    f = num[j]
                    c = lis[j]
                    d = j
            
            nlis.append(c)
            num[d] = -1
        
        return nlis
