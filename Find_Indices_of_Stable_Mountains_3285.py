class Solution(object):
    def stableMountains(self, height, threshold):
        lis = []
        for i in range(1,len(height)):
            if height[i-1] > threshold and height[i-1] > 0:
                lis.append(i)
        return lis
