class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0] * (n+1)
        if 1 <= int(s[0]) <= 9:
            dp[0] = 1
        dp[1] = 1 if int(s[0]) != 0 else 0
        for i in range(2, n+1):
            take_one = int(s[i-1])
            take_two = int(s[i-2:i])
            if 1 <= take_one <= 9:
                dp[i] = dp[i-1]
            if 10 <= take_two <= 26:
                dp[i] += dp[i-2]
        return dp[-1]


