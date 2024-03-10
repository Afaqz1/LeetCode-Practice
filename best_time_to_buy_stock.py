class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1 # Left= buy, right = sell
        maxP = 0

        while r < len(prices):
            # profitTable 
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        
        return maxP
