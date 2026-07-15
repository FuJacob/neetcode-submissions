class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dp[i][j] = True
        
        best_length = 1 
        best_start = 0
        for length in range(2,n+1):
            for i in range(0, n-length+1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    best_length = length
                    best_start = i

        return s[best_start:best_start+best_length]



