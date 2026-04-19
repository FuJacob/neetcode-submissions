class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthest_idx = 0
        tmp_farthest_idx = 0
        n = len(nums)
        for idx, jump in enumerate(nums):
            if idx > farthest_idx:
                jumps+=1
                farthest_idx = tmp_farthest_idx
            tmp_farthest_idx = max(tmp_farthest_idx, idx+jump)
            if n - 1 <= farthest_idx:
                return jumps
        return jumps


            