class Solution(object):
    def countBits(self, n):
        lis =[]
        for i in range(n+1):
            lis.append(bin(i).count("1"))
        return lis
        
