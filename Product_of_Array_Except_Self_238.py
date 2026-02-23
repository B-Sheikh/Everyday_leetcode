class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        pr = [1] * n
        l= 1
        for i in range(n):
            pr[i] = l
            l= l*nums[i]
        r = 1
        for i in range(n-1, -1, -1):
            pr[i] = pr[i]*r
            r= r*nums[i]
        
        return pr
