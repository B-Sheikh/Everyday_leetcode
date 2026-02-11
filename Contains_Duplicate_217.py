class Solution(object):
    def containsDuplicate(self, nums):
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] = dic[i] +1
        t = False
        for i in dic:
            if dic[i] >1:
                t = True
        return t
