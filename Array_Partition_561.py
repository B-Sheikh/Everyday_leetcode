class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        ma = 0
        for i in range(len(nums)):
            if i%2 == 0:
                ma= ma +nums[i]
        return ma

