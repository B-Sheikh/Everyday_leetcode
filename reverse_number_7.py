class Solution(object):
    def reverse(self, x):
        neg = False
        if x < 0:
            neg = True
            x = abs(x)

        s = ""
        while x > 0:
            d = x % 10
            s = s + str(d)
            x = x // 10

        s = int(s) if s else 0
        if neg:
            s = -s
        if (s <= -2**31 or s>= 2**31-1):
            return 0

        return s
