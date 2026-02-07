class Solution(object):
    def countPrimeSetBits(self, left, right):
        def isprime(n):
            if n <= 1:
                return False
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True
        
        def bin_con(n):
            res = ''

            while n > 0:
                res = str(n % 2) + res
                n //= 2
            return int(res)

        sum = 0
        for i in range(left,right+1):
            bin = str(bin_con(i))
            s = bin.count("1")
            if isprime(s):
                sum =sum+1
        return sum



        
