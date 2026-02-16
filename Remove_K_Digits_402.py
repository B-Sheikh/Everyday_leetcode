class Solution(object):
    def removeKdigits(self, num, k):
        x = num
        y = ""
        lis = []
        for i in x:
            while k > 0 and lis and lis[-1] > i:
                lis.pop()
                k = k - 1
            lis.append(i)
        while k > 0:
            lis.pop()
            k = k - 1
        for i in lis:
            y = y + i
        y = y.lstrip("0")
        if y == "":
            return "0"
        return y
