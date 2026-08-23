class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        curr = []
        nums.sort()
        def backtrack(start):
            ans.append(curr[:])
            
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue ## skip duplicate
                curr.append(nums[i])
                backtrack(i+1)
                curr.pop()
        backtrack(0)
        return ans
