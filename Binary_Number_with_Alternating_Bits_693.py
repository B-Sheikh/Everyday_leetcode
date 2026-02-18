class Solution(object):
    def hasAlternatingBits(self, n):
        s = format(n,"b")
        t = True
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                t = False
        return t
