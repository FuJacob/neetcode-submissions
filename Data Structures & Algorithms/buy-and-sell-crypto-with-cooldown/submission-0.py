class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        rest = [0] * n
        sell = [0] * n
        hold = [0] * n
        ## x[i] repesnts max profit by day i doing x descision
        hold[0] = -prices[0]

        for i in range(1, n):
            sell[i] = hold[i-1] + prices[i]
            rest[i] = max(sell[i-1], rest[i-1])
            hold[i] = max(hold[i-1], rest[i-1] - prices[i])
        return max(rest[-1], sell[-1])


        
