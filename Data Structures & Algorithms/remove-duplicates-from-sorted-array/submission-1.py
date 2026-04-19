class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen_ptr = 0
        seen = set()
        for idx, num in enumerate(nums):
            if num not in seen:
                nums[seen_ptr] = num
                seen.add(num) 
                seen_ptr+=1
        return seen_ptr


