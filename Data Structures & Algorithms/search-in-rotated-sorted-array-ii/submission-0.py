class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        ## trying to find kid
        lo,hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                return True
            if nums[lo] == nums[mid] == nums[hi]:
                lo +=1
                hi-=1
            ## tryna find which side sorted? wait 
            elif nums[lo] <= nums[mid]:
                ## do we fall in here
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid+1
            else:
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid-1
        return False
