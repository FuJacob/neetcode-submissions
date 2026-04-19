class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0] * n
        if 1 <= int(s[0]) <= 9:
            dp[0] = 1

        
        for i in range(1, n):
            take_one = int(s[i])
            take_two = int(s[i-1] + s[i])
            ## dp i representing the # of ways to decode by ith index of string.

            if 1 <= take_one <= 9: ## if we cna add naother integer right now. ## how many ways decode?
            ## its jsut ogoing to be # of ways te decode dpi-1
                dp[i] = dp[i-1]
            ## what if we cna ahve 2 work? 
            ## then dp i is just gonan be e# ways to decipde dpi-2
            if 10 <= take_two <= 26:
                if i-2 >= 0:
                    dp[i] += dp[i-2]
                else:
                    dp[i] += 1

            ## if both work, then we add both. why? because this means that both dp i-2 # ways to decode we need to add it 
            
        return dp[-1]


