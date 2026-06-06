class Solution(object):
    def similarPairs(self, words):
        def sim(x):
            l = ""
            for i in x:
                if i not in l:
                    l += i
            return ''.join(sorted(l))

        lis = []
        for i in words:
            lis.append(sim(i))

        c = 0
        for i in range(len(lis)):
            for j in range(i + 1, len(lis)):
                if lis[i] == lis[j]:
                    c += 1

        return c
