class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        curr = []
        candidates.sort()
        def backtrack(start, _sum):
            if _sum == target:
                sol.append(curr[:])
                return
            for i in range(start, len(candidates)):
                ## not zero, would be same loop depth
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if _sum + candidates[i] <= target:
                    curr.append(candidates[i])
                    backtrack(i+1, _sum + candidates[i])
                    curr.pop()
        backtrack(0, 0)
        return sol