class Solution(object):
    def twoSum(self, nums, target):
        n = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] +nums[j] == target and (nums[i] != nums[j] or i != j):
                    n.extend([i,j])
                    break
        return n
        
