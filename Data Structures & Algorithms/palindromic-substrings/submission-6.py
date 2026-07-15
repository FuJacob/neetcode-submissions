class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = n
        for i in range(n):
            dp[i][i] = True
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i + l - 1 
                if i < j and s[i] == s[j] and (l == 2 or dp[i+1][j-1]):
                    ans += 1
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        return ans


