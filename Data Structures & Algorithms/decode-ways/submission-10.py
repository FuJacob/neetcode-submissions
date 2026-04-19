class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * n
        dp[0] = 1
        if n < 2:
            return dp[0]
        if int(s[1]) != 0:
            dp[1] = dp[0] 
        if 10 <= int(s[:2]) <= 26:
            dp[1] += 1
        for i in range(2, n):
            take_one = int(s[i])
            take_two = int(s[i-1] + s[i])
            if 1 <= take_one <= 9:
                dp[i] = dp[i-1]
            if 10 <= take_two <= 26:
                dp[i] += dp[i-2]
        return dp[-1]


