class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        ## dp[i] = minimum extra characters in s[:i]
        n = len(s)
        dp = [n] * (n+1)

        dp[0] = 0

        dictionary.sort(key=len)
        for i in range(1, n+1):
            for word in dictionary:
                if len(word) <= i:
                    if word == s[i-len(word):i]:
                        dp[i] = min(dp[i], dp[i-len(word)])
            dp[i] = min(dp[i], 1 + dp[i-1])
        return dp[-1]
            


