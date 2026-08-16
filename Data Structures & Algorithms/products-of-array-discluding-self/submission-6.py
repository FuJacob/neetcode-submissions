class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        ans = [1] * n
        for i in range(1, n):
            ans[i] *= prefix * nums[i-1] 
            prefix *= nums[i-1]
        
        suffix = 1
        for i in range(n-2,-1,-1):
            ans[i] *= suffix * nums[i+1]
            suffix *= nums[i+1]
        
        return ans