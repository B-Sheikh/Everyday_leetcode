class Solution(object):
    def searchInsert(self, nums, target):
        t = False
        
        for i in range(len(nums)):
            if nums[i] == target:
                t = True
                return i
        
        if not t:
            for j in range(len(nums)-1):
                if nums[j]<target and nums[j + 1]>target:
                    return j+1
            
            if target>nums[-1]:
                return len(nums)
            else:
                return 0
