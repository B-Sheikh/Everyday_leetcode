class Solution(object):
    def selfDividingNumbers(self, left, right):
        def selfdiv(x):
            f = True
            for i in str(x):
                if i == "0" or x%int(i) != 0:
                    f = False
                    break
            return f
        lis = []
        for i in range(left,right+1):
            if selfdiv(i):
                lis.append(i)
        return lis
