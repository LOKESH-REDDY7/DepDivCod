class Solution(object):
    def maxProfit(self, prices):
        min_profit = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_profit:
                min_profit = price
            elif price - min_profit > max_profit:
                max_profit = price - min_profit

        return max_profit

        
        