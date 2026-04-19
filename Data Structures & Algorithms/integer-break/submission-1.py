class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n+1)
        ## 1 1 1 1 1
        for num in range(2, n+1):
            ## pos, need leave at elast 1 so have 2 nums pos
            for num_part in range(1, num):
                ## keep brekaing apart
                dp[num] = max((num-num_part) * num_part, dp[num-num_part] * num_part, dp[num])
        return dp[n]




