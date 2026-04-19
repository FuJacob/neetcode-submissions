class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        ## cols represnet m
        ## rows represnt idx wre on 
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(1,n+1):
            dp[-1][i] = piles[-1]
        
        for i in range(n-1,-1,-1):
            for m in range(1, n+1):
                if i + 2 * m >= n:
                    dp[i][m] = sum(piles[i:])
                else:
                    ## we cant take all
                    ## try all X choices? 
                    max_stones = 0
                    for x in range(1, 2 * m + 1):
                        oppo_best = dp[i+x][max(m,x)]
                        my_score = sum(piles[i:]) - oppo_best
                        max_stones = max(max_stones, my_score)
                    

                    dp[i][m] = max_stones
        return dp[0][1]

