class Solution(object):
    def maximumGap(self, nums):
        if len(nums) <2:
            return 0
        ma = 0
        nums.sort()
        for i in range(1,len(nums)):
            if ma < nums[i] - nums[i-1]:
                ma = nums[i] - nums[i-1]
        return ma
        
