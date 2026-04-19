class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r) //2
            if nums[m] == target:
                return m
            ## check which side of the array is sorted
            if nums[l] <= nums[m]:
                ## then it's sorted from this half, then we can do the proper check
                ## whether the target is actually in this half tho
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    ## else check ther right side
                    l = m +1
            else:
                ## right side is sorted
                ## check if it actualyl has it tho
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    ## else keep checking the other half
                    r = m - 1
        return -1