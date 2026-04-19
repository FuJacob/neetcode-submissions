class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _max = nums[0]
        ans = nums[0]
        for num in nums[1:]:
            _max = max(num, _max + num)
            ans = max(_max, ans)
        return ans
        