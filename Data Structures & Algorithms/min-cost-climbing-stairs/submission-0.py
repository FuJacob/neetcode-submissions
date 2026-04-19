class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        given cost 
        cost taking step frim ith floor
        pay ost, ether go to ith or ith+ 2 floor 

        start 0 and 1 for free

        """
        n = len(cost)
        dp = [float('inf')] * (n+1) ## here we have infinite cost to reach this part of stair case
        ## n + 1 cjuz we want to reach the index just after 
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
            ## dp i is min if either going from the one boefre or the 2 before 
        return dp[-1]
