class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _max = 0
        ans = nums[0]
        for num in nums:
            _max += num
            ans = max(ans, _max)
            if _max < 0:
                _max = 0

        return ans
        