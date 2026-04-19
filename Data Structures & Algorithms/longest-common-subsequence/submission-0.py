class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        given 2 strings text1 text2, return legnth of LCS between 2 strings if one exists
        otherwise return 0.

        subsequcne is seqeunce that cna be derived from given seuq
        delet some or not 

        comon subsequence
        LCS
        dp i j represnts lenght ofl ongest LCS by index i 
        """
        m,n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[m][n]