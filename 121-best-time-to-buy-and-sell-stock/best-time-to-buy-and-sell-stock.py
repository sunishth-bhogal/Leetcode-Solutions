class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price_so_far = prices[0]
        max_profit_so_far = 0

        for i in range(len(prices)):
            if prices[i] < min_price_so_far:
                min_price_so_far = prices[i]
            if prices[i] - min_price_so_far > max_profit_so_far:
                max_profit_so_far = prices[i] - min_price_so_far

        return max_profit_so_far

        
