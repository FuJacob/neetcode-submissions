class Solution:
    def rob(self, nums: List[int]) -> int:
        robbed = {0: nums[0]}
        not_robbed = {0: 0}
        def dfs(i): ## most amount of money assuming i robbed this current house
            if i == 0:
                return nums[0]
            if i in robbed:
                return max(robbed[i], not_robbed[i])
            dfs(i-1)
            not_robbed[i] = max(robbed[i-1], not_robbed[i-1])
            robbed[i] = not_robbed[i-1] + nums[i]
            return max(robbed[i], not_robbed[i])
        return dfs(len(nums)-1)