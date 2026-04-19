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
            prevRob = currRob = 0
            for h in nums:
                nxtRob = max(prevRob + h, currRob)
                prevRob = currRob
                currRob = nxtRob
            return currRob
                
        
        return max(max_rob(nums[1:]), max_rob(nums[:-1]))