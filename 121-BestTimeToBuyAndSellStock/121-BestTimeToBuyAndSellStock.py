# Last updated: 8/16/2026, 9:52:19 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf") # current min price
        res = 0

        for price in prices:
            res = max(res, price - min_price)
            min_price = min(price, min_price)
        
        return res