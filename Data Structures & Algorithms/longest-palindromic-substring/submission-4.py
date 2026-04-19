class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        start = 0 ## record longest we seen so far
        max_len = 1 ## max length we sseen so far, we can create the string again by knowing these 2 variabels
        for length in range(2, n+1): ## try every lneght
            for i in range(n- length + 1): ## try every start
                j = i + length - 1
                if s[i] == s[j]: ## we are using dp so no nweed recheck fi paldriome, we cna check the inside
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and length > max_len: ## if we have a pladirome so far, then we can check length if it works
                    max_len = length
                    start = i
        return s[start:start+max_len]
        




        

        