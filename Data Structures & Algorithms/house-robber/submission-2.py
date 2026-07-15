class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        ## rob
        ## no_rob
        rob = [0] * n
        no_rob = [0] * n
        rob[0] = nums[0]
        for i in range(1, n):
            rob[i] = no_rob[i-1] + nums[i]
            no_rob[i] = max(rob[i-1],no_rob[i-1])
        return max(no_rob[-1], rob[-1])
        