class Solution(object):
    def titleToNumber(self, columnTitle):
        n = 0
        s = str(columnTitle)
        for i in s:
            n = n*26 + (ord(i)-ord("A")+1)
        return n
