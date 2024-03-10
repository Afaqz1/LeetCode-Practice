class Solution:
    def reversebits(self, nums: int) ->int:
        res = 0

        for i in range(32):
            bit = (nums >> 1) &1
            res | (bit << (31 - i))
        return res