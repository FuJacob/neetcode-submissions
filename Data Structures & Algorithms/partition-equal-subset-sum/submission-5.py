class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        nums => array of positive integers
        return true if can partition array into 2 subsets
        theyre equal
        postive so if odd numbers then cooked.
        """
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False
        half = total // 2
        dp = [False] * (half+1)
        dp[0] = True
        for num in nums:
            for i in range(half,num - 1, -1): 
                if dp[i-num]: 
                    dp[i] = True
        return dp[half]