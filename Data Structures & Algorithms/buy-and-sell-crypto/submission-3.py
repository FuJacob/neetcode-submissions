class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        curr_profit = 0
        last_price = prices[0]
        for i in range(len(prices)):
            curr_profit = prices[i] - last_price
            if curr_profit < 0:
                curr_profit = 0
                last_price = prices[i]
            else:
                max_profit = max(max_profit, curr_profit)
        return max_profit
    """
    [5, 7, 1]
    last 1
    max_profit = 4
    curr_profit = 4

    
    """
            
            
