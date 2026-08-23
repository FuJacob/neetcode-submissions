class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        ans = []
        n = len(nums)
        curr = []
        def backtrack(start):
            ans.append(curr[:])
            seen.add(tuple(curr))
            if start == n:
                return
            
            for i in range(start, n):
                curr.append(nums[i])
                if tuple(curr) not in seen:
                    backtrack(i+1)
                curr.pop()
        backtrack(0)
        return ans

                    


