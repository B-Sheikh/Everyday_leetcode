class Solution(object):
    def plusOne(self, digits):
        a = ""
        for i in digits:
            a = a+str(i)
        a = int(a)
        a = str(a+1)
        lis = []
        for i in a:
            lis.append(int(i))
        return lis
        
