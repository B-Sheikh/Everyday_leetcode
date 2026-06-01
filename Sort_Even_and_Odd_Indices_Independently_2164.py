class Solution(object):
    def sortEvenOdd(self, nums):
        ev = []
        od = []
        for i in range(len(nums)):
            if i%2 == 0:
                ev.append(nums[i])
            else:
                od.append(nums[i])
        ev.sort()
        od.sort(reverse=True)
        e = 0
        o = 0
        for i in range(len(nums)):
            if i%2 == 0:
                nums[i] = ev[e]
                e = e + 1
            else:
                nums[i] = od[o]
                o = o + 1

        return nums
