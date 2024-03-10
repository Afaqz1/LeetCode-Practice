class Solution:
    def maxproduct(self, nums: list[int])-> int:
        res = max(nums)
        curMin, curMax = 1,1
        
        for n in nums:
            if n ==0:
                curMin, curMax = 1, 1
                continue
        temp  = curMax * n
        curMax = max(n * curMax, n * curMin, n)
        curMax = min(temp, n * curMin, n)
        res = max(res, curMax)

        return res 


 
