class Solution(object):
    def isHappy(self, n):                
        def numsq(x):
            s = 0
            while x > 0:
                d = x%10
                s = s + d**2
                x = x//10
            return s
        st = set()
        while True:
            n = numsq(n)
            if n == 1:
                return True
            if n in st:
                return False
            st.add(n)

        
