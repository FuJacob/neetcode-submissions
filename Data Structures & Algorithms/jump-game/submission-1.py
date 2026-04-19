class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        given nums where each elent numsi indicates maximum jump length @ position
        return true if. u cna reach the last index fattom frin 0

        Input: nums = [1,2,0,1,0]

        farthest_idx can reach
        1
        """
        n = len(nums)
        farthest_idx = nums[0]
        for idx, num in enumerate(nums):
            if idx <= farthest_idx:
                farthest_idx = max(farthest_idx, idx + num)
        return n - 1 <= farthest_idx