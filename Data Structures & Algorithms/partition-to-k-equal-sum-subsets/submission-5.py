class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % k != 0:
            return False
        size = total / k
        curr = [0] * k
        nums.sort(reverse=True)
        def backtrack(idx):
            if idx == n:
                if curr == [size] * k:
                    return True
                else: ## were at end it doesnt work
                    return False
            ## otehrwise we need tofigure a spot wher it go
            for i in range(k):

                if curr[i] + nums[idx] <= size:
                    curr[i] += nums[idx]
                    if backtrack(idx+1):
                        return True
                    curr[i] -= nums[idx]

                if curr[i] == 0:
                    return False
            return False
            
        return backtrack(0)