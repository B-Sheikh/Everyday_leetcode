class Solution(object):
    def reverseBits(self, n):
        s = bin(n)[2:]

        def recu(s):
            if len(s) == 32:
                return s
            return recu("0" + s)

        x = recu(s)
        return int(x[::-1], 2)
