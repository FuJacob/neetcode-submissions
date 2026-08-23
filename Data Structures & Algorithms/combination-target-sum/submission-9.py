class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        curr = []
        ans = []
        def backtrack(start, total):
            if total == target:
                ans.append(curr[:])
            
            if start >= n or total > target:
                return
            
            for i in range(start, n):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                backtrack(i, total + nums[i]) 
                curr.pop()
        backtrack(0,0)
        return ans