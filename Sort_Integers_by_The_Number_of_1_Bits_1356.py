class Solution(object):
    def sortByBits(self, arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(n-i-1):
                if (bin(arr[j]).count("1") > bin(arr[j+1]).count("1")) or \
                   (bin(arr[j]).count("1") == bin(arr[j+1]).count("1") and arr[j] > arr[j+1]):
                    
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
