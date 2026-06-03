class Solution(object):
    def isValid(self, s):
        lis = []
        o = "([{"
        c = "])}"
        m = {")":"(","]":"[","}":"{"}
        for i in s:
            if i in o:
                lis.append(i)
            elif i in c:
                if not lis or lis[-1] != m[i]:
                    return False
                lis.pop()
        return not lis
