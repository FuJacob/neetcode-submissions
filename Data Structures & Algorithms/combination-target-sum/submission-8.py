class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        curr = []
        ans = []
        seen = set()
        def backtrack(start):
            if sum(curr) == target:
                ans.append(curr[:])
            
            if start >= n or sum(curr) > target:
                return
            
            for i in range(start, n):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                ## start? no u can only start picking unbers on me and after
                backtrack(i)
                curr.pop()
        backtrack(0)
        return ans