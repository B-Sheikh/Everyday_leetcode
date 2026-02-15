class Solution(object):
    def countElements(self, nums, k):
        y = list(nums)
        y.sort()
        s = 0
        n = len(y)
        i = 0
        while i < n:
            j = i
            while j < n and y[j] == y[i]:
                j = j + 1
            z = n-j
            if z >= k:
                s = s + (j-i)
            i = j

        return s
