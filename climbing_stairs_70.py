class Solution(object):
    def climbStairs(self, n):
        if n <=1:
            return 1
        lis = [1,2]
        for i in range(2,n):
            lis.append(lis[i-1]+lis[i-2])
        return lis[-1]

        
