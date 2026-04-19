class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curr = []
        ans = []
        n=len(nums)
        used = [False] * n ## ez way check if used
        def backtrack():
            if len(curr) == n:
                ans.append(curr[:])

            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                curr.append(nums[i])
                used[i] = True
                backtrack()
                curr.pop()
                used[i] = False



        backtrack() ## idxstarting at 
        return ans