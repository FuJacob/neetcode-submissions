class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = l + (r-l) // 2
            if nums[m] <= nums[r]:
                r = m
            else:
                l = m + 1
        ## l is pivot
        pivot = l
        if pivot == 0:
            l,r = 0, n - 1
        elif nums[pivot] <= target <= nums[-1]:
            l,r = pivot, n - 1
        else:
            l,r = 0, pivot - 1
        
        while l <= r:
            m = l + (r-l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1 
        return -1


