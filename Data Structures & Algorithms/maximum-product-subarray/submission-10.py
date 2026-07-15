class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        _max = [1] * n 
        _min = [1] * n ## min 
        _max[0] = _min[0] = nums[0]
        
        for i in range(1, n):
            if nums[i] >= 0:
                _max[i] = max(_max[i-1] * nums[i], nums[i])
                _min[i] = min(_min[i-1] * nums[i], nums[i])
            elif nums[i] < 0:
                _max[i] = max(_min[i-1] * nums[i], nums[i])
                _min[i] = min(_max[i-1] * nums[i],nums[i])
        return max(_max)


