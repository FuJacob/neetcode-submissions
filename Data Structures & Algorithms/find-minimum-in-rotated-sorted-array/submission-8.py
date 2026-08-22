class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0, n - 1
        while l < r:
            m = l + (r-l) // 2
            if nums[m] <= nums[r]:
                r = m
            else: ## nums m > nums r 
            ## ans mist bewenein beween
                l = m + 1
        ## hwen thisends well have 1 eleent left, it mus bthe pivot
        return nums[l]


        