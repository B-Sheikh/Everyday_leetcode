class Solution(object):
    def majorityElement(self, nums):
        if len(nums) == 1:
            return nums[0]
        max = 0
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            elif i in dic :
                dic[i] = dic[i] +1
                if  max < dic[i]:
                    max = dic[i]
        for i in dic:
            if dic[i] == max:
                return i
