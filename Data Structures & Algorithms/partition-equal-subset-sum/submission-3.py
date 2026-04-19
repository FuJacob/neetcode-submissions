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
        ## dp i repsesnting whether can have a subset to make i amount
        ## try every single num, if we can make bob, then tgeb uf wue ba nae dpi-1
        dp = [False] * (half+1)
        dp[0] = True
        for num in nums:
            for i in range(half,num - 1, -1): ## IT REUSES IF NOT BACKWARDS CUZ WE DOIGN SMALLER THEN GOIGN TO BIGGER
                if dp[i-num]: ## IF CAN MAKE SUBSET TI MAKE DP I - NUM THEN GOOD 
                    dp[i] = True
        return dp[half]