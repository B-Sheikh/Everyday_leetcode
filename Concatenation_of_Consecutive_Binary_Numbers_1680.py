class Solution(object):
    def concatenatedBinary(self, n):
        x = ""
        for i in range(1,n+1):
            x = x + format(i,'b')
        return int(x,2)%(10**9+7)
