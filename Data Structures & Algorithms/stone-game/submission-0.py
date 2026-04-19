class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        ## actualy needs to be teh point difference
        ## because otherwise im not saving any info. current player loses, is not necessiarly true
        ### dp i j shoudl reppsetn the best point diff for hte currnet player
        for i in range(n):
            dp[i][i] = piles[i]
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1

                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        return dp[0][-1] > 0
