class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        ans = 0
        for num in nums:
            if num-1 not in seen:
                curr = 1
                while num + curr in seen:
                    curr+=1
                ans = max(curr,ans)
        return ans




