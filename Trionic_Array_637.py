class Solution(object):
    def isTrionic(self, nums):
        n = len(nums)
        if n < 3:
            return False
        p = -1
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                p = i
                break
        if p <= 0:
            return False

        q = -1
        for i in range(p, n - 1):
            if nums[i] < nums[i + 1]:
                q = i
                break
        if q <= p or q >= n - 1:
            return False

        def inc(arr, s, e):
            for i in range(s + 1, e + 1):
                if arr[i] <= arr[i - 1]:
                    return False
            return True

        def dec(arr, s, e):
            for i in range(s + 1, e + 1):
                if arr[i] >= arr[i - 1]:
                    return False
            return True

        if (inc(nums, 0, p) and dec(nums, p, q) and inc(nums, q, n - 1)):
            return True
        else:
            return False
