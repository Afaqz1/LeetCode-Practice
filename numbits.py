class Solution:
    def numbits(self, n:int)-> int:
        """ Simple Solution
        res = 0
        while n:
            res += n%2
            n = n>>1
        return res"""
        res = 0
        while n:
            n &= (n-1)
            res += 1
            n = n>>1
        return res