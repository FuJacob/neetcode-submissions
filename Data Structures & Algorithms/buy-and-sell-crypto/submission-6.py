class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        last_price = float('inf')
        for p in prices:
            if p < last_price:
                last_price = p
            else:
                max_profit = max(max_profit, p - last_price)
        return max_profit



