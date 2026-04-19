class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit = 0
        max_profit = 0
        buy_price = prices[0]

        for price in prices:
            if price - buy_price > curr_profit:
                curr_profit = price - buy_price
            else:
                max_profit += curr_profit
                curr_profit = 0
                buy_price = price
        max_profit += curr_profit

        return max_profit