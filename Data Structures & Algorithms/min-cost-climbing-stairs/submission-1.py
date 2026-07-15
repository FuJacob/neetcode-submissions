class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ## let dp i represtn the min cost to reach top of staircase of ith floor
        ## to get there either we paid the price -1 or -2 before
        n = len(cost)
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[-1]
