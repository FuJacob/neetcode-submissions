class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        curr = []
        used_idxs = set()
        seen = set() ## to stop duplicae
        def backtrack(start):
            key = tuple(curr)
            if len(curr) == n and key not in seen:
                ans.append(curr[:])
                seen.add(key)
                return
            
            for i in range(start, n):
                if i in used_idxs:
                    continue
                curr.append(nums[i])
                used_idxs.add(i)
                ## bu u can pick it out of order tho too
                ## so. uneed to start from start + 1 regardlss
                ## then maitnia duplciates 
                backtrack(start)
                curr.pop()
                used_idxs.remove(i)

        backtrack(0)
        return ans
