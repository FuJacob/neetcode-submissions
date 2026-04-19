class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        ## dp i j repesntes the amx amout nof coioins u can get fmro idx i to idx j not inclusive
        ## ah so thats why we need more 
        dp = [[0] * n for _ in range(n)]
        ## base case, well if ur i == j, then max amout nfo coins is ust the nums
        for i in range(n):
            dp[i][i] = nums[i]
        for length in range(2, n): ## in this case, n is already n + 1 
            for i in range(n-length):
                j = i + length
                ## try every idx to be teh last one popped
                for x in range(i+1, j):
                    coins = nums[x] * nums[i] * nums[j] + dp[i][x] + dp[x][j]                
                    dp[i][j] = max(dp[i][j], coins)
                    
        return dp[0][n-1]
