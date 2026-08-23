class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        curr = []
        candidates.sort()
        def backtrack(start, total):
            if total == target:
                ans.append(curr[:])
            
            if total > target:
                return
            
            for i in range(start, n): ## if i is bigger thna strat,  of this recursion levle, and and b4 candidatei s equal skip
            ## if i les htan recursion lvl its not teh same 
                if i > start and candidates[i] == candidates[i-1]: ## past orginal reciruson level? 
                    continue
                curr.append(candidates[i])
                backtrack(i+1, total + candidates[i])
                curr.pop()
            
        backtrack(0,0)
        return ans
