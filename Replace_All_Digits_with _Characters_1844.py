class Solution(object):
    def replaceDigits(self, s):
        t = ""
        for i in s:
            if i.isdigit():
                t += chr(ord(t[-1]) + int(i))
            else:
                t += i
        return t
