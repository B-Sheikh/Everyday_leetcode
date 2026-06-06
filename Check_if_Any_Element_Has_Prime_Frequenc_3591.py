class Solution(object):
    def checkPrimeFrequency(self, nums):
        def isp(x):
            c = 0
            for i in range(1,x+1):
                if x%i == 0:
                    c = c +1
            if c == 2:
                return True
            else:
                return False
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] = dic[i] +1
        for j in dic:
            if isp(dic[j]):
                return True
        return False

        
