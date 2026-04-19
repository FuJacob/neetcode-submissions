class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for num in range(1,n+1):
            for num_part in range(int(num ** 0.5), -1,-1):
                dp[num] = min(dp[num-num_part*num_part]+1, dp[num])
        return dp[n]



