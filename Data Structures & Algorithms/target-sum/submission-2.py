class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ## key = curr sum
        ## val = # ways
        dp = {0: 1} ## sparse data, limited # of items
        for num in nums:
            curr = {}
            for key,val in dp.items():
                ## biuld upon it 
                curr[key+num] = curr.get(key+num,0) +val
                curr[key-num] = curr.get(key-num,0) +val
            dp = curr
        return dp.get(target,0)
            
