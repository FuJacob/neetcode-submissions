class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ptr = 0
        n = len(nums)
        ans = float('inf')
        curr = 0
        for i in range(n):
            curr += nums[i]
            while ptr < n and curr >= target:
                ans = min(ans, i - ptr + 1)
                curr -= nums[ptr]
                ptr+=1
        return ans if ans != float('inf') else 0
        