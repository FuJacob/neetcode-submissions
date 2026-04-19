class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr = []
        ans = []
        def backtrack(start):
            if len(curr) == k:
                ans.append(curr[:])
                return
            
            for i in range(start,n+1):
                curr.append(i)
                backtrack(i+1)
                curr.pop()
        backtrack(1)
        return ans
