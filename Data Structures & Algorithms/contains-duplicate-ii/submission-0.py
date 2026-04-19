class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        ptr = 0
        for i in range(len(nums)):
            ## ensrue window valid first because we cantj ust add otherwise were off by one
            while i - ptr > k:
                seen.remove(nums[ptr])
                ptr+=1
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
