class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        curr = []
        used_idxs = set()
        def backtrack():
            key = tuple(curr)
            if len(curr) == n:
                ans.append(curr[:])
                return
            
            for i in range(0, n):
                if i in used_idxs:
                    continue
                curr.append(nums[i])
                used_idxs.add(i)
                backtrack()
                curr.pop()
                used_idxs.remove(i)
        backtrack()
        return ans
