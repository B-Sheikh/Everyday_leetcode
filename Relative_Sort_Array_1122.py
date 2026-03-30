class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        lis = []
        for i in arr2:
            c = arr1.count(i)
            for j in range(c):
                lis.append(i)
        nlis = []
        for j in arr1:
            if j not in lis:
                nlis.append(j)
        nlis.sort()
        return lis+nlis
