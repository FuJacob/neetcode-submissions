class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        placement_ptr = 0
        for scanner_ptr in range(n):
            if nums[scanner_ptr] != val:
                nums[placement_ptr] = nums[scanner_ptr]
                placement_ptr +=1
        return placement_ptr