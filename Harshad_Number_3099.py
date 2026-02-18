class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        def sum(x):
            s = 0
            for i in str(x):
                s = s + int(i)
            return s
        s = sum(x)
        if x%s==0:
            return s
        else:
            return -1
