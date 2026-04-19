class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthest_idx = 0 ## this is how far we can go
        tmp_farthest_idx = 0 ## this is how far tehcncially we can go, lets not commit to it yet though because
        n = len(nums)
        for idx, jump in enumerate(nums):
            if idx > farthest_idx: ## if we need ot spawn a jump ( we know there alwtys a solutino), then we take it afte explrogin this winowd
                jumps+=1
                farthest_idx = tmp_farthest_idx ## then we udpate our farthest inex
            tmp_farthest_idx = max(tmp_farthest_idx, idx+jump) ## toherwsie keep track of how far we can really jump now
            if n - 1 <= farthest_idx: ## if we can hit end just reutnr instantly 
                return jumps
        return jumps


            