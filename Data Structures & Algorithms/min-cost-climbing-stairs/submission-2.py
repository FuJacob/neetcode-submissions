class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i <= 1:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = min(dfs(i-1) +cost[i-1], dfs(i-2) +cost[i-2])
            return memo[i]
        return dfs(len(cost)) ## cost ot hit the top of this 
