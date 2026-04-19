class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        ptr = 0
        for i in range(len(nums)):
            if i - ptr > k:
                seen.remove(nums[ptr])
                ptr+=1
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
