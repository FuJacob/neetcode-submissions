class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        edit dist
        given 2 strings
        wrod 1
        word 2

        rpeform 3 ops

        word 1
        insert 
        del
        replace

        return min ops to make wrd1 eqal tword 2

        dp i j reprensts min ops to make word1 from ith to word2 same 
        """
        m,n = len(word1), len(word2)
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        dp[0][0] = 0
        for i in range(1, m+1):
            dp[i][0] = i
        for i in range(1, n+1):
            dp[0][i] = i
        for i in range(1, m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[m][n]
                
