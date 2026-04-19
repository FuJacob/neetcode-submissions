class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        either we rob first hosue
        or we rob the last house.
        do house robber 2x

        one whre we rob the first one
        one where dont dont rob the first one, (we ARE ABLE OO rob the last one)
        max of which ever
        """
        def max_rob(nums):
            n = len(nums)
            if n < 2:
                return sum(nums)
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return dp[-1]
        if len(nums) < 2:
            return sum(nums)
        return max(max_rob(nums[1:]), max_rob(nums[:-1]))