"""

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = 100000
        profit = 0
        for price in prices:
            min_prices = min(min_prices, price)
            profit = max(profit, price - min_prices)
        
        return profit

print(Solution().maxProfit([7,1,5,3,6,4]))