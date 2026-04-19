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
        if len(nums) < 2:
            return sum(nums)
        
        def max_rob(nums):
            n = len(nums)
            if n < 2:
                return nums[0]
            rob1 = rob2 = 0
            for h in nums:
                new_rob = max(h + rob1, rob2)
                rob1 = rob2
                rob2 = new_rob
            return rob2
        
        return max(max_rob(nums[1:]), max_rob(nums[:-1]))