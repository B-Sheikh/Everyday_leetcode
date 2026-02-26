class Solution(object):
    def numSteps(self, s):
        n = int(s,2)
        s = 0
        while n!= 1:
            if n%2 == 0:
                n = n/2
            else:
                n = n+1
            s = s +1
        return s
        
