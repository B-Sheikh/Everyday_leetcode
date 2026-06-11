class Solution(object):
    def clearDigits(self, s):
        t = ""
        for i in s:
            if i.isdigit():
                t = t[:-1]
            else:
                t = t + i
        return t
