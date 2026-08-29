class Solution(object):
    def subsetXORSum(self, nums):
        if len(nums) <= 0:
            return 0
        n = 0
        for i in nums:
            n = n|i
        return n * 2**(len(nums)-1)
