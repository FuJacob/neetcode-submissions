class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        n = len(nums)
        for num in nums:
            if num == 0:
                zeros+=1
        if zeros > 1:
            return [0] * n
        ## product before X
        prefix = [1] * n
        ## product after X
        suffix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        ans = []
        for i in range(n):
            ans.append(prefix[i] * suffix[i])
        return ans
        




