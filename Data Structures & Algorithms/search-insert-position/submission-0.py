class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo,hi = 0, n ## bounds exclusive
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        ## atp, lo shiod obe the first bad
        ## so whers hould idx be?
        return lo
            

