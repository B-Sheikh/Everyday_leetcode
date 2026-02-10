class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        
        n = len(nums1)
        if n % 2 == 0:
            m = n//2
            med = (nums1[m-1] + nums1[m])/2.0
        else:
            m = n//2
            med = nums1[m]
        
        return med
