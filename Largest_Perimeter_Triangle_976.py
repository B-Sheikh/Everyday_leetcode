class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort()
        s = 0
        ma = []
        n = 0
        for i in range(2,len(nums)):
            if nums[i-2] + nums[i-1] > nums[i] and nums[i-1] + nums[i] > nums[i-2] and nums[i] + nums[i-2] > nums[i-1]:
                s = nums[i] + nums[i-1] + nums[i-2]
                ma.append(s)
        for i in ma:
            if i >n:
                n = i
        return n
